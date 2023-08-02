# git
git status 
git push origin master
git pull origin master
# to push
git add .
git commit -m "agu 1, 2023; groups added"
git push
git pull
# on server
git clone https://github.com/username/repo.git

git pull origin branch_name 
# or
git pull origin master

# env
source env/bin/activate
deactivate
# for turn serveron 
ssh -i "key.ssh" ubuntu@172-31-33-161
# server atablish
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
mkdir ~/myprojectdir
cd ~/myprojectdir
virtualenv myprojectenv
source myprojectenv/bin/activate
pip install django gunicorn psycopg2-binary
# django setting or testing
django-admin startproject myproject ~/myprojectdir #if we start to test
nano ~/myprojectdir/myproject/settings.py # to allow host ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . ., 'localhost']
~/myprojectdir/manage.py makemigrations
~/myprojectdir/manage.py migrate
~/myprojectdir/manage.py createsuperuser
~/myprojectdir/manage.py collectstatic
sudo ufw allow 8000
~/myprojectdir/manage.py runserver 0.0.0.0:8000
cd ~/myprojectdir
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
deactivate
# for postger db in ubuntu
sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
sudo systemctl status postgresql
sudo systemctl start postgresql
sudo systemctl enable postgresql
#gunicorn and nginx settings
sudo nano /etc/systemd/system/gunicorn.socket
# socket file
'''[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
'''
# service file
sudo nano /etc/systemd/system/gunicorn.service
'''
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myprojectdir
ExecStart=/home/sammy/myprojectdir/myprojectenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          myproject.wsgi:application

[Install]
WantedBy=multi-user.target
'''
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock
sudo journalctl -u gunicorn.socket
sudo systemctl status gunicorn
curl --unix-socket /run/gunicorn.sock localhost
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nano /etc/nginx/sites-available/myproject
# nginx file:
'''
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myprojectdir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
'''
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
sudo tail -F /var/log/nginx/error.log
namei -l /run/gunicorn.sock
sudo systemctl restart gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
sudo nginx -t && sudo systemctl restart nginx

# comon sh

sudo systemctl daemon-reload

sudo systemctl start gunicorn.socket

sudo systemctl enable gunicorn.socket

sudo systemctl status gunicorn
sudo systemctl status gunicorn.socket

sudo systemctl restart nginx
sudo systemctl restart gunicorn