import unittest
from functions import distance_on_sphere


class TestDistanceOnSphere(unittest.TestCase):
    def test_distance(self):
        # проверяем расстояние между Нью-Йорком и Лос-Анджелесом
        self.assertAlmostEqual(distance_on_sphere(40.7128, -74.0060, 34.0522, -118.2437), 3938, delta=10)
        # проверяем расстояние между Парижем и Москвой
        self.assertAlmostEqual(distance_on_sphere(48.8566, 2.3522, 55.7558, 37.6173), 2484, delta=10)


if __name__ == '__main__':
    unittest.main()
