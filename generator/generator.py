import os
from random import randint

from PyQt5.QtWidgets import QFileDialog


class Generator:
    OPEN_DIRECTORY = 'Выберите директорию для сохранения последовательности'
    DEFAULT_DIRECTORY = './'
    EXTENSION = '.test'
    _save_directory = None

    def __init__(self, parent) -> None:
        self._parent = parent

    def save_test(self, test_name: str, test: list) -> None:
        directory = QFileDialog.getExistingDirectory(self._parent, self.OPEN_DIRECTORY, self.DEFAULT_DIRECTORY)
        if directory:
            files = os.listdir(directory)
            path = f'{directory}/{test_name}{len(test)}{self.EXTENSION}'
            k = 1
            while path in files:
                path = f'{directory}/{test_name}{len(test)}({k}){self.EXTENSION}'
                k += 1
            with open(path, 'w') as outfile:
                outfile.write(' '.join(map(str, test)))

    def generate_sorted(self, n: int) -> None:
        test = list(range(n))
        self.save_test('sorted-', test)

    def generate_reverse_sorted(self, n: int) -> None:
        test = list(range(n))
        test.reverse()
        self.save_test('reverse-sorted-', test)

    def generate_random(self, n: int) -> None:
        test = [randint(0, 1_000_000) for _ in range(n)]
        self.save_test('random-', test)

    def generate_repetitive(self, n: int) -> None:
        test = [n] * n
        self.save_test('repetitive-', test)

    def generate_partially_sorted(self, n: int, length: int = None) -> None:
        test = list()
        if 1 > length or length > 1_000_000:
            length = randint(0, 32) + 1
        while len(test) < n:
            start = randint(0, 1_000_000)
            test.extend([start := start + randint(0, 100) for _ in range(length)])
        test = test[: n]
        self.save_test(f'{length}-partially-sorted-', test)

    def generate_partially_reverse_sorted(self, n: int, length: int = None) -> None:
        test = list()
        if 1 > length or length > 1_000_000:
            length = randint(1, 32)
        while len(test) < n:
            start = randint(0, 1_000_000)
            test.extend([start := start - randint(0, 100) for _ in range(length)])
        test = test[: n]
        self.save_test(f'{length}-partially-reverse-sorted-', test)

    def generate_partially_sorted_and_reverse_sorted(self, n: int, length: int = None) -> None:
        test = list()
        if 1 > length or length > 1_000_000:
            length = randint(1, 32)
        positive = True
        while len(test) < n:
            start = randint(0, 1_000_000)
            if positive:
                test.extend([start := start - randint(0, 100) for _ in range(length)])
            else:
                test.extend([start := start + randint(0, 100) for _ in range(length)])
            positive = not positive
        test = test[: n]
        self.save_test(f'{length}-partially-sorted-and-reverse-sorted-', test)
