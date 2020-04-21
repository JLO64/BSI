#!/bin/bash

sudo apt update
sudo apt install git -y
sudo apt install python3-pip -y
sudo pip3 install boto3

text="#!/bin/bash \n\npython3 /usr/lib/BSI-Manager/BSI_Manager.py"
echo -e "${text}" > BSI_Manager
sudo chmod +x BSI_Manager
sudo rm -rf /bin/BSI_Manager
sudo mv BSI_Manager /bin/BSI_Manager

cd /usr/lib
sudo rm -rf /usr/lib/BSI-Manager
sudo git clone https://github.com/JLO64/BSI-Manager.git

echo -e \n\n"In a terminal type BSI_Manager"