from scapy.all import *

# this script will send 2000 packets of net id to specified server
# INPUT: netid, IP
# 192.168.100.196
# port 31337

for i in range(2000):
    send(IP(dst='192.168.100.196')/TCP(sport=33, dport=31337)/"ppng2")
