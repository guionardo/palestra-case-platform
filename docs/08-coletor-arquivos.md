# Worker: Coleta de arquivos

--

## Estratégias para ler arquivos das pastas monitoradas

--
### Estratégia 1

<ul>
<li class="fragment">A partir das configurações, iterar pelas pastas monitoradas (glob)</li>
<li class="fragment">Em cada pasta, iterar pelos arquivos</li>
<li class="fragment">Alimentar uma lista de arquivos a serem processados</li>
</ul>

--
<h3><span class="mdi mdi-comment-alert"></span> Problemas da estratégia 1</h3>

<ul>
<li class="fragment">A iteração das pastas e arquivos se tornou lenta em pastas muito populosas</li>
<li class="fragment">Era necessário aguardar a iteração completar para obter o primeiro item da lista</li>
</ul>

--
### Estratégia 2

<ul>
<li class="fragment"><span class="mdi mdi-head-question"/> Melhorar a iteração dos arquivos.</li>
<li class="fragment"><span class="mdi mdi-head-question"/> Identificar os meios em python para iterar.
<ul class="fragment">
    <li>glob / iglob</li>
    <li>os.walk</li>
    <li>os.scandir</li>
    <li>pathlib.Path</li>
</ul>
</li>

<li class="fragment"><span class="mdi mdi-head-heart"/> Essa pesquisa produziu informações interessantes documentadas <a href="https://dev.to/guionardo/fast-folder-iteration-in-python-3g1f" target="new">aqui</a>.</li>
<li class="fragment"><span class="mdi mdi-head-heart"/> O método de iteração de arquivos escolhido foi <i><a href="https://docs.python.org/3/library/os.html#os.scandir" target="new">os.scandir</a></i>.</li>
</ul>

--
### Iterando arquivos: os.scandir

- Uso de generator
- Minimizado o consumo de memória
- Retorno imediato ao primeiro arquivo encontrado
- Ótima performance com qualquer situação de quantidade de arquivos

```python
def get_files(folder: str):
    with os.scandir(folder) as scan:
        for item in scan:
            if item.is_file():
                yield item.path
            else:
                for subitem in get_files(item.path):
                    yield subitem
```

--
<h3><span class="mdi mdi-comment-alert"></span> Pendências da estratégia 2</h3>

<ul>
<li class="fragment">A lista obtida estava em ordem de pasta/arquivo</li>
</ul>
--
### Estratégia 3

<ul>
<li class="fragment">Escalonar a ordem dos arquivos</li>
</ul>
--
### Exemplo de distribuição de arquivos

```
├── folder1
│   ├── file001
│   ├── file002
│   ├── file003
│   ├── file004
│   └── file005
├── folder2
│   ├── file001
│   ├── file002
│   ├── file003
│   ├── file004
│   └── file005
└── folder3
    ├── file001
    ├── file002
    ├── file003
    ├── file004
    └── file005
```
--
### Resultado da iteração dos arquivos

``` python
['folder1/file001',
 'folder1/file002',
 'folder1/file003',
 'folder1/file004',
 'folder1/file005',
 'folder2/file001',
 'folder2/file002',
 'folder2/file003',
 'folder2/file004',
 'folder2/file005',
 'folder3/file001',
 'folder3/file002',
 'folder3/file003',
 'folder3/file004',
 'folder3/file005'
]
```
--
### Escalonamento necessário para envio
``` python
['folder1/file001',
 'folder2/file001',
 'folder3/file001',
 'folder1/file002',
 'folder2/file002',
 'folder3/file002',
 'folder1/file003',
 'folder2/file003',
 'folder3/file003',
 'folder1/file004',
 'folder2/file004',
 'folder3/file004',
 'folder1/file005',
 'folder2/file005',
 'folder3/file005'
]
```
--
### Escalonando arquivos

A função schedule_files retornará um generator que entregará os arquivos na ordem necessária para o envio escalonado entre pastas.

```python
file_generators = [get_files('/tmp/sample/'+folder) 
                   for folder in ['folder00',
                                  'folder01',
                                  'folder02']]

def schedule_files(file_generators):
    g_index = -1
    while len(file_generators)>0:
        g_index = (g_index + 1) % len(file_generators)
        file_generator = file_generators[g_index]
        try:
            file_name = next(file_generator)
            yield file_name
            
        except StopIteration:
            file_generators.pop(g_index)

```

--
<h3><span class="mdi mdi-head-heart"></span> Estratégia de coleta de arquivos</h3>

<ul>
<li class="fragment">A partir das configurações, iterar pelas pastas monitoradas</li>
<li class="fragment">Coleta dos arquivos usando generators para cada pasta</li>
<li class="fragment">Escalonamento dos arquivos</li>
<li class="fragment">Arquivos coletados alimentando uma fila <i>queue.Queue</i>.</li>
</ul>