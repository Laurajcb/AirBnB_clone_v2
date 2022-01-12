#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

sudo apt-get update -y
sudo apt-get install nginix -y 
ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
