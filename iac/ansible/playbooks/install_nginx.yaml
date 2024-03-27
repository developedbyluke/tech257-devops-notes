---
- name: Install and configure nginx
  hosts: agents
  gather_facts: yes
  become: yes

  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Configure reverse proxy
      shell: |
        sed -i "s|try_files .*;|proxy_pass http://127.0.0.1:3000;|g" /etc/nginx/sites-available/default
        systemctl restart nginx
        systemctl enable nginx
