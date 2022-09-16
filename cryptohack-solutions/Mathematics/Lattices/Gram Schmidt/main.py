def dot(v1, v2):
    res = 0

    for a, b in zip(v1, v2):
        res += a * b

    return res


def size(v):
    from math import sqrt

    return sqrt(dot(v, v))


def sub(v1, v2):
    return [a - b for a, b in zip(v1, v2)]


def mult(v, n):
    return [n * x for x in v]


def get_projection(v, u):
    n = dot(v, u) / dot(u, u)

    return mult(u, n)


def get_unit(u):
    return [x * size(u) / abs(dot(u, u)) for x in u]


def main():
    v = [[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]]

    u = []

    for i in range(len(v)):
        ui = v[i]
        j = i
        while j > 0:
            j -= 1
            ui = sub(ui, get_projection(v[i], u[j]))

        u.append(ui)

    print(round(u[3][1], 5))


main()
