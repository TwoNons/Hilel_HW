"""Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""

from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_square(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.__a = a
        self.__b = b
        self.__h = h

    def get_square(self):
        return self.__a * self.__h

    def get_perimeter(self):
        return 2 * (self.__a + self.__b)

class Triangle(Figure):
    def __init__(self, a, b, c, h):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__h = h

    def get_square(self):
        return 1/2 * self.__a * self.__h

    def get_perimeter(self):
        return self.__a + self.__b + self.__c

class Trapezoid(Figure):
    def __init__(self, a, b, c, d, h):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__h = h

    def get_square(self):
        return (self.__a + self.__b) / 2 * self.__h

    def get_perimeter(self):
        return self.__a + self.__b + self.__c + self.__d

figure = [Parallelogram(3, 4, 6), Triangle(6, 6, 7, 8), Trapezoid(5, 6, 7, 8, 2)]

for i in figure:
    print(f"Площа {type(i).__name__} дорiвнює {i.get_square()}")
    print(f"Периметр {type(i).__name__} дорiвнює {i.get_perimeter()}")
    print()