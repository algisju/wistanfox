#!/usr/bin/env python
from scapy.all import *
ap_list = []
localiface="wlan0"

def PacketHandler(pkt) :
  if pkt.haslayer(Dot11) :
    if pkt.type == 0 and pkt.subtype == 8 :
      if pkt.addr2 not in ap_list :
        ap_list.append(pkt.addr2)
        print("AP MAC: %s with SSID: %s " %(pkt.addr2, pkt.info))

print("\033c")
print("[+] Sniffing on "+localiface)
sniff(iface=localiface, prn = PacketHandler)
