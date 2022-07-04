# PITFALLS

<img src="https://classic.exame.com/wp-content/uploads/2017/08/pitfall-activision.png?w=480"/><br/>
<small>(Activision/Reprodução)</small>


## Buraco (1)

<table>
<tr><td width="30%"><img src="assets/mri-2.png" /></td>
<td>Ambiente AIX disponibiliza apenas python 2.6.8.</td></tr></table>


## Buraco (2)

<table>
<tr><td width="30%"><img src="assets/mri-3.png" /></td>
<td>Ambiente AIX não disponibiliza o python com uso de pacotes de terceiros via pip.<br/>
Todo o desenvolvimento deve ser feito usando a biblioteca padrão.</td>
</td></tr></table>

Note: Robôs do ERP criarão arquivos JSON que


## Buraco (3)

<table>
<tr><td width="30%"><img src="assets/mri-2.png" /></td>
<td>O serviço de captura de arquivos vai concorrer com centenas de outros serviços no acesso ao sistema de arquivos, memória e CPU.</td></tr></table>


## Buraco (4)

<table>
<tr><td width="30%"><img src="assets/mri-3.png" /></td>
<td>Ambiente AIX não disponibiliza recursos de SSL, impossibilitando o uso de requests HTTPS via urllib.</td></tr></table>


## Buraco (5)

<table>
<tr><td width="30%"><img src="assets/mri-1.png" /></td>
<td>Deve ser implementada uma rotina de house-keeping para remover arquivos antigos.</td></tr></table>


## Buraco (6)

<table>
<tr><td width="30%"><img src="assets/mri-3.png" /></td>
<td>O volume de arquivos produzidos pelos robôs, em ambiente de desenvolvimento é estimado em 84 mil por iteração a cada 1 a 5 minutos.<br/>
Em ambiente de produção pode chegar a dez vezes mais.</td></tr></table>


## Buraco (7)

<table>
<tr><td width="30%"><img src="assets/mri-2.png" /></td>
<td>Os ambientes do AIX e do AKS estão em redes separadas. Dessa forma a latência e a banda de rede impactam no processamento.</td></tr></table>