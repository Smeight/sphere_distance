import unittest
import osmnx as ox
from functions import distance_on_sphere, route_distance


class TestFunctions(unittest.TestCase):
    def setUp(self):
        # загружаем граф для тестирования маршрута
        self.G = ox.graph_from_place('Manhattan, New York City, New York, USA', network_type='drive')

    def test_distance_on_sphere(self):
        # тестируем расстояние между Нью-Йорком и Лос-Анджелесом
        self.assertAlmostEqual(distance_on_sphere(40.7128, -74.0060, 34.0522, -118.2437), 3938, delta=10)
        # тестируем расстояние между Парижем и Москвой
        self.assertAlmostEqual(distance_on_sphere(48.8566, 2.3522, 55.7558, 37.6173), 2484, delta=10)

    def test_route_distance(self):
        # тестируем маршрут между двумя точками в Нью-Йорке
        distance = route_distance(40.738, -73.98, 40.741, -73.99, self.G)
        self.assertAlmostEqual(distance, 1.4, delta=0.1)
        # тестируем маршрут между двумя точками в Лондоне
        distance = route_distance(51.5113, -0.1198, 51.5033, -0.1195, self.G)
        self.assertAlmostEqual(distance, 1.0, delta=0.1)


if __name__ == '__main__':
    unittest.main()
