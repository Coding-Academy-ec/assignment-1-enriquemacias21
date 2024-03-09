import unittest
from main import *

class TestEjercicio(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 5), 8)
      

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_contar_vocales(self):
        self.assertEqual(contar_vocales("Enrique Macías"), 6)

    def test_palindromo(self):
        self.assertFalse(palindromo("casa"))
    
    def test_suma_lista(self):
        self.assertEqual(suma_lista([1, 2, 3, 4, 5]), 15)


if __name__ == "__main__":
    unittest.main()
