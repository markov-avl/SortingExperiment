from typing import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class Exit(QAction):
    def __init__(self, function: Callable) -> None:
        super().__init__()
        self.setText('Закрыть')
        self.setStatusTip('Закрыть программу')
        self.setIcon(QIcon('icons/quit.png'))
        self.setShortcut('Ctrl+Q')
        self.triggered.connect(function)
