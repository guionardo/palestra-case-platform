from src.s_01_config.config import Configuration
import os
import datetime

class StopControl:

    def __init__(self, config:Configuration):
        self.config = config

    def can_run(self)->bool:
        self.config.load()
        return (not os.path.isfile(self.config.stop.stop_file)
            and self.start_time<=datetime.datetime.now().strftime('%H:%m:%s')<=self.stop_time)
        
