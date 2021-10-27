#!/usr/bin/env python3
from scapy.all import *
def PacketHandler(pkt) :
  if pkt.haslayer(Dot11) :
    if pkt.type == 0 and pkt.subtype == 4 :
      if pkt.info :
        print("Client: %s with SSID: %s " %(pkt.addr2, pkt.info))

#print("\033c")
print("[+] Sniffing on "+"whatever")
sniff(iface="wlan0", prn = PacketHandler)
