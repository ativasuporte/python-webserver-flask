from flask import Flask
import os
import time
import requests

app = Flask(__name__)


@app.route("/chamados")
def chamados():
    r = requests.get("https://script.google.com/macros/s/AKfycbzOjBDFdWihG4yQY-tI7kIsLwcGsaSSt4p-t6yzo5ZW5chzyj0s4WPfiD-lWPqSoo8/exec")
    return "Temos "+r.text+" chamados pendentes!"

@app.route("/video/<pasta>/<nome>")
def video(pasta, nome):
    home = os.path.expanduser("~")
    print(home, pasta, nome)
    arquivo = home + "\\" + pasta + "\\" + nome
    os.system("start " + arquivo)
    return "O vídeo " + nome + " está passando!"

@app.route("/block")
def bloquear():
    os.system("C:/Windows/System32/rundll32.exe user32.dll,LockWorkStation")
    return "Sua máquina foi bloqueada!"

@app.route("/shutdown")
def desligar():
    os.system("shutdown -s -t 2")
    return "Sua máquina está desligando..."

@app.route("/reboot")
def reiniciar():
    os.system("shutdown -r -t 2")
    return "Reiniciando..."

@app.route("/mouse")
def mouse():
    #tela = pyautogui.size()
    #largura = tela[0]
    #altura = tela[1]
    #pyautogui.moveTo(largura/2, altura/2)
    #time.sleep(1)
    #pyautogui.click()
    return "Desbloqueado!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded=True)
