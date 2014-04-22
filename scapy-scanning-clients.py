#!/usr/bin/env python
from scapy.all import *
import sys
import datetime

# Define the interface name that we will be sniffing from
interface = "mon0"

observedclients = []

# The sniffmgmt() function is called each time Scapy receives a packet
# The packet that was sniffed is passed as the function argument, "p".
def sniffmgmt(p):
    timestamp = str(datetime.datetime.now())

    # Define our tuple (an immutable list) of the 3 management frame
    # subtypes sent exclusively by clients. I got this list from Wireshark.
    stamgmtstypes = (0, 2, 4)

    # Make sure the packet has the Scapy Dot11 layer present
    if p.haslayer(Dot11):

        # Check to make sure this is a management frame (type=0) and that
        # the subtype is one of our management frame subtypes indicating a
        # a wireless client
        if p.type == 0 and p.subtype in stamgmtstypes:

            # We only want to print the MAC address of the client if it
            # hasn't already been observed. Check our list and if the
            # client address isn't present, print the address and then add
            # it to our list.
            if p.addr2 not in observedclients:
                sys.stdout.write( "pi1" + "," + timestamp + "," + p.addr2)
                observedclients.append(p.addr2)

# With the sniffmgmt() function complete, we can invoke the Scapy sniff()
# function, pointing to the monitor mode interface, and telling Scapy to call
# the sniffmgmt() function for each packet received. Easy!
sniff(iface=interface, prn=sniffmgmt)
