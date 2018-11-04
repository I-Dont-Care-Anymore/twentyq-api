sudo su -c 'cd /home/ubuntu/twentyq-api && source .env/bin/activate && gunicorn main:app --bind 0.0.0.0:80'
