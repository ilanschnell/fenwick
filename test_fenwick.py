from random import randint
import unittest

from fenwick import Fenwick


class TestsFenwick(unittest.TestCase):

    def test_init_0(self):
        f = Fenwick(0)
        self.assertEqual(len(f), 0)
        self.assertEqual(f.values(), [])

    def test_1(self):
        N = 15
        a = [randint(-N, N) for _ in range(N)]
        sm = 0
        s = []
        for i in range(N):
            sm += a[i]
            s.append(sm)
        f = Fenwick(N)
        for i, v in enumerate(a):
            f.add(i, v)
        self.assertEqual([f.prefix_sum(i + 1) for i in range(N)], s)
        self.assertEqual(f.values(), a)

    def test_2(self):
        for n in range(20):
            a = [randint(-100, 100) for _ in range(n)]
            f = Fenwick(a)
            self.assertEqual([f[i] for i in range(n)], a)
            for _ in range(10 * n):
                i = randint(0, n - 1)
                j = randint(i, n - 1)
                self.assertEqual(f.range_sum(i, j), sum(a[i:j]))

if __name__ == '__main__':
    unittest.main()
