# Linking the App VM to the Database VM

## [Database VM](#database-vm)

### Create a VM

-   Make sure that the VM is in the same virtual network as the app VM and uses the private subnet as opposed to the public subnet which is used for the app VM.
-   Allow SSH connections (No need for HTTP or HTTPS as we won't be accessing the database from the internet).

### Install MongoDB

1. `sudo apt-get update`: Updates the package lists for upgrades to make sure you have the latest version of the packages.
2. `sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y`: Upgrades all the currently installed packages on the system to their latest versions in a non-interactive shell so that it can be run in a script without user interaction.
3. `sudo apt-get install gnupg curl`: Installs `gnupg` and `curl`, which are both needed for the next steps.
4. `curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor`: Downloads the MongoDB GPG key.
5. `echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list`: Adds the MongoDB repository to the system's package sources.
6. `sudo apt-get update -y`
7. `sudo apt-get install -y mongodb-org=7.0.6 mongodb-org-database=7.0.6 mongodb-org-server=7.0.6 mongodb-mongosh=2.1.5 mongodb-org-mongos=7.0.6 mongodb-org-tools=7.0.6`: Installs the MongoDB packages.
8. `sudo nano /etc/mongod.conf`: Opens the MongoDB configuration file for editing so we can change the `bindIp` to `0.0.0.0` to allow connections from any IP address.
9. `sudo systemctl enable mongod`: Enables the MongoDB service so it starts automatically at boot.
10. `sudo systemctl start mongod`: Starts the MongoDB service.
11. `sudo systemctl status mongod`: Checks the status of the MongoDB service.

## App VM

### Configuring the Database Host Environment Variable

1. `export DB_HOST="mongodb://10.0.3.4:27017/posts"`: Temporarily sets the `DB_HOST` environment variable to the MongoDB connection string with its default port. The private IP of the [Database VM](#database-vm) This environment variable is set for the current session only.
2. For a persistent environment variable: `echo 'export DB_HOST="mongodb://10.0.3.4:27017/posts"' >> ~/.bashrc` appends the `DB_HOST` variable export command to `~/.bashrc`, ensuring it's set every time a new shell session starts for the current user.
3. `source ~/.bashrc`: Reloads the `.bashrc` file to apply the changes immediately.
4. `echo $DB_HOST`: Displays the current value of the `DB_HOST` variable to verify it's set correctly.

### App Setup

1. `sudo -E npm install`: Installs Node.js dependencies, preserving the user's environment variables. The `-E` flag ensures `sudo` runs with the current user's environment, important for using the correct `DB_HOST`.
2. `sudo -E npm start`: Starts the Node.js application, preserving the user's environment variables.
