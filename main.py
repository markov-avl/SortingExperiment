import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from actions.clear import Clear
from actions.exit import Exit
from actions.experiment import Experiment
from actions.generate import Generate
from widgets.graph import Graph, generate, experiment


class CourseWork(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # window parameters
        self.__min_width = 640
        self.__min_height = 360
        # menubar
        self.__menu_bar = self.menuBar()
        self.__file_menu = self.__menu_bar.addMenu('&Файл')
        self.__run_menu = self.__menu_bar.addMenu('&Выполнить')
        self.__help_menu = self.__menu_bar.addMenu('&Справка')
        # widgets
        self.__graph_widget = Graph()
        # actions
        self.__clear_action = Clear(self.__graph_widget.clear)
        self.__exit_action = Exit(self.close)
        self.__generate_action = Generate(generate)
        self.__experiment_action = Experiment(experiment)
        # buttons
        self.init_ui()

    def __set_menu_bar(self) -> None:
        self.__file_menu.addAction(self.__clear_action)
        self.__file_menu.addSeparator()
        self.__file_menu.addAction(self.__exit_action)
        self.__run_menu.addAction(self.__generate_action)
        self.__run_menu.addAction(self.__experiment_action)

    def __set_main_widget(self) -> None:
        self.setCentralWidget(self.__graph_widget)

    def init_ui(self) -> None:
        self.setGeometry(150, 150, self.__min_width, self.__min_height)
        self.setMinimumWidth(self.__min_width)
        self.setMinimumHeight(self.__min_height)
        self.setWindowTitle('Sorting Experiment')
        self.setWindowIcon(QIcon('icons/main.png'))
        self.__set_menu_bar()
        self.__set_main_widget()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CourseWork()
    sys.exit(app.exec_())
