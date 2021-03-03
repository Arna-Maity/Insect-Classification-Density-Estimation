sudo apt install build-essential python3-gpiozero libssl-dev libffi-dev python3-dev cargo python3-virtualenv
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo python3 reset.py
