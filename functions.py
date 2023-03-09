from math import radians, cos, sin, asin, sqrt


def distance_on_sphere(lat1, lon1, lat2, lon2):
    # переводим координаты в радианы
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # вычисляем расстояние между точками
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # радиус Земли в км
    return c * r
