from abc import ABC, abstractmethod

class LanguageImplementation(ABC):
    @abstractmethod
    def get_code(self, ai_output):
        pass

    @abstractmethod
    def get_args(self):
        pass

    @abstractmethod
    def get_mutation_score(self, folder, file_name, test_name):
        pass

    @abstractmethod
    def get_dict(self) -> dict:
        pass

    @abstractmethod
    def write_code(self, package, test_name, code):
        pass

    @abstractmethod
    def exec_test(self, package, test_name, test_string):
        pass

    @abstractmethod
    def did_test_fail(self, output):
        pass

    @abstractmethod
    def get_test_errors(self, output, test_name_improved):
        pass

    @abstractmethod
    def get_imports(self, package, class_name):
        pass

    @abstractmethod
    def get_prompt(self, package, class_name):
        pass

    @abstractmethod
    def get_test_instance(self, folder, class_name, test_name):
        pass

    @abstractmethod
    def create_file(self, folder, class_name, ai_model):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def work_already_satisfied(self, folder, class_name, ai_model):
        pass

    @abstractmethod
    def generate_sbst_tool(self, folder, class_name):
        pass



