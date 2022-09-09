from collections import defaultdict

from src.workers.generic_worker import GenericWorker


class MetricPublisherWorker(GenericWorker):

    def __init__(self, stop_control, metric_queue):
        super().__init__(stop_control, metric_queue=metric_queue)

    def iteration_code(self, **kwargs):
        metric_queue = kwargs.get('metric_queue')
        metrics = defaultdict(int)

        # Aggregate metrics with same name
        for (metric_name, metric_value) in metric_queue.queue:
            metrics[metric_name] += 1

        # Publish using HTTP API
        _publish_to_datadog(dict(metrics))

        time.sleep(30)
