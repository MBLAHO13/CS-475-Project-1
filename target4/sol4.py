#!/usr/bin/env python2

from struct import pack

# Padding goes here
p = ""

p += pack('<I', 0x80);

#p += pack('<I', 0x0805dcaa) # pop edx ; ret

print p
