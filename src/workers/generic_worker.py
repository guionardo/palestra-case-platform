import threading


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
