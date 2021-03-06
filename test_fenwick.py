import array
import math
import random
import unittest

from fenwick import Fenwick


class TestsFenwick(unittest.TestCase):

    def test_0(self):
        f = Fenwick(0)
        self.assertEqual(len(f), 0)
        self.assertEqual(f.values(), [])

    def test_n(self):
        for n in range(100):
            a = [random.randint(-100, 100) for _ in range(n)]
            f = Fenwick(n)
            for i, v in enumerate(a):  # O(n * log n)
                f.add(i, v)
            b = f.values()
            self.assertEqual(b, a)
            self.assertIsInstance(b, list)
            self.assertEqual([f[i] for i in range(n)], a)

    def test_randint(self):
        for n in range(20):
            a = [random.randint(-100, 100) for _ in range(n)]
            f = Fenwick(a)
            self.assertEqual(f.values(), a)
            self.assertEqual([f[i] for i in range(n)], a)
            for _ in range(10 * n):
                i = random.randint(0, n - 1)
                if i > 0:
                    self.assertEqual(f.prefix_sum(i), sum(a[0:i]))
                j = random.randint(i, n - 1)
                self.assertEqual(f.range_sum(i, j), sum(a[i:j]))

    def test_random(self):
        N = 1000
        a = [random.random() for _ in range(N)]
        f = Fenwick(a)
        self.assertTrue(math.isclose(f.prefix_sum(N), sum(a)))
        for i in range(N):
            self.assertTrue(math.isclose(f[i], a[i]))

    def test_array(self):
        N = 10000
        a = array.array('l')
        for _ in range(N):
            a.append(random.randint(-1000, 1000))
        f = Fenwick(a)
        b = f.values()
        self.assertEqual(a, b)
        self.assertIsInstance(b, array.array)
        self.assertEqual(f.prefix_sum(N), sum(a))


if __name__ == '__main__':
    unittest.main()
