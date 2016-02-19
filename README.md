# pyPlaylist
Python playlist selector for MPC

## Installation

* Install MPC / MPD

```
# bower install
```

Bower may require node.js, if required dependencies can be installed on another computer and copied across with scp.

With PIP:

```
# sudo pip install flask python-mpd2
```

With easy_install:
```
# sudo easy_install flask python-mpd2
```

## Starting/using the app

Your existing playlists will be read from `mpd`, but if you do not have any then you can add some by using the `add_stations.sh` bash script. It will add several popular British radio stations.

Run `python app.py` then navigate to [http://localhost:5000](http://localhost:5000) to select one of the playlists you have saved in MPD.
