
## Motivation

The first thing admins usually do after logging into an _off-the-shelf_ server is to secure it.

While there are a lot of advanced techniques and methods that can be used to improve the security of a new server and help keep it protected from various threats, this guide will only focus on the essentials.

## Assumptions

-   you have ssh access to a VPS (Debian/-based) from a GNU/Linux machine
-   basic terminal and nano editor knowledge
-   ~1 hour free time

## 1. Add new user

_Note: run `ssh root@server_ip` in a terminal if you are not connected. Replace server_ip with your VPS IP address._

To avoid using the root account on a regular basis, we need to first add a new user and grant it administrative privileges:

`adduser newuser` 

Enter a strong password and hit Enter to skip optional fields.

`usermod -aG sudo newuser`

## 2. Install firewall

Update and install a basic firewall via apt:

`apt update`

`apt install ufw`

Set default policies:

`ufw default deny incoming`

`ufw default allow outgoing`

Allow ssh connections and enable the firewall:

`ufw allow SSH`

Verify the status with:

`ufw status verbose`

Only proceed if the output includes this line:

```
To             Action      From
--             ------      ----
22/tcp (SSH)   ALLOW IN    Anywhere
```

Enable the firewall:

`ufw enable`

_Note: later you will probably need to adjust the firewall settings to allow traffic in from other services that you install; example for Nginx: `sudo ufw allow 'Nginx Full'`._

You can now close the connection to the server with `exit`.

## 3. Harden SSH

### 3.1 Client config

On your local machine, open the `ssh_config` file:

`sudo nano /etc/ssh/ssh_config`

Add or modify these li nes to allow public key authentication, disable IPv6 to reduce attack surface, and use the strongest cipher suites, message integrity codes, and key exchange algorithms available:

```
PubkeyAuthentication yes
AddressFamily inet
StrictHostKeyChecking ask
Ciphers chacha20-poly1305@openssh.com
MACs hmac-sha2-512-etm@openssh.com
KexAlgorithms curve25519-sha256
```

Save the file with `CTRL+X` > `Y` > press Enter.

### 3.2 Server config

Open two terminal tabs/windows and establish two separate SSH connections to the server, for backup purposes:

`ssh root@server_ip`

Restart the sshd daemon:

`systemctl restart sshd`

If both connections are still alive, try opening a third terminal window and test new connections:

`ssh root@server_ip`

Proceed if everything is working as expected.

In any terminal, make a backup of the original SSH configuration file with:

`cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup`

Now open the `sshd_config` file:

`nano /etc/ssh/sshd_config`

Add or modify these lines to enable SSH v2 for added protections against known vulnerabilities, disable IPv6, disallow root/pass logins, only allow logins from the user `newuser`, and use the strongest ciphers and algos available:

```
Protocol 2
AddressFamily inet
PermitRootLogin prohibit-password
PasswordAuthentication no
AllowUsers newuser
Ciphers chacha20-poly1305@openssh.com
MACs hmac-sha2-512-etm@openssh.com
KexAlgorithms curve25519-sha256
```

_Note: replace `newuser` with the actual username from step 1._

_Note: run `ssh -Q cipher`, `ssh -Q mac`, and `ssh -Q kex` for a list of supported ciphers and algorithms._

You can also change the default ssh daemon listen port from 22 to something else in an attempt to avoid open ports scans:

`Port 3489`

_Note: if you change the default ssh port, you need to update ufw rules; example: `ufw allow 3489`. Connect with `ssh newuser@server_ip -p 3489`._

Save the file with `CTRL+X` > `Y` > press Enter.

### 3.2 Test connection

Restart the sshd daemon:

`systemctl restart sshd`

Open another terminal tab/window and try to SSH to the server:

`ssh newuser@server_ip`

If it doesn’t work, check for configuration errors using the other terminal and then try again.

If successful, you will be able to ssh with `newuser` to the server from now on, and install any software you want.

## Observations

-   use strong and random passwords for system logins to protect against brute-force attacks
-   generate and use strong SSH keys protected by passphrases
-   update system regularly; you could automate the process with a _cron_ job
-   optionally install _Fail2Ban_ to monitor system logs and protect against DDoS attacks

That’s it for this basic server security guide. Reach out to me if you run into any trouble. Good luck!