from Crypto.Hash import SHA256

test_hash = '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8'


def get_first_block_hash(filename):
    blocks = []
    with open(filename, 'rb') as f:
        data = f.read(1024)
        while data:
            blocks.append(data)
            data = f.read(1024)

    i = len(blocks) - 1
    while i >= 0:
        hashing = SHA256.new()

        hashing.update(blocks[i])

        if not i:
            return hashing.hexdigest()

        blocks[i - 1] += hashing.digest()

        i -= 1


if get_first_block_hash('test') == test_hash:
    print('Test hash computed successfully')
else:
    print('Test hash computed incorrectly')

print('Task hash: %s' % get_first_block_hash('video'))
