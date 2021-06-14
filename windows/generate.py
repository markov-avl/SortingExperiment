from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QLabel

from buttons.generate import GenerateButton
from generator.generator import Generator
from widgets.amount import Amount


STYLESHEET = 'font-size: 8pt;'


class Option(QWidget):
    def __init__(self, *args, parent=None) -> None:
        super().__init__(parent=parent)
        self._layout = QVBoxLayout(self)
        self._group = QButtonGroup(self)
        self._options = [QRadioButton(option, self) for option in args]
        self._init_ui()

    @property
    def option(self) -> QRadioButton:
        return self._group.checkedButton()

    def _set_checkboxes(self) -> None:
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
    def __init__(self):
        super().__init__()
        self._generator = Generator(self)
        self._tests = {
            'Отсортированная': self._generator.generate_sorted,
            'Отсортированная инвентированная': self._generator.generate_reverse_sorted
        }
        self._options = Option(*self._tests.keys())
        self._count = QLabel('Количество элементов:')
        self._amount = Amount()
        self._generate_button = GenerateButton(self._generate_and_save_test)
        self._layout = QVBoxLayout()
        self._init_ui()

    def _set_layout(self) -> None:
        self._layout.addWidget(self._options)
        self._layout.addWidget(self._count)
        self._layout.addWidget(self._amount)
        self._layout.addWidget(self._generate_button)

    def _set_count(self) -> None:
        self._count.setStyleSheet(STYLESHEET)

    def _init_ui(self) -> None:
        self._set_count()
        self._set_layout()
        self.setWindowTitle('Генерация')
        self.setStyleSheet('font-size: 12pt;')
        self.setFixedSize(300, 200)
        self.setWindowIcon(QIcon('icons/generate.png'))
        self.setLayout(self._layout)

    def _generate_and_save_test(self) -> None:
        self._tests[self._options.option.text()](self._amount.value())
