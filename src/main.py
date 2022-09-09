import queue

from src.circuit_breaker import CircuitBreaker
from src.workers.collector_worker import CollectorWorker
from src.workers.sender_worker import SenderWorker
from src.workers.metric_publisher_worker import MetricPublisherWorker

stop_control = StopControl()
circuit_breaker = CircuitBreaker()
file_queue = queue.Queue()
collector_worker = CollectorWorker(stop_control,
                                   file_queue)
metric_queue = queue.Queue()
sender_worker = SenderWorker(stop_control,
                             file_queue,
                             circuit_breaker,
                             metric_queue)

metric_publisher_worker = MetricPublisherWorker(stop_control,
                                                metric_queue)

threads = [w.get_thread()
           for w in [collector_worker,
                     sender_worker,
                     metric_publisher_worker]]

for t in threads:
    t.start()

for t in threads:
    t.join()
