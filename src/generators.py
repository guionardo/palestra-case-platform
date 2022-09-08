import os
from queue import Queue
from typing import Generator
import concurrent.futures


def get_files(folder: str) -> Generator:
    with os.scandir(folder) as scan:
        for item in scan:
            if item.is_file():
                yield item.path
            else:
                for subitem in get_files(item.path):
                    yield subitem

NF = 3
NA = 100 # 0000
print('Criando arquivos')
tc=0
for f in range(NF):
    folder=os.path.join('/tmp','sample',f'folder{f:02}')
    print(folder)
    os.makedirs(folder,exist_ok=True)
    for fi in range(NA):
        filename=os.path.join(folder,f'file_{f:02}_{fi:06}')
        with open(filename,'w') as file:
            file.write('0')
        tc+=1
print('Criados',tc,'arquivos')
        

file_generators = [get_files('/tmp/sample/'+folder) for folder in ['folder00','folder01','folder02']]


def schedule_files(file_generators):
    g_index = -1
    while len(file_generators)>0:
        g_index = (g_index + 1) % len(file_generators)
        file_generator = file_generators[g_index]
        try:
            file_name = next(file_generator)
            yield file_name
            
        except StopIteration:
            file_generators.pop(g_index)
        
def send_file(result_queue,**kwargs):
    result_queue.put(kwargs)
    print(kwargs)

def files_sender(scheduled_files):
    result_queue=Queue()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures=[]
        total_done= total_not_done=0
        
        def futures_wait():
            nonlocal futures,total_done,total_not_done
            if len(futures)==0:
                return
            done, not_done = concurrent.futures.wait(futures)
            total_done += len(done)
            total_not_done+=len(not_done)
            futures.clear()            

        for filename in scheduled_files:            
            receiver_url = '' # get_receiver_url(filename)
            futures.append(
                executor.submit(send_file,
                                filename=filename,
                                receiver_url=receiver_url,
                                result_queue=result_queue))
            if len(futures)==128:
                futures_wait()
                
        futures_wait()
        
    if total_not_done>0:
        print('Tasks not completed',total_not_done)
    print('Tasks done',total_done)
    return result_queue


# for file in schedule_files(file_generators):
#     print(file)

q=files_sender(schedule_files(file_generators))
print(q.qsize())
