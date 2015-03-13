import random
import unittest
from answer import timesort

class TestSequenceFunctions(unittest.TestCase):

    def test_timesort(self):
        self.assertEqual(timesort('5am', '6am'), -1)
        self.assertEqual(timesort('6am', '5am'), 1)
        self.assertEqual(timesort('10am', '1pm'), -1)

if __name__ == '__main__':
    unittest.main()
