from math import ceil, log

from algorithms.counter import Counter
from algorithms.heap_sort import HeapSort
from algorithms.insertion_sort import InsertionSort


class IntroSort(Counter):
    def __init__(self, log_multiplier: int = 2) -> None:
        self._heap_sort = HeapSort()
        self._insertion_sort = InsertionSort()
        self._size_threshold = 16
        self._log_multiplier = log_multiplier

    @staticmethod
    def median_of_3(array: list, first: int, middle: int, last: int) -> int:
        if (array[first] > array[middle]) != (array[first] > array[last]):
            return array[first]
        elif (array[middle] > array[first]) != (array[middle] > array[last]):
            return array[middle]
        return array[last]

    @staticmethod
    def partition(array: list, low: int, high: int, pivot: int) -> int:
        i, j = low, high
        while True:
            while array[i] < pivot:
                i += 1
            j -= 1
            while pivot < array[j]:
                j -= 1
            if i >= j:
                return i
            array[i], array[j] = array[j], array[i]
            i += 1

    @staticmethod
    def intro_sort(array: list, start: int, end: int, size_threshold: int, max_depth: int) -> list:
        while end - start > size_threshold:
            if max_depth == 0:
                return HeapSort.heapsort(array)
            max_depth -= 1
            pivot = IntroSort.median_of_3(array, start, start + ((end - start) // 2) + 1, end - 1)
            p = IntroSort.partition(array, start, end, pivot)
            IntroSort.intro_sort(array, p, end, size_threshold, max_depth)
            end = p
        return InsertionSort.insertion_sort(array, start, end)

    @staticmethod
    def introsort(array: list, log_multiplier: int = 2) -> list:
        n = len(array)
        if n == 0:
            return array
        max_depth = log_multiplier * ceil(log(n))
        return IntroSort.intro_sort(array, 0, n, 16, max_depth)

    def _median_of_3(self, array: list, first: int, middle: int, last: int) -> int:
        if (array[first] > array[middle]) != (array[first] > array[last]):
            self._comparisons += 1
            return array[first]
        elif (array[middle] > array[first]) != (array[middle] > array[last]):
            self._comparisons += 2
            return array[middle]
        self._comparisons += 2
        return array[last]

    def _partition(self, array: list, low: int, high: int, pivot: int) -> int:
        k: int
        i, j = low, high
        while True:
            k = i
            while array[i] < pivot:
                i += 1
            self._comparisons += i - k + 1
            j -= 1
            k = j
            while pivot < array[j]:
                j -= 1
            self._comparisons += k - j + 1
            if i >= j:
                return i
            array[i], array[j] = array[j], array[i]
            self._permutations += 1
            i += 1

    def _intro_sort(self, array: list, start: int, end: int, max_depth: int) -> list:
        while end - start > self._size_threshold:
            if max_depth == 0:
                return self._heap_sort._heapsort(array)
            max_depth -= 1
            pivot = self._median_of_3(array, start, start + ((end - start) // 2) + 1, end - 1)
            p = self._partition(array, start, end, pivot)
            self._intro_sort(array, p, end, max_depth)
            end = p
        return self._insertion_sort._insertion_sort(array, start, end)

    def _introsort(self, array: list) -> list:
        n = len(array)
        if n == 0:
            return array
        max_depth = self._log_multiplier * ceil(log(n))
        return self._intro_sort(array, 0, n, max_depth)

    def sort(self, sequence: list, counting: bool = True) -> list:
        self._heap_sort.prepare(counting)
        self._insertion_sort.prepare(counting)
        self.prepare(counting)
        sequence = self._introsort(sequence) if counting else self.introsort(sequence, self._log_multiplier)
        self.end()
        if counting:
            self._permutations += self._heap_sort.permutations + self._insertion_sort.permutations
            self._comparisons += self._heap_sort.comparisons + self._insertion_sort.comparisons
        return sequence
