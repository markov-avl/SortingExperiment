from typing import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class Generate(QAction):
    def __init__(self, function: Callable) -> None:
        super().__init__()
        self.setText('Генерация')
        self.setStatusTip('Сгенерировать тесты')
        self.setShortcut('Ctrl+G')
        self.setIcon(QIcon('icons/generate.png'))
        self.triggered.connect(function)
