sudo su -c 'cd /home/ubuntu/twentyq-api && source .env/bin/activate && gunicorn main:app --bind 0.0.0.0:443 --keyfile /etc/letsencrypt/live/api.twentyq.com/privkey.pem --certfile /etc/letsencrypt/live/api.twentyq.com/cert.pem --ca-certs /etc/letsencrypt/live/api.twentyq.com/chain.pem --timeout 600'
