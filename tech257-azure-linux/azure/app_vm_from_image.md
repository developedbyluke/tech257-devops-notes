# Deploying an App with User Data

### Pre-requisites

-   An image with:
    -   dependencies installed (git, node.js, npm, nginx, pm2)
    -   a cloned app repo in the root directory
    -   a reverse proxy in the nginx config

### Creating the VM instance

Navigate to the image and create a new VM from it or create a VM elsewhere and select the image in the image field.

![](..images/vm-image.png "Selecting the image for the VM")

In the 'Advanced' tab, enable 'User Data' and provide the user data needed to start the app from the VM.

![](..images/minimal-user-data.png "User data needed to start the app")

In this script, we simply `cd` into the app directory and run `pm2 start app.js` to start the app in the background.

```bash
#!/bin/bash

cd repo/app

pm2 stop app.js

pm2 start app.js
```

### Accessing the App

Now the app is running and you should be able to access it from the public IP of the VM without needing to specify a port.

![](./..images/website.png "App running on public IP")

### Blockers Encountered

The public IP of the app was not accessible at first. This was because I forgot to add the shabang at the top of the user data script. Once I added `#!/bin/bash` at the top of the script, the app was accessible.
