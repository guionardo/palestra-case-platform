import concurrent.futures

def files_sender(scheduled_files, circuit_breaker):
    result_queue = Queue()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        total_done = total_not_done = 0
        
        def futures_wait():
            nonlocal futures, total_done, total_not_done
            if len(futures) == 0:
                return
            done, not_done = concurrent.futures.wait(futures)
            total_done += len(done)
            total_not_done += len(not_done)
            futures.clear()

        for filename in scheduled_files:
            receiver_url = ''  # get_receiver_url(filename)
            futures.append(
                executor.submit(send_file,
                                filename=filename,
                                receiver_url=receiver_url,
                                result_queue=result_queue,
                                circuit_breaker=circuit_breaker))
            if len(futures) == 128:
                futures_wait()

        futures_wait()

    if total_not_done > 0:
        print('Tasks not completed', total_not_done)
    print('Tasks done', total_done)
    return result_queue
