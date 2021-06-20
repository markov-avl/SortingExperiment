from PyQt5.QtCore import Qt, pyqtSignal, pyqtBoundSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from animations.loading import LoadingAnimation
from buttons.cancel import CancelButton
from experimenter.experimenter import Experimenter

STYLESHEET = 'font-size: 8pt;'


class ExperimentWindow(QWidget):
    _state_changed = pyqtSignal(str)

    def __init__(self, files: list, on_experiment_ended: pyqtBoundSignal, parent=None):
        super().__init__(parent)
        self._files = files
        self._state = QLabel()
        self._cancel = CancelButton(self.close)
        self._loading = LoadingAnimation()
        self._upper_layout = QHBoxLayout()
        self._main_layout = QVBoxLayout()
        self._state_changed.connect(self.set_state)
        self._experimenter = Experimenter(self._files, self._state_changed, on_experiment_ended)
        self._init_ui()

    def _set_layouts(self) -> None:
        self._upper_layout.addWidget(self._loading, 0, alignment=Qt.AlignLeft)
        self._upper_layout.addWidget(self._state, 1, alignment=Qt.AlignLeft)
        self._main_layout.addLayout(self._upper_layout)
        self._main_layout.addWidget(self._cancel, alignment=Qt.AlignRight)

    def _set_state(self) -> None:
        self._state.setWordWrap(True)
        self._state.setStyleSheet(STYLESHEET)

    def _init_ui(self) -> None:
        self._set_state()
        self._set_layouts()
        self.setWindowTitle('Эксперимент')
        self.setFixedSize(250, 120)
        self.setWindowIcon(QIcon('icons/experiment.png'))
        self.setLayout(self._main_layout)

    def start_loading(self) -> None:
        self._loading.start()

    def stop_loading(self) -> None:
        self._loading.stop()

    def set_state(self, state: str) -> None:
        self._state.setText(state)

    def experiment(self) -> None:
        self._loading.start()
        self._experimenter.start()

    def close(self) -> None:
        if self._experimenter.isRunning():
            self._experimenter.terminate()
        self._loading.stop()
        super().close()
