from pwn import *  # pip install pwntools
import json
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377)


def json_recv():
    line = r.recvline()
    print(line)
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:
    received = json_recv()

    if 'flag' in received:
        print(received['flag'])
        exit(0)

    type = received['type']
    message = received['encoded']

    answer = None
    if type == 'base64':
        answer = base64.b64decode(message).decode('utf-8')
    elif type == 'hex':
        answer = bytes.fromhex(message).decode('utf-8')
    elif type == 'rot13':
        answer = codecs.decode(message, 'rot-13')
    elif type == 'bigint':
        answer = bytes.fromhex(long_to_bytes(int(message, 16)).hex()).decode('utf-8')
    elif type == 'utf-8':
        answer = ''
        for c in message:
            answer += chr(c)

    to_send = {
        "decoded": answer
    }

    print(to_send)
    json_send(to_send)
