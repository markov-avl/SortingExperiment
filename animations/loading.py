from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel


class LoadingAnimation(QLabel):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._loading = QMovie('gif/loading.gif')
        self._loading.setScaledSize(QSize(30, 30))
        self.setMovie(self._loading)

    def start(self) -> None:
        self._loading.start()

    def stop(self) -> None:
        self._loading.stop()
