# Scripting and Automation

## Creating and Running a Provisioning Script for Nginx

To automate the installation and configuration of Nginx on a Linux system, you can create a shell script. Here's an example script that installs Nginx, starts the service, and enables it to run at boot:

```bash
#!/bin/bash

# Update the package list
sudo apt update

# Install Nginx
sudo apt install nginx -y

# Restart the Nginx service
sudo systemctl restart nginx

# Enable Nginx to start on boot
sudo systemctl enable nginx

echo "Nginx installation and setup completed."
```

Save this script to a file, for example, `install_nginx.sh`, and make it executable with the command `chmod +x install_nginx.sh`. Run the script using `./install_nginx.sh`.

## Variables in Shell Scripts

1. **Creating a Variable** : Assign a value to a variable with `variable_name=value`. Do not add spaces around the `=` sign. For example, `greeting="Hello, World!"`.
2. **Using a Variable** : Reference the variable with `$variable_name`. For example, `echo $greeting` would print "Hello, World!".
3. **Persisting Variables** : To make variables persistent across sessions and VM restarts, add them to `~/.bashrc`.

```bash
echo 'export greeting="Hello, World!"' >> ~/.bashrc
source ~/.bashrc
```
