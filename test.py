import unittest
from funciones import diferencias_dividas,polinomio

class TestDiferenciasDivididas(unittest.TestCase):
    def test_diferenciasDivididas_withEmptyLists(self):
        self.assertEqual(diferencias_dividas([], []), [])

    def test_diferenciasDivididas_withSingleElementLists(self):
        self.assertEqual(diferencias_dividas([1], [2]), [[2]])

    def test_diferenciasDivididas_withEqualLists(self):
        self.assertEqual(diferencias_dividas([1, 2, 3], [4, 5, 6]), [[4, 0, 0], [4, 1, 0], [4, 1, 1]])

    def test_diferenciasDivididas_withDifferentLengthLists(self):
        self.assertEqual(diferencias_dividas([1, 2, 3], [4, 5]), [[4, 0, 0], [4, 1, 0]])

unittest.main()