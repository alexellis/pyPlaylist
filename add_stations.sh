#!/bin/sh

if [ -e personal_stations.sh ]; then
  sh ./personal_stations.sh
fi

rm ~/.mpd/playlists/*

mpc clear
curl -s http://www.radiofeeds.co.uk/bbcradio1.pls|cat|grep 'File1'|cut -d\= -f2-20 |mpc add
mpc save BBCRadio1

mpc clear
curl -s http://www.radiofeeds.co.uk/bbcradio2.pls|cat|grep 'File1'|cut -d\= -f2-20 |mpc add
mpc save BBCRadio2

mpc clear
curl -s http://www.radiofeeds.co.uk/bbcradio4fm.pls|cat|grep 'File1'|cut -d\= -f2-20 |mpc add
mpc save BBCRadio4

mpc clear
curl -s http://www.radiofeeds.co.uk/bbc6music.pls|cat|grep 'File1'|cut -d\= -f2-20 |mpc add
mpc save BBC6Music

mpc clear
curl -s http://icy-e-ba-08-boh.sharp-stream.com/kissnational.mp3.m3u|cat|mpc add
mpc save KissFM

mpc clear
curl -s http://media-ice.musicradio.com/CapitalXTRANationalMP3.m3u|cat|mpc add
mpc save CapitalXtra

echo "Stations added."
