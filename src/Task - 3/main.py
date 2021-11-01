import os
import sys

sys.path.insert(1, 'matrix')

from container.container import *
from pathlib import Path
from time import perf_counter

"""main.py - содержит главную функцию, выполняющую тестирование."""


def command_line_error():
    print("incorrect command line!\n" +
          "  Waited:\n" +
          "     command -f infile outfile01 outfile02\n" +
          "  Or:\n" +
          "     command -n number outfile01 outfile02\n")


def qualifier_value_error():
    print("incorrect qualifier value!\n" +
          "  Waited:\n" +
          "     command -f infile outfile01 outfile02\n" +
          "  Or:\n" +
          "     command -n number outfile01 outfile02\n")


def create_dir(path: str):
    try:
        os.makedirs(os.path.dirname(path))
    except Exception:
        pass


if __name__ == '__main__':
    start_count = perf_counter()
    args = sys.argv
    if len(args) != 5:
        command_line_error()
        exit(1)

    print("Start\n")
    cont = Container()
    if args[1] == '-f':
        create_dir(args[2])

        file_open = Path(args[2])
        file_open.touch(exist_ok=True)
        with open(file_open, "r") as file:
            data = file.read()
            cont.initialize(data)
    elif args[1] == '-n':
        try:
            cont.random_initialize(int(args[2]))
        except Exception as exception:
            print(exception)
            exit(2)
    else:
        qualifier_value_error()
        exit(3)

    create_dir(args[3])

    """Вывод контейнера до сортировки."""
    with open(args[3], "w+") as file_write:
        cont.to_file(file_write)
        file_write.write(f"\nTime: {round(perf_counter() - start_count, 4)} s\n")
    cont.sort()

    create_dir(args[4])

    """Вывод контейнера после сортировки."""
    with open(args[4], "w+") as file_write:
        file_write.write("---Sorted Container---\n")
        cont.to_file(file_write)
        file_write.write(f"\nTime sorted: {round(perf_counter() - start_count, 4)} s\n")
        cont.clear()
        file_write.write(f"\nTime after clearing: {round(perf_counter() - start_count, 4)} s\n")

    print("End\n")
