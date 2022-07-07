import json
import os
from typing import List

class BaseConfiguration:

    def _get_fields(self, data: dict, **fields)->List[any]:
        result=[]
        for field in fields:
            if field not in data:
                raise ValueError(f'{field} is not in the {self.__class__.__name__}')
            
            result.append(data[field])
        return result

class SourceConfiguration(BaseConfiguration):

    def __init__(self, data:dict):
        self.path,self.host = self._get_fields(data, 'path', 'host')
        

class StopConfiguration(BaseConfiguration):

    def __init__(self,data:dict):
        self.stop_file,self.start_time,self.stop_time=self._get_fields(data, 'stop_file','start_time','stop_time')
        
        
class Configuration(BaseConfiguration):

    def __init__(self, filename:str):
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)
        self._filename = filename
        self._modification_time = 0
        self.sources:List[SourceConfiguration] = []


    def load(self):
        if self._modification_time>=os.path.getmtime(self._filename):
            return
        
        with open(self._filename) as file:
            data = json.load(file)
        
        self._modification_time = os.path.getmtime(self._filename)

        self.sources = [SourceConfiguration(subdata) for subdata in self._get_fields(data,'sources')]
        self.stop = StopConfiguration(self._get_fields(data,'stop')[0])


