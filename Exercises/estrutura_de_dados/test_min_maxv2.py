import unittest

from estrutura_de_dados.min_max_recursive_v2 import minmax


class TestMinMax(unittest.TestCase):
    def test_min_max_lista_com_um_elemento(self):
        resultado = minmax([1])
        self.assertEqual((1, 1), resultado)

    def test_min_max_lista_com_dois_elementos(self):
        resultado = minmax([1, 2])
        self.assertEqual((1, 2), resultado)

    def test_min_max_lista_sem_elementos(self):
        with self.assertRaises(ValueError):
            minmax([])
            
