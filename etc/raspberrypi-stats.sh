#!/bin/bash

date=`date`
temp=`vcgencmd measure_temp`
volts=`vcgencmd measure_volts core`
clock_freq=`vcgencmd measure_clock arm`
wifi_info=`/sbin/iwconfig wlan0`
echo "$date $temp $volts $clock_freq $wifi_info"


