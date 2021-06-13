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

    def _set_starting_state(self) -> None:
        self.set_bars('Приветствую!', [100, 1000, 10000], [50, 9, 4], [60, 45, 4])

    def __init_ui(self) -> None:
        self.__set_chart()
        self.setChart(self._chart)
        self.setRenderHint(QPainter.Antialiasing)
        self._set_starting_state()

    def set_bars(self, title: str, count: list, heapsort_values: list, introsort_values: list) -> None:
        if len(count) == len(heapsort_values) == len(introsort_values):
            self._chart.setTitle(title)
            self._chart.removeAllSeries()
            if self._series:
                self._series.clear()
            self._axis_x.clear()
            self._axis_y.setRange(0, max(*heapsort_values, *introsort_values) if len(count) else 100)
            if len(count):
                heapsort = QBarSet('Heapsort')
                introsort = QBarSet('Introsort')
                for i in range(len(count)):
                    heapsort.append(heapsort_values[i])
                    introsort.append(introsort_values[i])
                self._series.append(heapsort)
                self._series.append(introsort)

                self._chart.addSeries(self._series)

                self._axis_x.append(list(map(str, count)))
                self._chart.addAxis(self._axis_x, Qt.AlignBottom)
                self._series.attachAxis(self._axis_x)

                self._chart.addAxis(self._axis_y, Qt.AlignLeft)
                self._series.attachAxis(self._axis_y)

    def clear(self) -> None:
        self.set_bars('Гистограмма очищена', [], [], [])
