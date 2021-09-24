from flask import Flask

app = Flask(__name__)

@app.route("/<maq>")
def hello_world(maq):
    print(maq)
    return "<h1>Ôbá!</h1><p>Bão?</p>"

app.run(host='0.0.0.0',threaded=True)
