# Using a VM to Deploy an App

### Commands to run once you SSH into the VM

1. `sudo apt update -y`
2. `sudo apt upgrade -y`
3. `sudo apt install nginx -y`
4. `sudo systemctl restart nginx`
5. `sudo systemctl enable nginx`
6. `curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - &&\ sudo apt-get install -y nodejs`

### Transfer files to the VM

#### Method 1: Using SCP

```bash
scp -i /c/Users/username/.ssh/private_key -r /c/Users/username/Downloads/app username@public-ip:/path/to/save
```

#### Method 2: Using GitHub

1. Create a new repository on GitHub.
2. Push the app to the repository.
3. SSH into the VM.
4. Run the following commands:

```bash
sudo apt install git -y
git clone https://github.com/developedbyluke/sparta-test-app.git
mv sparta-test-app/app .
rm -rf sparta-test-app
```

### Run the app

```bash
cd app
npm install
npm start
```

### Access the app

Go to `http://public-ip:3000` in a web browser.

### Automating the Deployment

```bash
#!/bin/bash

echo "Running apt update..."
sudo apt update -y
echo "Running apt upgrade..."
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -yq

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
echo "Cloning repo..."
git clone https://github.com/developedbyluke/tech257-sparta-app.git

echo "Moving app folder out of repo and deleting empty repo folder..."
mv tech257-sparta-app/app ./
rm -rf tech257-sparta-app

echo "Moving into app folder..."
cd app

# echo "Running npm install..."
# npm install
# echo "Running npm start..."
# npm start

echo "Installing pm2..."
sudo npm install pm2 -g

echo "Starting app.js with pm2..."
pm2 start app.js
```
