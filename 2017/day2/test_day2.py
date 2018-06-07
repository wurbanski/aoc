import unittest
import day2

class TestDay2(unittest.TestCase):
    sample = ((5,1,9,5),
              (7,5,3),
              (2,4,6,8))
    chksum = 18

    def test_solution(self):
        self.assertEqual(
            day2.solution(self.sample),
            self.chksum)

if __name__ == '__main__':
    unittest.main()
