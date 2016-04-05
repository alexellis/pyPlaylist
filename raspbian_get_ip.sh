#!/bin/sh

ifconfig eth0|grep "inet addr"|cut -d":" -f2|cut -d" " -f1
ifconfig wlan0|grep "inet addr"|cut -d":" -f2|cut -d" " -f1
