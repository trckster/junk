from Crypto.Hash import SHA256

hashing = SHA256.new()

hashing.update(b'test')

print(hashing.hexdigest())
