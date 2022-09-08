# ARQUITETURA
--
<img src="images/arquitetura-c4.svg" height="80%"></img>
--
## Fluxo global
<table><tr><td>
<img src="images/arquitetura-provider-flow-global.svg"></img>
</td><td>
<p class="fragment fade-up"><span class="mdi mdi-hammer-screwdriver"></span> Configurações</p>
<p class="fragment fade-up"><span class="mdi mdi-stop-circle"></span> Controle de parada</p>
<p class="fragment fade-up"><span class="mdi mdi-robot"></span> Workers</p>
</td>
</tr>
</table>
--
## Controle de Execução
<table><tr><td>
<img src="images/arquitetura-provider-flow-stop-control.svg" height="80%"></img>
</td><td>
<p class="fragment fade-up"><span class="mdi mdi-window-closed-variant"></span> Janela de execução</p>
<p class="fragment fade-up"><span class="mdi mdi-content-save-all"></span> Backup</p>
<p class="fragment fade-up"><span class="mdi mdi-file-lock-open-outline"></span> Arquivo .STOP</p>
</td>
</tr></table>

--
<table><tr><td>
<img src="images/arquitetura-provider-flow-collector.svg" height="80%"></img>
</td><td>
<h2>Coletor de arquivos</h2>
<p class="fragment fade-up"><span class="mdi mdi-hammer-screwdriver"> Configurações</p>
<p class="fragment fade-up"><span class="mdi mdi-stop-circle"></span> Controle de parada</p>
<p class="fragment fade-up"><span class="mdi mdi-pipe"></span> Fila interna de envio</p>
<p class="fragment fade-up"><span class="mdi mdi-chart-bar"></span> Produção de estatísticas</p>
</td>
</tr></table>

--
<table><tr><td>
<img src="images/arquitetura-provider-flow-sender.svg"></img>
</td><td>
<h2>Envio</h2>
<p class="fragment fade-up"><span class="mdi mdi-hammer-screwdriver"> Configurações</p>
<p class="fragment fade-up"><span class="mdi mdi-stop-circle"></span> Controle de parada</p>
<p class="fragment fade-up"><span class="mdi mdi-pipe"></span> Fila interna de envio</p>
<p class="fragment fade-up"><span class="mdi mdi-api"></span> Comunicação com receivers</p>
<p class="fragment fade-up"><span class="mdi mdi-chart-bar"></span> Produção de estatísticas</p>
</td>
</tr></table>
--
<table><tr><td>
<img src="images/arquitetura-provider-flow-metric-publisher.svg" height="80%"></img>
</td><td>
<h2>Publicação de Métricas</h2>
<p class="fragment fade-up"><span class="mdi mdi-clock-start"></span> Intervalo entre envios</p>
<p class="fragment fade-up"><span class="mdi mdi-format-list-group"></span> Agregação</p>
<p class="fragment fade-up"><span class="mdi mdi-publish"></span> Envio para DataDog</p>
</td>
</tr>
</table>

