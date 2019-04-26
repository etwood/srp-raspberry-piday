#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

date
cd /home/pi/srp/piday 
git pull origin master

# update cron tab
crontab $DIR/piday.cron


