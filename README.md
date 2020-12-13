# potoo2

Quick and dirty developments with django admin :
* Allows to generate a configuration file from a template for some PSTN to VoIP gateway

## install
```
apt-get install python3-venv
git clone https://github.com/benasse/potoo2.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations gwconf
python3 manage.py migrate
python3 manage.py loaddata fixtures/*.yaml
python3 manage.py createsuperuser
```

## run
```
python3 manage.py runserver 0:8000
```
