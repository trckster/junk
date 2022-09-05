from Crypto.PublicKey import RSA

key = RSA.importKey(open('private-key.pem', 'r').read())

print(key.d)