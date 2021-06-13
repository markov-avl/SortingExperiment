from algorithms.sort import Sort


class InsertionSort(Sort):
    @staticmethod
    def sort(array: list[any], start: int = 0, end: int = 0) -> list:
        end = end or len(array)
        for i in range(start, end):
            temp_index, temp_index_value = i, array[i]
            while temp_index != start and temp_index_value < array[temp_index - 1]:
                array[temp_index] = array[temp_index - 1]
                temp_index -= 1
            array[temp_index] = temp_index_value
        return array
