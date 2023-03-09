import functions

# принимаем координаты точек
lat1, lon1 = map(float, input('Введите координаты первой точки через пробел: ').split())
lat2, lon2 = map(float, input('Введите координаты второй точки через пробел: ').split())

# вычисляем расстояние между точками
distance = functions.distance_on_sphere(lat1, lon1, lat2, lon2)

# выводим результат
print(f'Расстояние между точками: {distance:.2f} км')
