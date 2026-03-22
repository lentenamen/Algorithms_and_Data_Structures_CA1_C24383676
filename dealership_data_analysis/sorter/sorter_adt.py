from abc import ABC, abstractmethod
class Sorter(ABC):
    """
    Abstract Data Type: Sorter
    Defines the interface for sorting
    algorithms.
    Concrete subclasses must implement the
    sort method.
    """
    @abstractmethod
    def sort(self, data: list, key=lambda x: x) -> list:
        """
        Sorts the given data using the provided
        key function.
        :param data: List of elements to sort
        :param key: Function that extracts
        comparison value
        :return: New sorted list
        """
        pass