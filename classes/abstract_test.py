from abc import ABC, abstractmethod

class HandleTestImplementation(ABC):
    @abstractmethod
    def __init__(self, folder, class_name, oracle, test_name):
        pass

    @abstractmethod
    def get_contents(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def empty_file(self):
        pass

    @abstractmethod
    def add_test(self, test):
        pass

    @abstractmethod
    def remove_last_test(self):
        pass

    @abstractmethod
    def add_imports(self, response):
        pass

