#### Enable I2C channel on Rpi running Ubuntu 20 
```
wget https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20160527_all.deb -P /tmp
sudo apt-get install libnewt0.52 whiptail parted triggerhappy lua5.1 alsa-utils -y
sudo apt-get install -fy
sudo dpkg -i /tmp/raspi-config_20160527_all.deb
sudo mount /dev/mmcblk0p1 /boot
sudo apt-get install i2c-tools

ls /dev/i2c*
sudo i2cdetect -y 1
```
[stack overflow link](https://askubuntu.com/questions/1130052/enable-i2c-on-raspberry-pi-ubuntu)