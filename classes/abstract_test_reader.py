from abc import ABC, abstractmethod


class ReaderTestImplementation(ABC):

    @abstractmethod
    def __init__(self, folder, oracle, test_name):
        pass

    @abstractmethod
    def partial_write(self, amount: int) -> None:
        pass

    @abstractmethod
    def amount_of_tests(self) -> int:
        pass
