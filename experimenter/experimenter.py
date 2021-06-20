from algorithms.heap_sort import HeapSort
from algorithms.intro_sort import IntroSort


class Experimenter:
    def __init__(self) -> None:
        self._algorithms = {
            'Heapsort': HeapSort(),
            'Introsort (log2(n)-depth)': IntroSort(2),
            'Introsort (log3(n)-depth)': IntroSort(3)
        }
        self._counters = ('permutations', 'comparisons', 'time')

    def _get_results(self) -> dict:
        return {i: {j: list() for j in self._counters} for i in self._algorithms}

    @staticmethod
    def get_sequence(file: str) -> list:
        with open(file, 'r') as infile:
            return list(map(int, infile.read()[1: -1].split(', ')))

    def experiment(self, files: list) -> dict:
        results = self._get_results()
        for file in files:
            sequence = self.get_sequence(file)
            for algorithm in self._algorithms:
                self._algorithms[algorithm].sort(sequence, False)
                for counter in self._counters:
                    results[algorithm][counter].append(eval(f'self._algorithms[algorithm].{counter}'))
        return results
