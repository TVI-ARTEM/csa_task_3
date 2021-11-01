import random
from .matrix import Matrix, TextIO

"""diagonal.py - содержит описание диагональной квадратной матрицы."""

"""Диагональная квадратная матрица."""


class Diagonal(Matrix):
    """Инициализировать объект матрицы"""

    def __init__(self):
        super().__init__()
        self.__numbers = []

    """Получить числа матрицы"""

    @property
    def numbers(self):
        return self.__numbers

    """Получить среднее арифметическое матрицы"""

    @property
    def average(self):
        return sum(self.numbers) / self.dimension ** 2

    """Проинициализировать данные матрицы"""

    def initialize(self, args: []):
        if len(args) != self.dimension:
            self.correct = False
            raise ValueError("Incorrect length of arguments.")

        self.numbers.clear()

        for num_index in range(self.dimension):
            self.numbers.append(float(args.pop(0)))

    """Случайно проинициализировать данные матрицы"""

    def random_initialize(self):
        self.numbers.clear()

        for num_index in range(self.dimension):
            self.numbers.append(random.uniform(-10, 10))

    """Получить данные матрицы"""

    def __str__(self):
        result = "It's diagonal matrix. Dimension = {0}\n".format(self.dimension)
        if self.correct:
            current_index = 0
            for row_index in range(self.dimension):
                for column_index in range(self.dimension):
                    if row_index == column_index:
                        result += str(round(self.numbers[current_index], 4)) + " "
                        current_index += 1
                    else:
                        result += "0 "
                result += "\n"
            result += "Average: {0}\n".format(self.average)
        else:
            result = "Incorrect Matrix\n"

        return result

    """Записать данные матрицы в файл"""

    def to_file(self, file_stream: TextIO):
        file_stream.write(str(self))
