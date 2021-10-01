from flask import Flask
import os
import time
import pyautogui
import keyboard

app = Flask(__name__)

def escrever_senha():
    time.sleep(1)
    print("VOU ESCREVER")
    senha = "JTA*sup"
    keyboard.write(senha)
    print("VOU DAR ENTER")
    keyboard.press_and_release('enter')
    print("DEI ENTER")

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
    tela = pyautogui.size()
    largura = tela[0]
    altura = tela[1]
    pyautogui.moveTo(largura/2, altura/2)
    time.sleep(1)
    pyautogui.click()
    escrever_senha()
    return "Desbloqueado!"


if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded=True)
