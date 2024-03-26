#!/bin/bash

echo "Running apt update..."
sudo apt update -y
echo "Running apt upgrade..."
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

echo "Installing nginx..."
sudo apt install nginx -y
echo "Installed nginx successfully!"

echo "Adding reverse proxy to nginx config..."
sudo sed -i "s|try_files .*;|proxy_pass http://127.0.0.1:3000;|g" /etc/nginx/sites-available/default
echo "Added reverse proxy successfully!"

echo "Restarting and enabling nginx..."
sudo systemctl restart nginx
sudo systemctl enable nginx

echo "Installing node.js 20..."
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt-get install -y nodejs

echo "Installing git..."
sudo apt install git -y

cd /

echo "Cloning repo..."
git clone https://github.com/developedbyluke/tech257-sparta-app.git repo

echo "Moving app folder out of repo and deleting empty repo folder..."
mv tech257-sparta-app/app ./
rm -rf tech257-sparta-app

echo "Moving into app folder..."
cd app

echo "Running npm install..."
npm install

# echo "Running npm start..."
# npm start

echo "Installing pm2..."
sudo npm install pm2 -g

echo "Starting app.js with pm2..."
pm2 start app.js
