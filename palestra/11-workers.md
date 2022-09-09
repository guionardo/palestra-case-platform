# Algum código

Note: os fontes mostrados aqui foram reconstruídos de forma muito simplificada, para fins de demonstração e por motivos de detalhes sensíveis de implementação utilizados em produção.
--

## Worker Genérico

```python
class GenericWorker:

    def __init__(self, stop_control, **kwargs):
        self._kwargs = {'stop_control': stop_control, **kwargs}

    def iteration_code(self, **kwargs):
        """Execution code that will run in 
        a loop until stop control commands stopping"""

    def _loop(self, stop_control):
        while stop_control.can_run():
            self.iteration_code(**self._kwargs)

    def get_thread(self):
        return threading.Thread(
            name=self.__class__.__name__,
            daemon=True,
            target=self._loop,            
            kwargs=self._kwargs
        )
```
--
## Worker Coletor de arquivos

```python
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

```

Note: Função coletar os arquivos, ordenar por escalonamento e enfileirar para consumo do SenderWorker
--
## Worker para envio de arquivos

```python
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
        result_queue = files_sender(file_queue.queue, 
                                    circuit_breaker)
        ack_count = nack_count = retry_count = 0
        for (filename, 
             status_code, 
             response_body) in result_queue.queue:
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
```
--
## Worker para envio de métricas
```python
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

        if metrics:
            # Publish using HTTP API
            _publish_to_metric_api(dict(metrics))

        time.sleep(30)
```
--
## main
```python
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

```