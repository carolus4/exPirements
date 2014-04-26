import sys

from scapy.all import *

PROBE_REQ_TYPE = 0
PROBE_REQ_SUBTYPE = 4

unique_ssids = []

def PacketHandler(pkt) :

        if pkt.haslayer(Dot11):
                # check if Beacon frame
        
                if pkt.type == PROBE_REQ_TYPE and pkt.subtype == PROBE_REQ_SUBTYPE :
                        # null probe removal 
                        if pkt.info not in unique_ssids:
                                unique_ssids.append(pkt.info)
                                print "New probed SSID: %s" % ( pkt.info)

sniff(iface=sys.argv[1], count=int(sys.argv[2]), prn=PacketHandler)
