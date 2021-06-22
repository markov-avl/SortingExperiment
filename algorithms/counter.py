from abc import abstractmethod, ABC
from time import time


class Counter(ABC):
    _permutations = -1
    _comparisons = -1
    _time = -1.0

    @property
    def permutations(self) -> int:
        return self._permutations

    @property
    def comparisons(self) -> int:
        return self._comparisons

    @property
    def time(self) -> float:
        return self._time

    def prepare(self, counting: bool = True) -> None:
        self._permutations = 0 if counting else -1
        self._comparisons = 0 if counting else -1
        self._time = time()

    def end(self) -> None:
        self._time = time() - self._time

    @abstractmethod
    def sort(self, sequence: list, counting: bool = True) -> list:
        pass
