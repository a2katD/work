# Библиотека math - нужна для работы счислами и математическими функциями
import math


# math.pi - возвращает число пи
def circumference(radius):  # возвращает длинну окружности
	return 2 * radius * math.pi


def area_circle(radius):  # возвращает площадь окружности
	return (radius ** 2) * math.pi


# math.sqrt - возвращает квадратный корень числа
def distance_coordinates(x1, y1, x2, y2):  # возвращает растояние между точками
	return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# math.factorial(x) возвращает факториал числа

# Библиотека random
from random import randint, choice, sample, shuffle

players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
randint(1, 100)  # возвращает случайное число от 1 до 100
choice(players)  # возвращает случайное значение из последовательности
sample(players, 3)  # возвращает 3 случайные значения из последовательности
shuffle(players) # случайно перемешивает последовательность, возвращает None
print(players)

import sotr

sotr