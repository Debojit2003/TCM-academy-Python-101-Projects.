from pwn import *
print(cyclic(50))
print(cyclic_find('laaa'))
print(shellcraft.sh())
print(hexdump(asm(shellcraft.sh())))
#p = process("/bin/sh") 
#p.sendline('echo hello;')
#p.interactive()
# for local process
#For remote process use the below section code
# For accessing remote connection use command nc -lp [port no.]
#r = remote('127.0.0.1',1234)
#r.sendline("Hello! You are connected.")
#r.interactive()
#r.close()
#"-----------------------------"
# for packing and unpacking numbers.
print(p32(0x13371337)) #p32 = used for packing
print(hex(u32(p32(0x13371337)))) #u32 = used for unpacking.

l = ELF('/bin/bash')
print(hex(l.address)) #address
print(hex(l.entry)) #entry point
print(hex(l.got['write']))
print(hex(l.plt['write']))


for address in l.search(b'/bin/sh\x00'):
	print(hex(address))

print(hex(next(l.search(asm('jmp esp'))))) #location of jmp esp in /bin/bash
r = ROP(l)
print(r.rbx)

print(xor(xor("A","B"),"A"))
print(b64e(b"test")) #encoding base64
print(b64d(b"dGVzdA==")) #decoding base64
print(md5sumhex(b"password"))
print(sha1sumhex(b"password"))
print(bits(b'a'))
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))


