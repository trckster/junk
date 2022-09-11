def get_quadratic_root(n, m):
    for i in range(m):
        if (i ** 2) % m == n:
            return i

    return None


for x in [14, 6, 11]:
    qr = get_quadratic_root(x, 29)

    if qr is not None:
        print(qr)
