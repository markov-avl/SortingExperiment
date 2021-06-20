from PyQt5.QtCore import QThread, pyqtBoundSignal

from algorithms.heap_sort import HeapSort
from algorithms.intro_sort import IntroSort


class Experimenter(QThread):
    __results: dict

    def __init__(self, files: list = None, on_state_changed: pyqtBoundSignal = None,
                 on_experiment_ended: pyqtBoundSignal = None, parent=None) -> None:
        super().__init__(parent)
        self._algorithms = {
            'Heapsort': HeapSort(),
            'Introsort (log2(n)-depth)': IntroSort(2),
            'Introsort (log3(n)-depth)': IntroSort(3)
        }
        self._counters = ('permutations', 'comparisons', 'time')
        self.__files = files
        self.__on_state_changed = on_state_changed
        self.__on_experiment_ended = on_experiment_ended

    @property
    def results(self) -> dict:
        return self.__results

    def _reset_results(self) -> None:
        self.__results = {i: {j: list() for j in self._counters} for i in self._algorithms}

    def _state_changed(self, state: str) -> None:
        if self.__on_state_changed is not None:
            self.__on_state_changed.emit(state)

    def _experiment_ended(self) -> None:
        if self.__on_experiment_ended is not None:
            self.__on_experiment_ended.emit(self.__results)

    def set_files(self, files: list) -> None:
        self.__files = files

    def set_on_state_changed(self, on_state_changed: pyqtBoundSignal) -> None:
        self.__on_state_changed = on_state_changed

    def set_on_experiment_ended(self, on_experiment_ended: pyqtBoundSignal) -> None:
        self.__on_experiment_ended = on_experiment_ended

    def run(self) -> None:
        self.experiment()

    def experiment(self) -> None:
        self._reset_results()
        for file in self.__files:
            file_ = file[file.rfind('/') + 1:]
            self._state_changed(f'Чтение файла {file_}')
            sequence = self.get_sequence(file)
            for algorithm in self._algorithms:
                self._state_changed(f'Сортировка: {algorithm}\n'
                                    f'Файл: {file_}\n'
                                    f'Эксперимент: подсчет перестановок и сравнений')
                self._algorithms[algorithm].sort(sequence, True)
                self.__results[algorithm]['permutations'].append(self._algorithms[algorithm].permutations)
                self.__results[algorithm]['comparisons'].append(self._algorithms[algorithm].comparisons)
                self._state_changed(f'Сортировка: {algorithm}\n'
                                    f'Файл: {file_}\n'
                                    f'Эксперимент: подсчет времени')
                self._algorithms[algorithm].sort(sequence, False)
                self.__results[algorithm]['time'].append(self._algorithms[algorithm].time)
        self._experiment_ended()

    @staticmethod
    def get_sequence(file: str) -> list:
        with open(file, 'r') as infile:
            return list(map(int, infile.read().split(' ')))
