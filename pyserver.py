from flask import Flask
import os

app = Flask(__name__)

@app.route("/block")
def bloquear():

    os.system("C:/Windows/System32/rundll32.exe user32.dll,LockWorkStation")

    return "<h1>Sua máquina foi bloqueada</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded=True)
