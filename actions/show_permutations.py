from typing import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class ShowPermutations(QAction):
    def __init__(self, function: Callable) -> None:
        super().__init__()
        self.setText('Перестановки')
        self.setStatusTip('Показать перестановки')
        self.setShortcut('Ctrl+Shift+P')
        self.setIcon(QIcon('icons/show-permutations.png'))
        self.triggered.connect(function)
