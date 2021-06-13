from PyQt5.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


def generate(self, *args):
    print('generate')


def experiment(self, *args):
    print('experiment')


NavigationToolbar.toolitems = (
    ('Вернуться', 'Вернуться к первоначальному виду', 'home', 'home'),
    ('Назад', 'Вернуть прошлый вид', 'back', 'back'),
    ('Вперед', 'Вернуть следующий вид', 'forward', 'forward'),
    (None, None, None, None),
    ('Панорамирование', 'Панорамирование осей левой мышью, масштабирование правой', 'move', 'pan'),
    ('Увеличить', 'Увеличить вид', 'zoom_to_rect', 'zoom'),
    (None, None, None, None),
    ('Сохранить', 'Сохранить график', 'filesave', 'save_figure'),
    (None, None, None, None),
    ('Сгенерировать', 'Сгенерировать тесты', 'generate', 'generate'),
    ('Эксперимент', 'Провести эксперимент', 'experiment', 'experiment')
)
NavigationToolbar.generate = generate
NavigationToolbar.experiment = experiment


class Graph(QWidget):
    def __init__(self, width: int = 1, height: int = 1, dpi: int = 100, parent=None) -> None:
        super().__init__(parent)
        self.__canvas = Figure(figsize=(width, height), dpi=dpi)
        self.__graph = FigureCanvas(self.__canvas)
        self.__toolbar = NavigationToolbar(self.__graph, self)
        self.__layout = QVBoxLayout()
        self.__init_ui()

    def __set_graph(self) -> None:
        self.__graph.axes = self.__canvas.add_subplot(111)

    def __set_toolbar(self) -> None:
        pass

    def __set_layout(self) -> None:
        self.__layout.addWidget(self.__toolbar)
        self.__layout.addWidget(self.__graph)

    def __init_ui(self) -> None:
        self.__set_graph()
        self.__set_toolbar()
        self.__set_layout()
        self.setLayout(self.__layout)

    def add_values(self, horisontal: list, vertical: list) -> None:
        self.__graph.axes.plot(horisontal, vertical)
        self.__graph.draw()

    def set_values(self, horisontal: list, vertical: list) -> None:
        self.__graph.axes.clear()
        self.add_values(horisontal, vertical)

    def clear(self) -> None:
        self.__graph.axes.clear()
        self.__toolbar.update()
        self.__graph.draw()
