---
- name: Deploy app
  hosts: agents
  become: yes
  gather_facts: yes

  tasks:
    - name: Install node.js
      shell: curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt-get install -y nodejs

    - name: Install pm2
      npm:
       name: pm2
       global: yes

    - name: Install Git
      apt:
        name: git

    - name: Clone Git repo
      shell: git clone https://github.com/developedbyluke/tech257-ci-cd.git /temp/repo

    - name: Move app folder out of cloned repo
      shell: |
        mv /temp/repo/app /
        rm -rf /temp/repo

    - name: Start app
      shell: |
        cd /app
        npm install
        pm2 kill
        pm2 start app.js