from algorithms.counter import Counter


class HeapSort(Counter):
    @staticmethod
    def heapify(unsorted: list, index: int, heap_size: int) -> None:
        largest, left_index, right_index = index, 2 * index + 1, 2 * index + 2
        if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
            largest = left_index
        if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
            largest = right_index
        if largest != index:
            unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
            HeapSort.heapify(unsorted, largest, heap_size)

    @staticmethod
    def heapsort(unsorted: list) -> list:
        n = len(unsorted)
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(unsorted, i, n)
        for i in range(n - 1, 0, -1):
            unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
            HeapSort.heapify(unsorted, 0, i)
        return unsorted

    def _heapify(self, unsorted: list, index: int, heap_size: int) -> None:
        largest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
            largest = left_index
        self._comparisons += 1
        if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
            largest = right_index
        self._comparisons += 1
        if largest != index:
            unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
            self._permutations += 1
            self._heapify(unsorted, largest, heap_size)

    def _heapsort(self, unsorted: list) -> list:
        n = len(unsorted)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(unsorted, i, n)
        for i in range(n - 1, 0, -1):
            unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
            self._permutations += 1
            self._heapify(unsorted, 0, i)
        return unsorted

    def sort(self, sequence: list, counting: bool = True) -> list:
        self._prepare(counting)
        sequence = self._heapsort(sequence) if counting else self.heapsort(sequence)
        self._end()
        return sequence
