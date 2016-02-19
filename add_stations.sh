#!/bin/sh

rm ~/.mpd/playlists/*

mpc clear
curl http://www.radiofeeds.co.uk/bbcradio1.pls|cat|grep 'File1'|cut -d\= -f2-20 |mpc add
mpc save BBCRadio1

mpc clear
curl http://www.radiofeeds.co.uk/bbcradio2.pls|cat|grep 'File1'|cut -d\= -f2-20 |mpc add
mpc save BBCRadio2

mpc clear
curl http://www.radiofeeds.co.uk/bbcradio4fm.pls|cat|grep 'File1'|cut -d\= -f2-20 |mpc add
mpc save BBCRadio4

mpc clear
curl http://icy-e-ba-08-boh.sharp-stream.com/kissnational.mp3.m3u|cat|mpc add
mpc save KissFM
