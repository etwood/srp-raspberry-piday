#!/bin/sh

TTY="$(tty)"
echo "${TTY}"

if [ $TTY = "/dev/pts/0" ]; then
	echo "This is the PiDay data collection script! Dont close this window!"
	script -q -c "python /home/pi/srp/piday/piday.py" /dev/null | tee -a /home/pi/srp/piday/output.csv 
else
	echo "Not starting piday.py on remote session"
fi
# python /home/pi/srp/piday/piday.py >> /home/pi/srp/piday/output.csv

