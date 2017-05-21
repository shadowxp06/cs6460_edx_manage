#!/usr/bin/env bash
#
#Last Updated: 04/21/2017 3:09 PM/EST

#http://stackoverflow.com/questions/19306771/get-current-users-username-in-bash
#http://stackoverflow.com/questions/20551566/display-current-date-and-time-without-punctuation
currentuser=$(whoami)
current_date_time="`date "+%Y-%m-%d %H:%M:%S"`";

iptables -F
iptables -A INPUT -s 127.0.0.1 -j ACCEPT
iptables -A INPUT -s 130.207.114.239 -j ACCEPT

##SSH Rules to prevent Bruteforce attacks -- See https://wiki.centos.org/HowTos/Network/SecuringSSH#head-b726dd17be7e9657f8cae037c6ea70c1a032ca$
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set --name ssh --rsource
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent ! --rcheck --seconds 60 --hitcount 4 --name ssh --rsource -j ACCEPT

## deny rules
iptables -A INPUT -p tcp --destination-port 25 -j DROP #OpenEdX / SMTP
iptables -A INPUT -p tcp --destination-port 3306 -j DROP #MySQL
#iptables -A INPUT -p tcp --destination-port 18010 -j DROP #Studio
iptables -A INPUT -p tcp --dport 27017:27018 -j DROP #MongoDB
iptables -A INPUT -p tcp --destination-port 45172 -j DROP #MongoDB Administration Port - Custom
iptables -A INPUT -p tcp --dport 9002:9003 -j DROP #ElasticSearch
iptables -A INPUT -p tcp --match multiport --dports 18090,18130,8099,18080,18040 -j DROP #Various Open EdX ports
iptables -A INPUT -s masscan.security.gatech.edu -j DROP
iptables -A INPUT -s havarti.cc.gatech.edu -j DROP


## Sources ##
#https://www.cyberciti.biz/tips/linux-iptables-how-to-specify-a-range-of-ip-addresses-or-ports.html (03/03/2017)



echo "($current_date_time) $currentuser ran the firewall rules" >> /gt/logs/system.log