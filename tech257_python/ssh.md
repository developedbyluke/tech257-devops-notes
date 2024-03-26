# SSH and GitHub

### What is SSH?

- Secure Shell (SSH) is a protocol that enables securely sending commands to a
  computer over an unsecured network.
- Uses asymmetric cryptography
- Often used for:
    - controlling servers remotely
    - managing infrastructure
    - transferring files

### Why use it over HTTPS?

- Strong encryption and more comprehensive security features
- Automation and Configuration Management: SSH is used to execute commands and scripts on remote servers securely

### Generating SSH key pairs

**Generate with keygen command**

`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

- `-b 4096`: Specifies the number of bits in the key.
- `-C`: Adds a label to the key.

**Start SSH Agent**

```
ssh-agent -s
```

**Add SSH Key to SSH Agent**

```
ssh-add ~/.ssh/id_rsa
```

**Copy the SSH Public Key**: You need to copy your public key to the clipboard. You can display the content of your public key file with `cat` and then copy it:

`cat ~/.ssh/id_rsa.pub`

**Add the SSH Key to GitHub**:

Go to the SSH keys section and add the public key.

### Important

Never disclose your private SSH keys.
