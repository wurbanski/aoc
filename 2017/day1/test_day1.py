import day1
import unittest

class TestDay1(unittest.TestCase):
    basic_cases = (('1122', 3),
                   ('1111', 4),
                   ('1234', 0),
                   ('91212129', 9))

    adv_cases = (('1212', 6),
                 ('1221', 0),
                 ('123425', 4),
                 ('123123', 12),
                 ('12131415', 4))

    def test_basic(self):
        for input_string, answer in self.basic_cases:
            result = day1.solutionN(input_string, 1)
            self.assertEqual(answer, result)

    def test_adv(self):
        for input_string, answer in self.adv_cases:
            result = day1.solutionN(input_string)
            self.assertEqual(answer, result)

if __name__ == '__main__':
    unittest.main()
