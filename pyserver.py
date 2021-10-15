#JOÃO PEDRO, TI - ATIVA NÁUTICA
#VERSÃO 1.0


from flask import Flask
from flask import request
import os
import sys
import time
import requests
from subprocess import call

app = Flask(__name__)

pyautogui.FAILSAFE = False

APP_DEBUG = False

#Utilize '--debug' na linha de comando para iniciar em modo de debug:
if len(sys.argv) > 1 and "--debug" in sys.argv:
    print("RODANDO EM MODO DE DEBUG...")
    APP_DEBUG = True

ARQUIVO = sys.executable

@app.route("/close")
def fechar_conexao():
    func = request.environ.get("werkzeug.server.shutdown")

    if func is None:
        raise RuntimeError("Server não está rodando")

    func()

    if APP_DEBUG == True:
        os.system(f"start python {__file__}")

    else:
        os.system("start " + ARQUIVO)

    return "Servidor reiniciando..."

@app.route("/ping")
def ping():
    try:
        ip = request.headers.get('Host')
        return "Tudo ok! IP: " + ip
    except:
        return "Erro na conexão!"

@app.route("/chamados")
def chamados():
    r = requests.get("https://script.google.com/macros/s/AKfycbzOjBDFdWihG4yQY-tI7kIsLwcGsaSSt4p-t6yzo5ZW5chzyj0s4WPfiD-lWPqSoo8/exec")
    return "Temos "+r.text+" chamados pendentes!"

@app.route("/video/<pasta>/<nome>")
def video(pasta, nome):
    home = os.path.expanduser("~")
    arquivo = home + "\\" + pasta + "\\" + nome
    try:
        os.system("start " + arquivo)
        return "O vídeo " + nome + " está passando!"
    except:
        return "Houve algum problema na reprodução do vídeo..."

@app.route("/block")
def bloquear():
    try:
        call("C:/Windows/System32/rundll32.exe user32.dll,LockWorkStation")
        return "Sua máquina foi bloqueada!"
    except:
        return "Houve algum problema..."

@app.route("/shutdown")
def desligar():
    try:
        call("shutdown -s -t 1")
        return "Sua máquina está desligando..."
    except:
        return "Houve algum problema..."

@app.route("/reboot")
def reiniciar():
    try:
        call("shutdown -r -t 1")
        return "Reiniciando..."
    except:
        return "Houve algum problema..."

if __name__ == "__main__":

    app.run(host='0.0.0.0',threaded=True)

    #mete um request pra um webapp que registra a sessão como ativa (IP, porta, etc)
