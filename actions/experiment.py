from typing import Callable

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class Experiment(QAction):
    def __init__(self, function: Callable) -> None:
        super().__init__()
        self.setText('Эксперимент')
        self.setStatusTip('Провести эксперимент')
        self.setShortcut('Ctrl+E')
        self.setIcon(QIcon('icons/experiment.png'))
        self.triggered.connect(function)
