# Raspberry Pi Day 

to run:
```bash
python ./piday.py
```

Inspired by https://medium.com/@jdc_cunningham/how-to-connect-a-solar-panel-to-a-raspberry-pi-3fc15b7943ba
=======
# Raspberry pi data collection
For the SRP 2019 PiDay

```
sudo ./install.sh
echo yourusername > username
aws configure
  <enter in your access key>
  <enter in your secret key>
  region: us-west-1
  hit enter for the default output format

```


Your data will get written to /home/pi/srp/piday/output.csv and then once a day get moved into data-to-upload/data/ where it gets uploaded to Amazon.


inspired by: https://medium.com/@jdc_cunningham/how-to-connect-a-solar-panel-to-a-raspberry-pi-3fc15b7943ba
