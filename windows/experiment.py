from PyQt5.QtWidgets import QFileDialog


class ExperimentWindow(QFileDialog):
    OPEN_FILE = 'Выберите файлы для эксперимента'
    DEFAULT_DIRECTORY = './'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('font-size: 12pt;')
        self.files = self.getOpenFileNames(parent, self.OPEN_FILE, self.DEFAULT_DIRECTORY)[0]
