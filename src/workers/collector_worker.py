import queue

from src.workers.generic_worker import GenericWorker


class CollectorWorker(GenericWorker):

    def __init__(self, stop_control,
                 file_queue: queue.Queue,
                 metric_queue: queue.Queue):

        super().__init__(stop_control,
                         file_queue=file_queue,
                         metric_queue=metric_queue)

    def iteration_code(self, **kwargs):
        file_queue = kwargs['file_queue']
        metric_queue = kwargs['metric_queue']
        # Get folders from configuration
        folders = get_folders()
        file_generators = [get_files(folder)
                           for folder in folders]
        collected_file = 0
        for file in schedule_files(file_generators):
            file_queue.put(file)
            collected_file += 1
        metric_queue.put(('collected_file', collected_file))
