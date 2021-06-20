from random import randint

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from buttons.random import RandomButton
from widgets.amount import Amount


class Partialness(QWidget):
    __DEFAULT = 16

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._label = QLabel('Длина:')
        self._amount = Amount()
        self._random = RandomButton(self._random_number)
        self._layout = QHBoxLayout(self)
        self._init_ui()

    def _set_layout(self) -> None:
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self._label, 0)
        self._layout.addWidget(self._amount, 1)
        self._layout.addWidget(self._random, 2)

    def _init_ui(self) -> None:
        self._amount.setValue(self.__DEFAULT)
        self._label.setStyleSheet('font-size: 8pt;')
        self._set_layout()
        self.setLayout(self._layout)

    def _random_number(self) -> None:
        self._amount.setValue(randint(1, 64))

    def value(self) -> int:
        return self._amount.value()

    def reset(self) -> None:
        self.setHidden(False)
        self._amount.setValue(self.__DEFAULT)
