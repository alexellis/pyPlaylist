from flask import Flask, request, render_template

from mpc import *
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    player=Player()
    val = player.get_playlists()
    player.quit()
    return render_template("home.html", playlists=val)

@app.route('/stats/', methods=['GET'])
def stats():
    _stats = None
    player=Player()
    _stats= player.get_stats()
    player.quit()
    return json.dumps({"stats": _stats})

@app.route('/playing/', methods=['GET'])
def playing():
    playlist =None
    player=Player()
    val = player.get_playing()
    player.quit()
    return json.dumps({"playlist": val})

@app.route('/stop/', methods=['POST'])
def stop():
    playlist =None
    player=Player()
    player.stop()
    player.quit()
    return json.dumps({"status": "OK"})

@app.route('/resume/', methods=['POST'])
def resume():
    playlist =None
    player=Player()
    player.play()
    player.quit()
    return json.dumps({"status": "OK"})


@app.route('/play/', methods=['POST'])
def play():
    playlist =None

    if(request !=None and request.form!=None):
        for x in request.form:
            if(x=="playlist"):
                playlist = request.form[x]

    player=Player()
    if(playlist!=None):
        player.stop()

        _pl =None
        for pl in player.get_playlists():
            if(pl["playlist"]==playlist):
                _pl=pl
                break

        player.load(_pl["playlist"])
    player.play()
    player.quit()
    return json.dumps({"status": "OK"})


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
