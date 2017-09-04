#!/usr/bin/python

import struct, socket

def WakeOnLan(ethernet_address):

  # Construct a six-byte hardware address

  addr_byte = ethernet_address.split(':')
  hw_addr = struct.pack(b'BBBBBB', int(addr_byte[0], 16),
    int(addr_byte[1], 16),
    int(addr_byte[2], 16),
    int(addr_byte[3], 16),
    int(addr_byte[4], 16),
    int(addr_byte[5], 16))

  # Build the Wake-On-LAN "Magic Packet"...

  msg = b'\xff' * 6 + hw_addr * 16

  # ...and send it to the broadcast address using UDP

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  s.sendto(msg, ('', 9))
  s.close()

# Example use
WakeOnLan('70:5a:0f:29:39:2b')
