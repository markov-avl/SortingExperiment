from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarCategoryAxis, QValueAxis, QBarSeries


class BarChart(QChartView):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._chart = QChart()
        self._series = QBarSeries()
        self._axis_x = QBarCategoryAxis()
        self._axis_y = QValueAxis()
        self.__init_ui()

    def __set_chart(self) -> None:
        self._chart.createDefaultAxes()
        self._chart.setAxisX(self._axis_x, self._series)
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self._chart.legend().setVisible(True)
        self._chart.legend().setAlignment(Qt.AlignBottom)
        self._chart.addAxis(self._axis_x, Qt.AlignBottom)
        self._chart.addAxis(self._axis_y, Qt.AlignLeft)

    def _set_starting_state(self) -> None:
        self.set_bars('Приветствую!', [])

    def _reset(self) -> None:
        self._chart.removeAllSeries()
        self._chart.removeAxis(self._axis_x)
        self._series = QBarSeries()
        self._axis_x.clear()

    def __init_ui(self) -> None:
        self.__set_chart()
        self.setChart(self._chart)
        self.setRenderHint(QPainter.Antialiasing)
        self._set_starting_state()

    def set_bars(self, title: str, experiments: list, **kwargs) -> None:
        n = len(experiments)
        for algorithm in kwargs:
            if n != len(kwargs[algorithm]):
                break
        else:
            self._reset()
            self._chart.setTitle(title)
            if len(experiments):
                max_ = max(map(max, kwargs.values()))
                if max_ <= 0:
                    max_ = 0.1
            else:
                max_ = 100
            self._axis_y.setRange(0, max_)
            if n:
                for algorithm in kwargs:
                    algorithm_ = QBarSet(algorithm)
                    for i in kwargs[algorithm]:
                        algorithm_.append(i)
                    self._series.append(algorithm_)
                self._chart.addSeries(self._series)
                self._axis_x.append(list(map(str, experiments)))
                self._chart.addAxis(self._axis_x, Qt.AlignBottom)
                self._series.attachAxis(self._axis_x)
                self._series.attachAxis(self._axis_y)

    def clear(self) -> None:
        self.set_bars('Гистограмма очищена', [])
