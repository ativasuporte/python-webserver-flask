# Controle Remoto

Esse é o script por trás do funcionamento dos "controles remotos" do dep. de TI.

É necessário configurar a máquina para que ela tenha um IP FIXO. Do contrário, a conexão pode ser perdida, sendo necessário reinicar o app manualmente sempre que o IP trocar.

O app funciona melhor em conjunto com aplicativos de gerenciamento/criação de atalhos para requisições HTTP. Recomendo o uso do "HTTP Shortcuts", disponível na Play Store (Android).

Todos os atalhos funcionam com o método HTTP **GET**

**Pra iniciar o servidor, é só rodar o arquivo _pyserver.exe_, presente na pasta dist/**

**SUBSTITUA {IP} PELO ENDEREÇO DO SERVIDOR NA SUA MÁQUINA (XXX.XXX.X.XX:YYYY)!**

## Os métodos disponíveis atualmente são:

### Desligar a máquina - http://{IP}/shutdown

Desliga sua máquina

### Reiniciar a máquina - http://{IP}/reboot

Reinicia sua máquina

### Bloquear a sessão de usuário - http://{IP}/block

Bloqueia sua sessão (como se você tivesse apertado Win + L)

### Checar a conexão - http://{IP}/ping

Manda um "pingzinho" pro servidor, pra conferir se a conexão está OK

### Reproduzir arquivo (vídeo, música, etc.) - http://{IP}/<PASTA>/<ARQUIVO.extensão>

Reproduz algum arquivo, utilizando o programa padrão.
Considere PASTA como sendo a pasta onde o arquivo se encontra, dentro da sua HOME (C:/Users/USUÁRIO/PASTA)


**Sempre especifique a extensão do arquivo (.mp4, .avi, etc.)! Se possível, renomeie o arquivo para algo como "video_01.mp4", por exemplo. O app não lida bem com nomes com ESPAÇOS...**

### Reiniciar o app - http://{IP}/close

Reinicia o servidor, caso haja algum problema (mas ainda haja conexão)
Raramente essa função vai ser útil, mas melhor prevenir do que remediar.
