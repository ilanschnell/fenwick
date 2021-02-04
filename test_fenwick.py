from random import randint
import unittest

from fenwick import Fenwick


class TestsFenwick(unittest.TestCase):

    def test_0(self):
        f = Fenwick(0)
        self.assertEqual(len(f), 0)
        self.assertEqual(f.values(), [])

    def test_n(self):
        for n in range(100):
            a = [randint(-100, 100) for _ in range(n)]
            f = Fenwick(n)
            for i, v in enumerate(a):
                f.add(i, v)
            self.assertEqual(f.values(), a)
            self.assertEqual([f[i] for i in range(n)], a)

    def test_random(self):
        for n in range(20):
            a = [randint(-100, 100) for _ in range(n)]
            f = Fenwick(a)
            self.assertEqual(f.values(), a)
            self.assertEqual([f[i] for i in range(n)], a)
            for _ in range(10 * n):
                i = randint(0, n - 1)
                if i > 0:
                    self.assertEqual(f.prefix_sum(i), sum(a[0:i]))
                j = randint(i, n - 1)
                self.assertEqual(f.range_sum(i, j), sum(a[i:j]))

if __name__ == '__main__':
    unittest.main()
