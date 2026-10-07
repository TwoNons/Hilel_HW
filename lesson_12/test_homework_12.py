import unittest
from lesson_10 import homework_10_2

class Test_Figure(unittest.TestCase):                          # 1) проверка действительно Figure абстрактная
    def test_abstract_methods(self):
        with self.assertRaises(TypeError):
            homework_10_2.Figure()

    def test_square_parallelogram(self):                       # 2) результаты площади паралелограма
        figure = homework_10_2.Parallelogram(3,4,6)
        self.assertEqual(figure.get_square(),18)

    def test_perimeter_parallelogram(self):                    # 3) результаты периметра паралелограма
        figure = homework_10_2.Parallelogram(3,4,6)
        self.assertEqual(figure.get_perimeter(),14)

    def test_square_triangle(self):                            # 4) результаты площади треугольника
        figure = homework_10_2.Triangle(6,7,8, 8)
        self.assertEqual(figure.get_square(),24)

    def test_perimeter_triangle(self):                         # 5) результаты периметра треугольника
        figure = homework_10_2.Triangle(6,7,8, 8)
        self.assertEqual(figure.get_perimeter(),21)

    def test_square_trapezoid(self):                                  # 6) результаты площади трапеции
        firure = homework_10_2.Trapezoid(5,6,7, 8,2)
        self.assertEqual(firure.get_square(),11)

    def test_perimeter_trapezoid(self):                               # 7) результаты периметра трапеции
        firure = homework_10_2.Trapezoid(5,6,7, 8, 2)
        self.assertEqual(firure.get_perimeter(),26)

    def test_square_trapezoid_float_number(self):                     # 8) результаты площади трапеции с результатом нецелого числа
        figure = homework_10_2.Trapezoid(5,6,7, 8, 3)
        self.assertEqual(figure.get_square(),16.5)

    def test_presence_methods_all_figures(self):                      # 9) проверка присутствия методов площади и периметра в фигурах
        figures = [homework_10_2.Parallelogram(3, 4, 6),
                   homework_10_2.Triangle(6, 7, 8, 8),
                   homework_10_2.Trapezoid(5, 6, 7, 8, 2)]

        for i in figures:
            self.assertTrue(hasattr(i, 'get_square'))
            self.assertTrue(hasattr(i, 'get_perimeter'))

    def Figure_parents_figures(self):                                 # 10) проверка наследования фигур от Figure
        figures = [homework_10_2.Parallelogram(3, 4, 6),
                   homework_10_2.Triangle(6, 7, 8, 8),
                   homework_10_2.Trapezoid(5, 6, 7, 8, 2)]
        for i in figures:
            self.assertIsInstance(i, homework_10_2.Figure)

if __name__ == '__main__':
    unittest.main()
