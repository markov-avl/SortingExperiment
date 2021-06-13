from typing import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class ShowComparisons(QAction):
    def __init__(self, function: Callable) -> None:
        super().__init__()
        self.setText('Сравнения')
        self.setStatusTip('Показать сравнения')
        self.setShortcut('Ctrl+Shift+C')
        self.setIcon(QIcon('icons/show-comparisons.png'))
        self.triggered.connect(function)
