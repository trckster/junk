p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

# Honestly stolen from https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


##########

# Our goal is to find x s.t. h = g ** x (mod p)

B = 2 ** 20

rainbow = {}

left = 1
for i in range(B):
    print(i)
    rainbow[(h * modinv(left, p)) % p] = i
    left *= g
    left %= p

for i in range(B):
    print(i)
    right = pow(g, B * i, p)
    if right in rainbow:
        j = rainbow[right]
        print('Found', j + i * B)
        exit()
