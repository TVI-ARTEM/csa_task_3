import random
from matrix.matrix import Matrix, TextIO

"""square.py - содержит описание обычной квадратной матрицы."""

"""Обычная квадратная матрица."""


class Square(Matrix):
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
        return sum([sum(row) for row in self.numbers]) / self.dimension ** 2

    """Проинициализировать данные матрицы"""
    def initialize(self, args: []):
        if len(args) != self.dimension ** 2:
            self.correct = False
            raise ValueError("Incorrect length of arguments.")

        self.numbers.clear()

        for row_index in range(self.dimension):
            row = []
            for column_index in range(self.dimension):
                row.append(float(args.pop(0)))
            self.numbers.append(row)

    """Случайно проинициализировать данные матрицы"""
    def random_initialize(self):
        self.numbers.clear()

        for row_index in range(self.dimension):
            row = []
            for column_index in range(self.dimension):
                row.append(random.uniform(-10, 10))
            self.numbers.append(row)

    """Получить данные матрицы"""
    def __str__(self):
        result = "It's square matrix. Dimension = {0}\n".format(self.dimension)
        if self.correct:
            for row in self.numbers:
                for number in row:
                    result += str(round(number, 4)) + " "
                result += "\n"
            result += "Average: {0}\n".format(self.average)
        else:
            result = "Incorrect Matrix\n"

        return result

    """Записать данные матрицы в файл"""
    def to_file(self, file_stream: TextIO):
        file_stream.write(str(self))
