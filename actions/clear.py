from typing import Callable

from PyQt5.QtWidgets import QAction


class Clear(QAction):
    def __init__(self, function: Callable) -> None:
        super().__init__()
        self.setText('Очистить')
        self.setStatusTip('Очистить состояние')
        self.setShortcut('Ctrl+C')
        self.triggered.connect(function)
