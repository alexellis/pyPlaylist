# pyPlaylist
Python playlist selector for MPC

## Installation

* Install MPC / MPD

On Raspberry PI:

Use `pacman` or `apt-get install` for the two packages `mpc` and `mpd`.

On Mac, I suggest you use `brew`:

```
brew install mpd mpc
```

Then you will find the config file in `/usr/local/etc/mpd/` edit the config file to enable playlists and make a directory of `~/.mpd/`.


* Install bower components:

Bower installs client dependencies for Bootstrap and jQuery. 

```
# bower install
```

*NB: If you are using a low powered computer such as a Raspberry PI and do not want to install node.js, then you can perform this step on another computer and copy the bower_components folder across with scp.*

* Installing python libraries

Use `pip` or `easy_install` to configure flask (a lightweight MVC framework) and python-mpd2 which will talk to the UNIX/Linux music player.

```
# sudo pip install flask python-mpd2
```

With easy_install:
```
# sudo easy_install flask python-mpd2
```

## Starting/using the app

Your existing playlists will be read from `mpd`, but if you do not have any then you can add some by using the `add_stations.sh` bash script.

Run `python app.py` then navigate to [http://localhost:5000](http://localhost:5000) to select one of the playlists you have saved in MPD.
