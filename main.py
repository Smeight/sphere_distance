from functions import get_coordinates, get_distance
import sys


def parse_arguments(args):
    """
    Функция для парсинга аргументов командной строки.
    Возвращает координаты двух точек в формате (широта, долгота).
    """
    try:
        lat1, lon1, lat2, lon2 = map(float, args)
    except ValueError:
        print("Некорректный формат координат.")
        sys.exit(1)
    return (lat1, lon1), (lat2, lon2)


def main(args):
    """
    Функция для обработки входных данных и запуска расчетов.
    """
    # Парсим аргументы командной строки
    try:
        point1, point2 = parse_arguments(args)
    except IndexError:
        print("Недостаточно аргументов.")
        sys.exit(1)

    # Получаем координаты точек
    coord1 = get_coordinates(*point1)
    coord2 = get_coordinates(*point2)

    # Вычисляем расстояние между точками
    distance = get_distance(coord1, coord2)

    # Выводим результаты
    print(f"Расстояние между точками: {distance} км")


if __name__ == '__main__':
    main(sys.argv[1:])
