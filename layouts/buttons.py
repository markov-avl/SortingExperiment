from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout


class ButtonsLayout(QVBoxLayout):
    def __init__(self, *args, button_weigt: int = 100, button_height: int = 25, parent=None) -> None:
        super().__init__(parent)
        self.setAlignment(Qt.AlignTop)
        self.__buttons = args
        self.__button_width = button_weigt
        self.__button_height = button_height
        self.__set_buttons()

    def __set_buttons(self) -> None:
        for button in self.__buttons:
            button.setFixedSize(self.__button_width, self.__button_height)
            self.addWidget(button)
