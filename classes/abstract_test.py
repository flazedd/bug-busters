from abc import ABC, abstractmethod

class HandleTestImplementation(ABC):
    @abstractmethod
    def __init__(self, folder, class_name, oracle):
        pass

    @abstractmethod
    def get_contents(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def add_test(self):
        pass

    @abstractmethod
    def remove_last_test(self):
        pass

