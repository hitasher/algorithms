import unittest

from dijkstra_algorithm import DijkstraAlgorithm


class TestDijkstraAlgorithm(unittest.TestCase):
    def test_sample(self):
        link_dictionary = {
            'a': {'b': 5, 'c': 0},
            'b': {'d': 15, 'e': 20},
            'c': {'d': 30, 'e': 35},
            'd': {'f': 20},
            'e': {'f': 10},
            'f': {}
        }
        dijkstra = DijkstraAlgorithm(link_dictionary, 'a')
        self.assertEqual(dijkstra.calculate_way('f'), (['a', 'b', 'e', 'f'], 35))
        self.assertEqual(dijkstra.calculate_way('e'), (['a', 'b', 'e'], 25))
        self.assertEqual(dijkstra.calculate_way('d'), (['a', 'b', 'd'], 20))
        self.assertEqual(dijkstra.calculate_way('c'), (['a', 'c'], 0))
        self.assertEqual(dijkstra.calculate_way('b'), (['a', 'b'], 5))
