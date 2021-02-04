from fenwick import Fenwick

a = [2, 11, 4, -5]

f = Fenwick(a)
print(f.values())
f.add(2, 3)
print(f.values())
f[1] = 15
print(f.values())
print(f[3])
print(f.prefix_sum(3))
print(f.range_sum(1, 3))
