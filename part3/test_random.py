import unittest
import numpy as np
import numpy.testing as npt

class MyTestCase(unittest.TestCase):
    def test_something(self):
        from numpy.random import normal

        mymean = 12
        mystd=3
        npoints = 1000000

        random_sample = normal(mymean,mystd,npoints)
        self.assertAlmostEqual(np.mean(random_sample), mymean, places=2)
        self.assertAlmostEqual(np.std(random_sample), mystd, places=2)


if __name__ == '__main__':
    unittest.main()
