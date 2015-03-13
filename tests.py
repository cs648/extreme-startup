import unittest
from answer import timesort
from answer import write_roman
from answer import multiply

class TestSequenceFunctions(unittest.TestCase):

    def test_timesort(self):
        self.assertEqual(timesort('5am', '6am'), -1)
        self.assertEqual(timesort('6am', '5am'), 1)
        self.assertEqual(timesort('10am', '1pm'), -1)


    def test_romannumerals(self):
        self.assertEquals(write_roman('17'), 'XVII')
        self.assertEquals(write_roman('419'), 'CDXIX')

    def test_multiply(self):
        self.assertEquals(multiply('5','9'), 45)

if __name__ == '__main__':
    unittest.main()
