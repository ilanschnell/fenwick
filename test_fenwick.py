from random import randint
from pprint import pprint

from fenwick import Fenwick

N = 15
a = [randint(-N, N) for _ in range(N)]
sm = 0
s = []
for i in range(N):
    sm += a[i]
    s.append(sm)
pprint(s)

f = Fenwick(N)
pprint(f.values())
for i, v in enumerate(a):
    f.add(i, v)
pprint([f.prefix_sum(i + 1) for i in range(N)])
pprint(a)
pprint([f[i] for i in range(N)])
pprint(f.values())

f = Fenwick(a)
pprint([f[i] for i in range(N)])
pprint(a)

for _ in range(1000):
    i = randint(0, N - 1)
    j = randint(i, N - 1)
    #print(i, j)
    assert f.range_sum(i, j) == sum(a[i:j])
