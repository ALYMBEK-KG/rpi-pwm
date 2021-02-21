sudo apt update
sudo apt install python3-pip
sudo pip3 install RPi.GPIO
sudo cp fancontrol.py /usr/local/bin/
sudo chmod +x /usr/local/bin/fancontrol.py
sudo cp fancontrol.sh /etc/init.d/
sudo chmod +x /etc/init.d/fancontrol.sh
sudo update-rc.d fancontrol.sh defaults
