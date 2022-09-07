from Crypto.PublicKey import RSA

key = RSA.importKey(open('rsa.pem', 'r').read())

print(key.n)
