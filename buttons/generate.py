from PyQt5.QtWidgets import QPushButton


class GenerateButton(QPushButton):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setText('Generate')
