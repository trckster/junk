# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
a = [2, 3, 5]
n = [5, 11, 17]


def get_inverse(num, p):
    for i in range(p):
        if (num * i) % p == 1:
            return i

    return None


N = 1
for number in n:
    N *= number

Ni = [N // number for number in n]

xi = [get_inverse(_Ni, _n) for _Ni, _n in zip(Ni, n)]

multiplications = [_a * _Ni * _xi for _a, _Ni, _xi in zip(a, Ni, xi)]

print(sum(multiplications) % N)
