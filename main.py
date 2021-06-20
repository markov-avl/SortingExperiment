import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication

from actions.clear import Clear
from actions.exit import Exit
from actions.experiment import Experiment
from actions.generate import Generate
from actions.show_comparisons import ShowComparisons
from actions.show_permutations import ShowPermutations
from actions.show_time import ShowTime
from toolbar.toolbar import Toolbar
from widgets.barchart import BarChart
from windows.get_files import GetFilesWindow
from windows.experiment import ExperimentWindow
from windows.generate import GenerateWindow


def no_action(*args, **kwargs) -> None:
    pass


class SortingExperiment(QMainWindow):
    _on_experiment_ended = pyqtSignal(dict)
    _generate_window: GenerateWindow = None
    _get_files_window: GetFilesWindow = None
    _experiment_window: ExperimentWindow = None
    _experiment_files: list
    _experiment_results = dict()

    def __init__(self) -> None:
        super().__init__()
        # window parameters
        self.__min_width = 840
        self.__min_height = 480
        # menubar
        self.__menu_bar = self.menuBar()
        self.__file_menu = self.__menu_bar.addMenu('&Файл')
        self.__run_menu = self.__menu_bar.addMenu('&Выполнить')
        self.__bar_chart_menu = self.__menu_bar.addMenu('&Гистограмма')
        self.__help_menu = self.__menu_bar.addMenu('&Справка')
        # toolbar
        self.__toolbar = Toolbar()
        # widgets
        self.__bar_chart = BarChart()
        # actions
        self.__clear_action = Clear(self.__clear)
        self.__exit_action = Exit(self.close)
        self.__generate_action = Generate(self._create_generate_window)
        self.__experiment_action = Experiment(self._create_get_files_window)
        self.__show_permutations_action = ShowPermutations(self.__show_experiment_permutations)
        self.__show_comparisons_action = ShowComparisons(self.__show_experiment_comparisons)
        self.__show_time_action = ShowTime(self.__show_experiment_time)
        # objects
        self.__active_experiment = None
        # signals
        self._on_experiment_ended.connect(self.__show_experiment_results)
        self.__init_ui()

    def __set_menu_bar(self) -> None:
        self.__file_menu.addAction(self.__clear_action)
        self.__file_menu.addSeparator()
        self.__file_menu.addAction(self.__exit_action)
        self.__run_menu.addAction(self.__generate_action)
        self.__run_menu.addAction(self.__experiment_action)
        self.__bar_chart_menu.addAction(self.__show_permutations_action)
        self.__bar_chart_menu.addAction(self.__show_comparisons_action)
        self.__bar_chart_menu.addAction(self.__show_time_action)

    def __set_toolbar(self) -> None:
        self.__toolbar.addAction(self.__generate_action)
        self.__toolbar.addAction(self.__experiment_action)
        self.__toolbar.addSeparator()
        self.__toolbar.addAction(self.__show_permutations_action)
        self.__toolbar.addAction(self.__show_comparisons_action)
        self.__toolbar.addAction(self.__show_time_action)
        self.addToolBar(Qt.TopToolBarArea, self.__toolbar)

    def __set_status_bar(self) -> None:
        self.statusBar().setStyleSheet('QStatusBar::item {border: None;}')

    def __set_main_widget(self) -> None:
        self.setCentralWidget(self.__bar_chart)

    def __set_active_bar_chart(self) -> None:
        self.__show_permutations_action.setEnabled(True)
        self.__show_comparisons_action.setEnabled(True)
        self.__show_time_action.setEnabled(True)

    def __set_inactive_bar_chart(self) -> None:
        self.__show_permutations_action.setEnabled(False)
        self.__show_comparisons_action.setEnabled(False)
        self.__show_time_action.setEnabled(False)

    def _create_generate_window(self) -> None:
        if self._generate_window is not None:
            if self._generate_window.isVisible():
                # TODO: переключение на окно
                return
            else:
                del self._generate_window
        if self._generate_window is None:
            self._generate_window = GenerateWindow()
            self._generate_window.show()

    def _create_get_files_window(self) -> None:
        if self._get_files_window is not None:
            if self._get_files_window.isVisible():
                # TODO: переключение на окно
                return
            else:
                del self._get_files_window
        if self._experiment_window is not None:
            if self._experiment_window.isVisible():
                # TODO: переключение на окно
                return
            else:
                del self._experiment_window
        if self._get_files_window is None and self._experiment_window is None:
            self._get_files_window = GetFilesWindow()
            if len(self._get_files_window.files):
                self._create_experiment_window(self._get_files_window.files.copy())

    def _create_experiment_window(self, files: list) -> None:
        self._experiment_window = ExperimentWindow(files, self._on_experiment_ended)
        self._experiment_window.show()
        self._experiment_window.experiment()

    def __clear(self):
        self.__bar_chart.clear()
        self.__set_inactive_bar_chart()
        self.__active_experiment = None

    def _get_values(self, key) -> dict:
        return {i: self._experiment_results[i][key] for i in self._experiment_results}

    def __show_experiment_permutations(self) -> None:
        if self.__active_experiment is not ShowPermutations:
            self.__bar_chart.set_bars('Перестановки', self._experiment_files, **self._get_values('permutations'))
            self.__active_experiment = ShowPermutations

    def __show_experiment_comparisons(self) -> None:
        if self.__active_experiment is not ShowComparisons:
            self.__bar_chart.set_bars('Сравнения', self._experiment_files, **self._get_values('comparisons'))
            self.__active_experiment = ShowComparisons

    def __show_experiment_time(self) -> None:
        if self.__active_experiment is not ShowTime:
            self.__bar_chart.set_bars('Время', self._experiment_files, **self._get_values('time'))
            self.__active_experiment = ShowTime

    def __show_experiment_results(self, results: dict) -> None:
        self._experiment_results = results
        self._experiment_files = [file[file.rfind('/') + 1:] for file in self._get_files_window.files]
        self._experiment_window.close()
        del self._get_files_window
        del self._experiment_window
        self.__active_experiment = None
        self.__set_active_bar_chart()
        self.__show_experiment_permutations()

    def __init_ui(self) -> None:
        self.setGeometry(150, 150, self.__min_width, self.__min_height)
        self.setMinimumWidth(self.__min_width)
        self.setMinimumHeight(self.__min_height)
        self.setWindowTitle('Sorting Experiment')
        self.setWindowIcon(QIcon('icons/main.png'))
        self.addToolBar(Qt.TopToolBarArea, self.__toolbar)
        self.__set_menu_bar()
        self.__set_toolbar()
        self.__set_status_bar()
        self.__set_main_widget()
        self.__set_inactive_bar_chart()
        self.show()

    def close(self) -> bool:
        if self._generate_window is not None:
            self._generate_window.close()
        return super().close()

    def closeEvent(self, a0: QCloseEvent) -> None:
        if self._generate_window is not None:
            self._generate_window.close()
        a0.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SortingExperiment()
    sys.exit(app.exec_())
