import unittest
from functions import FUNCTIONS, resolve, resolve_consistently, resolve_list_consistently


class FunctionsTestCase(unittest.TestCase):
    def test_functions_are_appropriate(self):
        self.assertEqual(4, FUNCTIONS['a'](2))
        self.assertEqual(5, FUNCTIONS['b'](2))
        self.assertEqual(1, FUNCTIONS['c'](2))
        self.assertEqual(0.5, FUNCTIONS['d'](5))
        self.assertEqual(10, FUNCTIONS['e'](0))
        self.assertEqual(1, FUNCTIONS['f'](2))
        self.assertFalse('aa' in FUNCTIONS)

    def test_resolve(self):
        self.assertEqual(4, resolve('a', 2))
        self.assertEqual(22.325, resolve('aa', 22.325))
        self.assertEqual([4, 2], resolve('aa', [4, 2]))
        self.assertEqual([4, 2], resolve('a', [4, 2]))

    def test_consistently(self):
        self.assertEqual(9, resolve_consistently(['a', 'b'], 2))
        self.assertEqual(10.1, resolve_consistently(['c', 'd', 'e'], 2))
        self.assertEqual(1, resolve_consistently(['f'], 2))
        self.assertEqual(10.1, resolve_consistently('cde', 2))

    def test_resolve_list_consistently(self):
        self.assertEqual([4.5, 9.5, 25.5], resolve_list_consistently(['a', 'b', 'f'], [2, 3, 5]))
        self.assertEqual([4.5, 9.5, 25.5], resolve_list_consistently('abf', [2, 3, 5]))


if __name__ == '__main__':
    unittest.main()
