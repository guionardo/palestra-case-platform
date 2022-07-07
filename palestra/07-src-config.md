# CONFIGURAÇÕES


## Arquivo de configuração

```json
{
    "sources": [
        {
            "path": "/data/extract/customers/*/*.json",
            "host": "http://api.localhost:8080"
        },
        {
            "path": "/data/extract/finance/*/*.json",
            "host":"http://api2.localhost:8080"
        }
    ],
    "stop": {
        "stop_file": "/data/extract/EXTRACTION.STOP",
        "start_time": "00:00:00",
        "stop_time": "00:00:00"
    }
}
```


## Classe básica de configuração

```python
class BaseConfiguration:

    def _get_fields(self, data: dict, **fields)->List[any]:
        result=[]
        for field in fields:
            if field not in data:
                raise ValueError('Missing field',
                                 field,self.__class__.__name__)
            
            result.append(data[field])
        return result
```


## Classe de configuração de controle de parada

```python
class StopConfiguration(BaseConfiguration):

    def __init__(self,data:dict):
        (self.stop_file,
         self.start_time,
         self.stop_time) = self._get_fields(data, 
                                            'stop_file',
                                            'start_time',
                                            'stop_time')
```


## Classe de configuração de fontes de dados

```python
class SourceConfiguration(BaseConfiguration):

    def __init__(self, data:dict):
        (self.path,
         self.host) = self._get_fields(data, 
                                       'path', 
                                       'host')
```