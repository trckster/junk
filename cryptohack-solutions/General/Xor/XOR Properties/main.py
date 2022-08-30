from pwn import xor

key1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key2_xor_key_3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
encrypted_flag = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

flag = xor(key1, key2_xor_key_3, encrypted_flag)

print(flag)