# Creating a VM from a Custom Image

### Issues

None. Everything worked as expected.

### How to Create an Image

1. Install Azure CLI.
2. Run the deallocate command to stop the VM:

```bash
az vm deallocate --resource-group <resource-group-name> --name <vm-name>
```

3. Run the generalize command to prepare the VM for use as an image:

```bash
az vm generalize --resource-group <resource-group-name> --name <vm-name>
```

4. In the Azure portal, go to the VM resource.
5. Click on `Capture`.
6. Fill in the details and click `Review + create`.
7. Click `Create`.
8. Once the image is created, go to the resource.
9. Click on `Create VM`.
10. Fill in the details using this image and click `Review + create`.
11. Click `Create`.

### Process of Automating Deployment of an App

Firstly, we need to create a VM and SSH into it. Commands then need to be run manually before we automate anything so we can make sure the commands are working and that they are working without requiring user input. Once we know the commands are working, we can then automate the process using a script. The next stage of automation is to use user data to run the script when the VM is created so we no longer need to SSH into the VM to run the script. After this, we can use a custom image to create a VM with the script already run.

### User Data

User data is a script that runs when a VM is created. It can be used to automate the process of setting up a VM. It is a shell script that runs when the VM is created and can be used to install software, configure the VM, and more.
