from typing import Callable

from PyQt5.QtWidgets import QPushButton, QSizePolicy


class GenerateButton(QPushButton):
    def __init__(self, function: Callable, parent=None) -> None:
        super().__init__(parent)
        self.setText('Генерировать')
        self.setStyleSheet('font-size: 8pt;')
        self.setFixedHeight(35)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.clicked.connect(function)
