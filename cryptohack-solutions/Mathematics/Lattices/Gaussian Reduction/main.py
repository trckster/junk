def dot(v, u):
    res = 0

    for a, b in zip(v, u):
        res += a * b

    return res


def size(v):
    from math import sqrt

    return sqrt(dot(v, v))


def mult(v, n):
    return [n * x for x in v]


def sub(v, u):
    return [a - b for a, b in zip(v, u)]


v1 = [846835985, 9834798552]
v2 = [87502093, 123094980]

while True:
    if size(v1) > size(v2):
        v1, v2 = v2, v1

    m = round(dot(v1, v2) / dot(v1, v1))
    if m == 0:
        break

    v2 = sub(v2, mult(v1, m))

print(dot(v1, v2))
