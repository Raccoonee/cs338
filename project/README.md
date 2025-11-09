# 🌐 Personal VPN Hosting Project

## Overview
This project explores how to **set up, host, and operate a personal VPN server** using **OpenVPN**. The goal was to understand how VPN tunneling, encryption, and IP masking work by creating a fully functional VPN that users can connect to.

Initially, I planned to set up a local VPN server on my laptop, but after researching hosting options, I decided to host the VPN on **Linode**, a cloud hosting provider. This allowed for a more stable, scalable, and realistic environment similar to how VPN providers deploy their infrastructure.

---

## Project Objectives
- Learn how VPNs function at the network and encryption level.  
- Deploy and configure an **OpenVPN** server from scratch.  
- Allow remote users to connect and securely tunnel their internet traffic.  
- Demonstrate the VPN in action through a **demo video** showing IP changes and traffic encryption.  
- (Optional) Create a small website to explain how the VPN works and how to connect.

---

## Technologies Used
- **Hosting:** [Linode](https://www.linode.com/)
- **VPN Protocol:** OpenVPN
- **Operating System:** Linux (Ubuntu Server)
- **Networking Tools:** `iptables`, `curl`, `ip route`, and IP verification tools such as [whatismyipaddress.com](https://whatismyipaddress.com/)

---

## Setup & Access

> ⚠️ **Note:** This VPN server is for educational and demonstration purposes only.

### Guest Connection Details
You can connect to the VPN using the following temporary credentials:

**Server Link:** `https://172.239.55.184/login`  
**Username:** `guest`  
**Password:** `Guestuser1!`

---

## How It Works

When a user connects to the VPN:
1. Their internet traffic is encrypted by OpenVPN.
2. The traffic is routed through the VPN server hosted on Linode.
3. External websites see the **VPN server’s IP address**, not the client’s real one.
4. The demo video clearly shows the **change in IP address** before and after the VPN connection.

This setup helps illustrate:
- How VPN tunnels encapsulate traffic.
- The relationship between local, remote, and public IPs.
- The advantages of hosting VPNs on cloud infrastructure.

---

## Demo Video 🎥
A short video walkthrough demonstrates:
- Setting up the OpenVPN server on Linode.  
- Connecting to the VPN from a client machine.  
- Verifying the encrypted tunnel and new IP address.  

**Watch the demo here:** `https://youtu.be/UCidO5g1VLA`

---

## Reflections
- Hosting on Linode proved to be a more stable and realistic approach than hosting locally.  
- OpenVPN offered strong documentation and easier setup compared to WireGuard for this use case.  
- Understanding routing tables and IP forwarding was key to getting traffic to pass through the VPN correctly.  
- The project deepened my understanding of **network security, encryption, and infrastructure deployment**.

---

## Legal & Security Considerations
- This project is strictly for **educational use**.  
- Users should avoid using the VPN for any unauthorized or malicious activity.  
- Always review your host’s **Terms of Service** and **data privacy policies** when deploying network services.

---

## Credits

Credits to Jeff Ondich for recommending the hosting service.  

---

## License
This project is released under the **MIT License** for educational use.  
Feel free to fork, modify, and learn from it — but please credit the original author.

---

