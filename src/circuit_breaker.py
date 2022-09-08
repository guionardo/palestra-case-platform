import time
from datetime import datetime, timedelta


class CircuitBreaker:

    def __init__(self):
        self._receivers = {}

    def open(self, url):
        if not self._receivers.get(url):
            self._receivers[url] = datetime.now()+timedelta(seconds=5)

    def close(self, url):
        if url in self._receivers:
            self._receivers.pop(url)

    def wait(self, url):
        if url not in self:
            return
        if self._receivers.get(url) > datetime.now():
            time.sleep(self._receivers.get(url)-datetime.now())
        self.close(url)
