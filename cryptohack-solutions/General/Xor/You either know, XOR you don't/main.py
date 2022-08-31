from pwn import xor

data = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
flag_start = 'crypto{'
secret = ''

for i in range(len(flag_start)):
    c = flag_start[i]
    secret += chr(ord(c) ^ data[i])

secret += 'y'

print(xor(data, secret))
