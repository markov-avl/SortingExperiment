from PyQt5.QtWidgets import QFileDialog


class Generator:
    OPEN_DIRECTORY = 'Выберите директорию для сохранения теста'
    DEFAULT_DIRECTORY = './'
    EXTENSION = '.test'
    _save_directory = None

    def __init__(self, parent) -> None:
        self._parent = parent

    def save_test(self, test_name: str, test: list) -> None:
        directory = QFileDialog.getExistingDirectory(self._parent, self.OPEN_DIRECTORY, self.DEFAULT_DIRECTORY)
        if directory:
            path = f'{directory}/{test_name}{len(test)}{self.EXTENSION}'
            with open(path, 'w') as outfile:
                outfile.write(str(test))

    def generate_sorted(self, n: int) -> None:
        test = list(range(n))
        self.save_test('sorted-', test)

    def generate_reverse_sorted(self, n: int) -> None:
        test = list(range(n))
        test.reverse()
        self.save_test('reverse-sorted-', test)
