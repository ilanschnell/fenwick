from fenwick import Fenwick

a = [2, 11, 4, -5, 6]

f = Fenwick(a)
print(f.values())

f.add(2, 3)  # like f[2] += 3 but faster
print(f.values())

f[1] = 15
a = f.values()
print(a)

print(f[3], a[3])
print(f.prefix_sum(3), sum(a[:3]))
print(f.range_sum(1, 3), sum(a[1:3]))
