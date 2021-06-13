from PyQt5.QtWidgets import QMenuBar, QAction


class MenuBar(QMenuBar):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self._file = self.addMenu('&Файл')
        self._run = self.addMenu('&Выполнить')
        self._help = self.addMenu('&Справка')

    def add_to_file(self, action: QAction) -> None:
        self._file.addAction(action)

    def add_to_run(self, action: QAction) -> None:
        self._run.addAction(action)

    def add_separator_to_file(self) -> None:
        self._file.addSeparator()

    def add_separator_to_run(self) -> None:
        self._run.addSeparator()
