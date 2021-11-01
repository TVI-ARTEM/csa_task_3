from matrix.matrix import *

"""container.py - содержит тип данных - матрица, представляющий простейший контейнер"""

"""Простейший контейнер на основе одномерного массива."""


class Container:
    """Инициализация контейнера"""

    def __init__(self):
        self.__matrices = [Matrix]

    """Получить матрицы из контейнера"""
    @property
    def matrices(self):
        return self.__matrices

    """Инициализировать данные в контейнере"""
    def initialize(self, data: str):
        matrices_data = data.lower().split("end")
        for row_index in range(len(matrices_data)):
            matrices_data[row_index] = matrices_data[row_index].replace("\n", " ").split()
        self.matrices.clear()
        matrices_data = [data for data in matrices_data if len(data) > 0]

        for matrix_data in matrices_data:
            try:
                self.matrices.append(Matrix.create_matrix(matrix_data))
            except ValueError as exception:
                print(exception)

    """Случайным образом инициализировать данные в контейнере"""
    def random_initialize(self, length: int):
        if not 0 < length <= 100000:
            raise ValueError("Incorrect length of container")
        self.matrices.clear()

        for matrix in [Matrix.random_create_matrix() for _ in range(length)]:
            self.matrices.append(matrix)

    """Получить информацию о контейнере"""
    def __str__(self):
        if len(self.matrices) > 0:
            result = f"Container contains {len(self.matrices)} elements:\n"
            for index, matrix in enumerate(self.matrices):
                result += f"{index + 1}: {str(matrix)}\n"
        else:
            result = "Container is empty."
        return result

    """Записать данные контейнера в файл"""
    def to_file(self, file: TextIO):
        file.write(str(self))

    """Отсортировать данные в контейнере"""
    def sort(self):
        for i in range(1, len(self.matrices)):
            j = i
            while j > 0 and self.matrices[j - 1].average < self.matrices[j].average:
                self.matrices[j - 1], self.matrices[j] = self.matrices[j], self.matrices[j - 1]
                j -= 1

    """Очистить контейнер"""
    def clear(self):
        self.matrices.clear()
