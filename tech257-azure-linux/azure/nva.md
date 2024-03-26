Network Virtual Appliance Virtual Machine

Filter and forward packets/traffic between virtual machines.

Steps

1. Create VNet with three subnets, public, private, and DMZ
2. Create DB VM
3. Create App VM
4. Create NVA VM
5. Ping from App VM to DB VM to check connectivity
6. Set up route table to route traffic from App VM to DB VM through NVA VM
7. Enable IP forwarding on NVA VM
