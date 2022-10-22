#!/bin/zsh

# Screen toggle
# By Putzak

CUR=$(brightnessctl -m | awk -F ',' '{print $4}')

if
	[ $CUR != "0%" ];
then;
	print "NCUR=$CUR" > ~/.screencur.txt;
	NCUR="0%"
else
	source ~/.screencur.txt
fi

brightnessctl set $NCUR

echo $CUR
echo $NCUR
