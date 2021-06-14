from PyQt5.QtWidgets import QToolBar


def no_action(*args, **kwargs) -> None:
    pass


class Toolbar(QToolBar):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setVisible(True)
        self.setMovable(False)
        self.contextMenuEvent = no_action
