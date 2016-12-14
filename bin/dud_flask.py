#!/usr/bin/python
from flask import Flask
import dud
from subprocess import call

app = Flask(__name__)

@app.route("/status")
def _status():
    return str(dud.statusRelay())

@app.route("/off")
def _off():
    call(["/usr/local/bin/daemon.pl", "/usr/local/bin/dud-ctl","reset"])
    return str(0)
    #return str(dud.setRelay(0))

@app.route("/<int:onForMins>min")
def _onxmin(onForMins):
    call(["/usr/local/bin/daemon.pl", "/usr/local/bin/dud-ctl", "xmin","%d"%onForMins])
    return str(1)

@app.route("/on")
def _on():
    call(["/usr/local/bin/daemon.pl", "/usr/local/bin/dud-ctl","xmin","45"])
    return str(1)

@app.route("/")
def _help():
    return "dud  &lt;on|off|status&gt;"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #app.run()
