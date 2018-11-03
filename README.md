
## Usage

### Linux

```bash
sudo apt-get install python3 python3-pip python3-virtualenv virtualenv
virtualenv .env --python=python3
source .env/bin/activate
pip3 install -r requirements.txt
python3 api.py
```

### Windows

Run in an administrator powershell:

```powershell
Set-ExecutionPolicy AllSigned
```

This one doesn't need to be admin

```powershell
virtualenv .\env --python=python3
.\env/bin/activate
pip3 install -r requirements.txt
python3 api.py
```

![spongebob](spongebob.jpg)
