# PITFALLS


## Buraco (v1)

<table>
<tr><td width="30%"><img src="assets/mri-2.png" /></td>
<td>Ambiente AIX não disponibiliza o python com uso de pacotes de terceiros via pip.</td>
</td></tr></table>

Note: Robôs do ERP criarão arquivos JSON que


## Buraco (v2)

<table>
<tr><td width="30%"><img src="assets/mri-2.png" /></td>
<td>O serviço de captura de arquivos vai concorrer com centenas de outros serviços no acesso ao sistema de arquivos, memória e CPU.</td></tr></table>


## Buraco (v3)

<table>
<tr><td width="30%"><img src="assets/mri-2.png" /></td>
<td>Ambiente AIX disponibiliza apenas python 2.7. Todo o desenvolvimento deve ser feito usando a biblioteca padrão.</td></tr></table>


## Buraco (v4)

<table>
<tr><td width="30%"><img src="assets/mri-3.png" /></td>
<td>Ambiente AIX não disponibiliza recursos de SSL, impossibilitando o uso de requests HTTPS via urllib.</td></tr></table>


## Buraco (v5)

<table>
<tr><td width="30%"><img src="assets/mri-1.png" /></td>
<td>Deve ser implementada uma rotina de house-keeping para remover arquivos antigos.</td></tr></table>


## Buraco (v6)

<table>
<tr><td width="30%"><img src="assets/mri-3.png" /></td>
<td>O volume de arquivos produzidos pelos robôs, em ambiente de desenvolvimento é estimado em 84 mil por iteração a cada 1 a 5 minutos.<br/>
Em ambiente de produção pode chegar a dez vezes mais.</td></tr></table>


## Buraco (v7)

<table>
<tr><td width="30%"><img src="assets/mri-2.png" /></td>
<td>Os ambientes do AIX e do AKS estão em redes separadas. Dessa forma a latência e a banda de rede impactam no processamento.</td></tr></table>