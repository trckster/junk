import gmpy2

N = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581
M = 22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540
E = 65537

A = gmpy2.isqrt(N) + 1

x = gmpy2.isqrt(abs(A ** 2 - N))
p = A - x
q = A + x

φ = (p - 1) * (q - 1)

d = pow(E, -1, φ)

message = hex(pow(M, d, N))

data_start = message.find('00') + 2

data = message[data_start:]
print(bytes.fromhex(data).decode('ASCII'))
