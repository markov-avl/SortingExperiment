from typing import Callable

from PyQt5.QtWidgets import QPushButton


class CancelButton(QPushButton):
    def __init__(self, function: Callable, parent=None) -> None:
        super().__init__(parent)
        self.setText('Отмена')
        self.setStyleSheet('font-size: 8pt;')
        self.setFixedSize(70, 35)
        self.clicked.connect(function)
