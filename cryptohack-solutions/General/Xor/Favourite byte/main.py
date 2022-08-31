from pwn import xor

data = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

number = data[0] ^ ord('c')

print(xor(data, number))