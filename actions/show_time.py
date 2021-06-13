from typing import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class ShowTime(QAction):
    def __init__(self, function: Callable) -> None:
        super().__init__()
        self.setText('Время')
        self.setStatusTip('Показать время')
        self.setShortcut('Ctrl+Shift+T')
        self.setIcon(QIcon('icons/show-time.png'))
        self.triggered.connect(function)
