from algorithms.sort import Sort


class HeapSort(Sort):
    @staticmethod
    def heapify(unsorted: list, index: int, heap_size: int) -> None:
        largest, left_index, right_index = index, 2 * index + 1, 2 * index + 2
        if left_index < heap_size and unsorted[right_index] > unsorted[largest]:
            largest = left_index
        if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
            largest = right_index
        if largest != index:
            unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
            HeapSort.heapify(unsorted, largest, heap_size)

    @staticmethod
    def sort(unsorted: list) -> list:
        n = len(unsorted)
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(unsorted, i, n)
        for i in range(n - 1, 0, -1):
            unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
            HeapSort.heapify(unsorted, 0, i)
        return unsorted
