from typing import Callable

from PyQt5.QtWidgets import QPushButton


class RandomButton(QPushButton):
    def __init__(self, function: Callable, parent=None) -> None:
        super().__init__(parent)
        self.setText('Случайное число')
        self.setStyleSheet('font-size: 8pt;')
        self.setFixedSize(150, 25)
        self.clicked.connect(function)
