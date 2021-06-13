from math import ceil, log2

from algorithms.sort import Sort
from heap_sort import HeapSort
from insertion_sort import InsertionSort


class IntroSort(Sort):
    _heap_sort = HeapSort()
    _insertion_sort = InsertionSort()
    __size_threshold = 16
    __max_depth: int

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

    def _sort(self, array: list, start: int, end: int) -> list:
        while end - start > self.__size_threshold:
            if self.__max_depth == 0:
                return self._heap_sort.sort(array)
            self.__max_depth -= 1
            pivot = self.median_of_3(array, start, start + ((end - start) // 2) + 1, end - 1)
            p = self.partition(array, start, end, pivot)
            self._sort(array, p, end)
            end = p
        return self._insertion_sort.sort(array, start, end)

    def sort(self, array: list) -> list:
        n = len(array)
        if n == 0:
            return array
        self.__max_depth = 2 * ceil(log2(n))
        return self._sort(array, 0, n)
