import random
from typing import TextIO

"""matrix.py - содержит описание обобщающей квадратной матрицы."""

"""Структура, обобщающая все имеющиеся квадратные матрицы."""


class Matrix:
    """Инициализировать объект матрицы"""

    def __init__(self):
        self.__dimension = 0
        self.__correct = True

    """Получить размерность матрицы"""

    @property
    def dimension(self):
        return self.__dimension

    """Установить размерность матрицы"""

    @dimension.setter
    def dimension(self, dimension: int):
        if dimension > 0:
            self.__dimension = dimension
        else:
            raise ValueError("Dimension must be more than 0.")

    """Получить информацию о корректности матрицы"""

    @property
    def correct(self):
        return self.__correct

    """Установить информацию о корректности матрицы"""

    @correct.setter
    def correct(self, correct):
        self.__correct = correct

    """Получить среднее арифметическое матрицы"""

    @property
    def average(self) -> float:
        return 0

    """Проинициализировать данные матрицы"""

    def initialize(self, args: []):
        pass

    """Случайно проинициализировать данные матрицы"""

    def random_initialize(self):
        pass

    """Записать данные матрицы в файл"""

    def to_file(self, file_stream: TextIO):
        pass

    """Создать матрицу по полученным данным"""

    @staticmethod
    def create_matrix(args: []):
        if len(args) < 3 or str(args[0]) != "begin":
            raise ValueError("Incorrect input. Length of arguments less thane 3 or arguments are incorrect.")
        key, dimension = int(args[1]), int(args[2])
        if key == 1:
            from matrix.square import Square
            matrix = Square()
        elif key == 2:
            from matrix.diagonal import Diagonal
            matrix = Diagonal()
        elif key == 3:
            from matrix.ltrinagle import LTriangle
            matrix = LTriangle()
        else:
            raise ValueError("Incorrect key value. Must be in range from 1 to 3.")

        if dimension < 1:
            raise ValueError("Incorrect dimension. Must be more than 0.")

        matrix.dimension = dimension
        matrix.initialize(args[3:])
        return matrix

    """Случайным образом создать матрицу"""

    @staticmethod
    def random_create_matrix():
        key, dimension = random.randint(1, 3), random.randint(1, 20)
        matrix = Matrix()
        if key == 1:
            from matrix.square import Square
            matrix = Square()
        elif key == 2:
            from matrix.diagonal import Diagonal
            matrix = Diagonal()
        elif key == 3:
            from matrix.ltrinagle import LTriangle
            matrix = LTriangle()

        matrix.dimension = dimension
        matrix.random_initialize()
        return matrix
