import queue

from src.workers.generic_worker import GenericWorker


class SenderWorker(GenericWorker):

    def __init__(self, stop_control,
                 file_queue: queue.Queue,
                 circuit_breaker: CircuitBreaker,
                 metric_queue: queue.Queue):

        super().__init__(stop_control,
                         file_queue=file_queue,
                         circuit_breaker=circuit_breaker,
                         metric_queue=metric_queue)

    def iteration_code(self, **kwargs):
        file_queue = kwargs['file_queue']
        circuit_breaker = kwargs['circuit_breaker']
        result_queue = files_sender(file_queue.queue, circuit_breaker)
        ack_count = nack_count = retry_count = 0
        for (filename, status_code, response_body) in result_queue.queue:
            if 200 <= status_code < 300:
                ack_count += 1
            elif 400 <= status_code < 500:
                nack_count += 1
            else:
                retry_count += 1
        metric_queue = kwargs['metric_queue']
        metric_queue.put(('ack', ack_count))
        metric_queue.put(('nack', nack_count))
        metric_queue.put(('retry', retry_count))
