from PyQt5.QtWidgets import QSpinBox, QLineEdit, QSizePolicy


class Amount(QSpinBox):
    def __init__(self) -> None:
        super().__init__()
        self.setRange(1, 1_000_000)
        self.setSingleStep(1)
        self.setLineEdit(QLineEdit())
        self.setStyleSheet('font-size: 8pt;')
        self.setFixedHeight(25)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
