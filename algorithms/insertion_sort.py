from algorithms.counter import Counter


class InsertionSort(Counter):
    @staticmethod
    def insertion_sort(array: list, start: int = 0, end: int = 0) -> list:
        end = end or len(array)
        for i in range(start, end):
            temp_index, temp_index_value = i, array[i]
            while temp_index != start and temp_index_value < array[temp_index - 1]:
                array[temp_index] = array[temp_index - 1]
                temp_index -= 1
            array[temp_index] = temp_index_value
        return array

    def _insertion_sort(self, array: list, start: int = 0, end: int = 0) -> list:
        end = end or len(array)
        for i in range(start, end):
            temp_index, temp_index_value = i, array[i]
            while temp_index != start and temp_index_value < array[temp_index - 1]:
                self._comparisons += 1
                array[temp_index] = array[temp_index - 1]
                self._permutations += 1
                temp_index -= 1
            self._comparisons += 1
            array[temp_index] = temp_index_value
            self._permutations += 1
        return array

    def sort(self, sequence: list, counting: bool = True) -> list:
        self._prepare(counting)
        sequence = self._insertion_sort(sequence) if counting else self.insertion_sort(sequence)
        self._end()
        return sequence
