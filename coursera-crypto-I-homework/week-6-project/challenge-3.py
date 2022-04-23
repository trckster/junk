import gmpy2

N = 720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929

n24 = 4 * 6 * N

A = gmpy2.isqrt(n24 - 1) + 1

# We are brute-forcing A (which is equal to 3p + 2q)
# and trying to solve this equation as quadratic, because:
#
# 3p + 2q = A               | q == N / p
# 3p + 2(N/p) = A           | *p
# 3(p ** 2) + 2N = Ap
# 3(p ** 2) - Ap + 2N = 0
# Here we have simple quadratic equation and our goal is to solve it for each A
# until we find suitable (s.t. N % x == 0) roots of this equation!
#
# UPD: In fact, it turns out, that sqrt(6N) is VERY near (3p + 2q) / 2, so there is no need to bruteforce A,
# initial value suits (cycle is excess)

a = 3
c = 2 * N

while True:
    b = -A

    s = gmpy2.isqrt(b ** 2 - 4 * a * c)
    x1 = (-b + s) // (2 * a)
    x2 = (-b - s) // (2 * a)

    if N % x1 == 0:
        print(min(x1, N // x1))
        break

    if N % x2 == 0:
        print(min(x2, N // x2))
        break

    A += 1
