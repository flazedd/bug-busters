# from utility import utils
#
#
# class Test:
#     def __init__(self, folder, class_name):
#         self.folder = folder
#         self.target = class_name + 'Test_LLM'
#         self.begin_template = (
#                 "package " + folder + ";\n" +
#                 "import org.junit.jupiter.api.Test;\n" +
#                 "import static org.junit.jupiter.api.Assertions.*;\n" +
#                 utils.get_imports(folder, class_name) +
#                 "public class " + self.target + " {\n"
#         )
#         self.end_template = "}"
#         self.classname = class_name
#         # self.benchmark_tests = self.get_benchmark_tests()
#         self.tests = []
#
#     def test_extractor(self, java_code):
#         start_index = java_code.find("@Test")
#         begin = java_code[start_index:]
#         last_brace_index = begin.rfind('}')
#         return '\t' + begin[:last_brace_index] + begin[last_brace_index + 1:]
#
#     def get_benchmark_tests(self):
#         with (open('JavaProgramUnderTest/lib/src/test/java/' + self.folder + '/' + self.classname + 'Test_EvoSuite.java',
#                    'r')
#               as java_file):
#             # Read the contents of the file
#             java_code = java_file.read()
#             # print(f'Java code found: {java_code}')
#             return self.test_extractor(java_code)
#
#     def get_contents(self):
#         result = self.begin_template
#         # result += self.benchmark_tests
#         # print(self.tests)
#         for test in self.tests:
#             result += test
#             result += "\n"
#         result += self.end_template
#         return result
#
#     def write(self):
#         code = self.get_contents()
#         # improved_test = self.classname + "_LLM"
#         utils.write_code(self.folder, self.target, code)
#
#     def add_test(self, t):
#         self.tests.append(t)
#
#     def replace_last_test(self, t):
#         self.tests[-1] = t
#
#     def remove_last_test(self):
#         self.tests.pop()
