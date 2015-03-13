import random
import unittest
from answer import timesort

class TestSequenceFunctions(unittest.TestCase):

    def test_timesort(self):
        self.assertEqual(timesort('5am', '6am'), -1)

if __name__ == '__main__':
    unittest.main()
