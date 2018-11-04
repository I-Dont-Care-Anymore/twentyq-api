#!/bin/sh
cd ~
sudo apt-get update
sudo apt-get install -y python3 python3-virtualenv virtualenv python3-pip gunicorn
git clone https://github.com/I-Dont-Care-Anymore/twentyq-api
cd twentyq-api
virtualenv --python=python3 .env
source .env/bin/activate
pip3 install -r requirements.txt
pip3 install gunicorn
python3 -m spacy download en_core_web_lg
