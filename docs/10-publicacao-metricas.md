# Publicação de métricas

--

## Estratégias para publicação de métricas

--
### Estratégia 1

<ul>
<li class="fragment">Obter estatísticas nos workers de coleta e envio de arquivos.</li>
<li class="fragment">Utilizar um contexto singleton para receber as estatísticas (queue).</li>
<li class="fragment">Worker de execução periódica para agregar as estatísticas e enviar à API de métricas.</li>
</ul>

Note: Novamente o uso de Queue possibilita uma fila thread safe.

