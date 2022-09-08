# Requisitos


## Requisitos

<table>
<tr><td width="30%"><img src="images/mri-0.png" /></td>
<td>ERP produzirá arquivos JSON de eventos que deverão ser enviados para mensageria.<br/>
Para receber estes arquivos será necessário um microsserviço de recebimento (API).
</td></tr></table>

Note: Robôs do ERP criarão arquivos JSON que


## Requisitos (v2)

<table>
<tr><td width="30%"><img src="images/mri-0.png" /></td>
<td>Os arquivos de eventos serão gravados em pastas correspontentes ao domínio que eles pertençem.</td></tr></table>


## Requisitos (v3)

<table>
<tr><td width="30%"><img src="images/mri-0.png" /></td>
<td>Além das pastas de domínio, os arquivos de eventos serão gravados em subpastas que indicam subdomínio.</td></tr></table>


## Requisitos (v4)

<table>
<tr><td width="30%"><img src="images/mri-1.png" /></td>
<td>Os arquivos de eventos podem ser enviados para diferentes serviços de recepção de acordo com o [sub]domínio via configuração.</td></tr></table>


## Requisitos (v5)

<table>
<tr><td width="30%"><img src="images/mri-1.png" /></td>
<td>O processo de envio dos arquivos deve contar com um mecanismo de <i>circuit-break</i>.</td></tr></table>

Note: O envio pode falhar por motivo de indisponibilidade dos serviços de recebimento, e nesse caso, deve-se controlar a taxa de envio ou o adiamento. Também pode falhar por motivo de payload inválido. Nesse caso o serviço de recebimento responde com um código de rejeição.


## Requisitos (v6)

<table>
<tr><td width="30%"><img src="images/mri-1.png" /></td>
<td>Arquivos enviados com sucesso devem ser movidos para pasta 'sent'.<br/>
Arquivos rejeitados pelas API's devem ser movidos para pasta 'error' com registro do motivo de rejeição.</td></tr></table>


## Requisitos (v7)

<table>
<tr><td width="30%"><img src="images/mri-1.png" /></td>
<td>Devem ser coletadas métricas:<br/>
- Arquivos aguardando envio,<br/>
- Arquivos enviados,<br/>
- Erros de envio,<br/>
- Espaço em disco ocupado.
</td></tr></table>

Note: As métricas coletadas são enviadas para um serviço de monitoramento. No nosso caso, uma API que faz o encaminhamento para o DataDog.


## Requisitos (v8)

<table>
<tr><td width="30%"><img src="images/mri-0.png" /></td>
<td>Disponibilizar modo de interromper a execução.
</td></tr></table>

Note: O serviço será executado como um worker, de modo contínuo, e portanto necessita de um mecanismo que possa interromper a execução.