# REFRESCOS

Note: Negociações e boas conversas melhoraram nosso cenário.
--
## Refresco (1)

<table>
<tr><td width="30%"><img src="images/mri-0.png" /></td>
<td>Atualização do python para a versão 3.8.5</td></tr></table>

Note: Toda modificação nos ambientes AIX só ocorre por meio de um processo de change, onde uma equipe é responsável por implantar os programas, arquivos e configurações necessárias. Todo o processo é necessariamente burocrático, documental e depende de autorizações, pois sendo um ambiente compartilhado, o impacto pode ser grave caso uma solução não testada seja implantada.
--
## Buraco (2)

<table>
<tr><td width="30%"><img src="images/mri-1.png" /></td>
<td>PIP não será liberado.<br/>
Todo o desenvolvimento deve ser feito usando a biblioteca padrão.</td>
</td></tr></table>

Note: É justificável. Pip pode facilitar a instalação de rotinas perigosas.
--
## Buraco (3)

<table>
<tr><td width="30%"><img src="images/mri-2.png" /></td>
<td>Concorrência com outros serviços é inevitável.</td></tr></table>

Note: Desafio para o desenvolvimento. Código deve ser otimizado tanto para consumo de memória quanto para as atividades paralelizadas.
--
## Refresco (4)

<table>
<tr><td width="30%"><img src="images/mri-0.png" /></td>
<td>Atualização do python resolveu o problema com o SSL.</td></tr></table>

Note: O binding do openssl foi corrigido na instalação da versão 3.8.
--
## Refresco (5)

<table>
<tr><td width="30%"><img src="images/mri-0.png" /></td>
<td>Responsabilidade do house keeping foi delegada a outro serviço.</td></tr></table>

Note: O house keeping era necessário em outras pasta do sistema além das monitoradas pelo sistema de exportação de dados, então foi implementado em outro serviço. 
--
## Buraco (6)

<table>
<tr><td width="30%"><img src="images/mri-2.png" /></td>
<td>Volume de mensagens é inevitável.</td></tr></table>

Note: Novamente um desafio para o desenvolvimento. A performance e a estratégia na captura dos arquivos de eventos é crucial para a entrega das informações a uma taxa média maior do que a produção.
--
## Refresco (7)

<table>
<tr><td width="30%"><img src="images/mri-1.png" /></td>
<td>Latência de rede pode ser contornada com o uso de pool de conexões HTTP e compactação dos payloads durante a transmissão para as APIs.</td></tr></table>

Note: Com a utilização de código nativo da urllib, foi possível economizar conexões HTTP e compactar os payloads como GZIP.