
# Privilege Escalation via fail2ban
In Linux, fail2ban is mostly used to protect the SSH service. 
If the daemon detects several unsuccessful ssh login attempts, it executes a command that blocks the IP address.
So some misconfigurations can lead to privilege escalation.

![alt text](https://github.com/rvizx/fail2ban/img.png?raw=true)

# Usage
@victim
```
python3 fail2ban.py
```

@attacker - to create unsuccessful login attempts
```
hydra <ip-addr> -l root -P /usr/share/wordlist/rockyou.txt ssh
```

# Notes
https://youssef-ichioui.medium.com/abusing-fail2ban-misconfiguration-to-escalate-privileges-on-linux-826ad0cdafb7
https://grumpygeekwrites.wordpress.com/2021/01/29/privilege-escalation-via-fail2ban/

