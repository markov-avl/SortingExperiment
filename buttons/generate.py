from typing import Callable

from PyQt5.QtWidgets import QPushButton, QSizePolicy


class GenerateButton(QPushButton):
    # def __init__(self, function: Callable, parent=None) -> None:  TODO
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setText('Генерировать')
        self.setStyleSheet('font-size: 8pt;')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.pressed.connect(function)
