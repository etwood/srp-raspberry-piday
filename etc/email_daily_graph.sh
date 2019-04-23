rm /home/pi/srp/piday/output.png
rm /home/pi/srp/piday/email_body.txt
python /home/pi/srp/piday/generate_email.py >> /home/pi/srp/piday/email_body.txt

cat /home/pi/srp/piday/email_body.txt | mail -s "PiDay Plot" -a "/home/pi/srp/piday/output.png" pi
