import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar

from actions.clear import Clear
from actions.exit import Exit
from actions.experiment import Experiment
from actions.generate import Generate
from actions.show_comparisons import ShowComparisons
from actions.show_permutations import ShowPermutations
from actions.show_time import ShowTime
from widgets.barchart import BarChart


def no_action(*args, **kwargs) -> None:
    pass


class SortingExperiment(QMainWindow):
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
        self.__toolbar = QToolBar()
        # widgets
        self.__bar_chart = BarChart()
        # actions
        self.__clear_action = Clear(self.__bar_chart.clear)
        self.__exit_action = Exit(self.close)
        self.__generate_action = Generate(no_action)                   # TODO
        self.__experiment_action = Experiment(no_action)               # TODO
        self.__show_permutations_action = ShowPermutations(no_action)  # TODO
        self.__show_comparisons_action = ShowComparisons(no_action)    # TODO
        self.__show_time_action = ShowTime(no_action)                  # TODO
        self.init_ui()

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
        self.__toolbar.setVisible(True)
        self.__toolbar.setMovable(False)
        self.__toolbar.contextMenuEvent = no_action
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

    def init_ui(self) -> None:
        self.setGeometry(150, 150, self.__min_width, self.__min_height)
        self.setMinimumWidth(self.__min_width)
        self.setMinimumHeight(self.__min_height)
        self.setWindowTitle('Sorting Experiment')
        self.setWindowIcon(QIcon('icons/main.png'))
        self.__set_menu_bar()
        self.__set_toolbar()
        self.__set_status_bar()
        self.__set_main_widget()
        self.__set_inactive_bar_chart()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SortingExperiment()
    sys.exit(app.exec_())
