from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QLabel

from buttons.generate import GenerateButton
from generator.generator import Generator
from widgets.amount import Amount
from widgets.partialness import Partialness

STYLESHEET = 'font-size: 8pt;'


class Option(QWidget):
    def __init__(self, *args, parent=None) -> None:
        super().__init__(parent=parent)
        self._index = 0
        self._names = args
        self._layout = QVBoxLayout()
        self._group = QButtonGroup()
        self._options = [QRadioButton(option) for option in self._names]
        self.partialness = Partialness()
        self._init_ui()

    @property
    def option(self) -> QRadioButton:
        return self._group.checkedButton()

    def on_click(self) -> None:
        index = self._names.index(self.option.text())
        if index != self._index:
            if 4 <= index <= 6:
                self._layout.insertWidget(index + 1, self.partialness)
                self.partialness.reset()
            else:
                self.partialness.setHidden(True)
                self._layout.removeWidget(self.partialness)
            self._index = index

    def _set_checkboxes(self) -> None:
        for option in self._options:
            option.clicked.connect(self.on_click)
        if len(self._options):
            self._options[0].setChecked(True)

    def _init_ui(self) -> None:
        self._set_checkboxes()
        for option in self._options:
            option.setStyleSheet(STYLESHEET)
            self._layout.addWidget(option)
            self._group.addButton(option)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)


class GenerateWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._generator = Generator(self)
        self._tests = {
            'Возрастающая': self._generator.generate_sorted,
            'Убывающая': self._generator.generate_reverse_sorted,
            'В случайном порядке': self._generator.generate_random,
            'Повторяющееся число': self._generator.generate_repetitive,
            'Частично возрастающая': self._generator.generate_partially_sorted,
            'Частично убывающая': self._generator.generate_partially_reverse_sorted,
            'Частично возрастающая и убывающая': self._generator.generate_partially_sorted_and_reverse_sorted
        }
        self._options = Option(*self._tests.keys())
        self._count = QLabel('Количество элементов:')
        self._amount = Amount()
        self._generate_button = GenerateButton(self._generate_and_save_test)
        self._layout = QVBoxLayout()
        self._init_ui()

    def _set_layout(self) -> None:
        self._layout.addWidget(self._options, 0)
        self._layout.addWidget(self._count, 1, alignment=Qt.AlignBottom)
        self._layout.addWidget(self._amount, 2)
        self._layout.addWidget(self._generate_button, 3)

    def _set_count(self) -> None:
        self._count.setStyleSheet(STYLESHEET)

    def _init_ui(self) -> None:
        self._set_count()
        self._set_layout()
        self.setWindowTitle('Генерация')
        self.setStyleSheet('font-size: 12pt;')
        self.setFixedSize(250, 305)
        self.setWindowIcon(QIcon('icons/generate.png'))
        self.setLayout(self._layout)

    def _generate_and_save_test(self) -> None:
        index = list(self._tests.keys()).index(self._options.option.text())
        if 4 <= index <= 6:
            self._tests[self._options.option.text()](self._amount.value(), self._options.partialness.value())
        else:
            self._tests[self._options.option.text()](self._amount.value())

    def close(self) -> bool:
        pass
