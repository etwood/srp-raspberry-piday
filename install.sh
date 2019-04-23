#!/bin/bash



DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "$DIR"

set +x
echo "install logrotate config"
ln -f -s $DIR/etc/piday-logrotate /etc/logrotate.d/piday-logrotate 
chown root /etc/logrotate.d/piday-logrotate
chown root $DIR/etc/piday-logrotate


echo "enable piday script start on boot"
mkdir -p /home/pi/.config/autostart
ln -f -s $DIR/etc/autostart/piday.desktop /home/pi/.config/autostart/piday.desktop

echo "schedule data uploads" 
crontab -u pi $DIR/etc/piday.cron
