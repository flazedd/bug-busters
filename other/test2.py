kk = """
INTERNALERROR>     raise exception.with_traceback(exception.__traceback__)
INTERNALERROR>   FDocumenError' in report.longrepr.reprcrash.message:
INTERNALERROR> AttributeError: 'str' object has no attribute 'reprcrash'
[*] Start mutation process:
   - targets: PythonPUT/codetiming/timers.py
   - tests: PythonPUT/codetiming/test_timers.py
[*] 5 tests passed:
   - test__timers [0.32722 s]
[*] Start mutants generation and execution:
   - [#   1] ASR _timers: [0.14658 s] survived
   - [#   2] COI _timers: [0.14077 s] survived
   - [#   3] COI _timers: [0.12500 s] survived
   - [#   4] COI _timers: [0.05618 s] survived
   - [#   5] COI _timers: [0.11743 s] killed by PythonPUT/codetiming/test_timers.py::test_case_5
   - [#   6] COI _timers: [0.10652 s] killed by PythonPUT/codetiming/test_timers.py::test_case_5
   - [#   7] IOD _timers: [0.12158 s] killed by PythonPUT/codetiming/test_timers.py::test_case_5
   - [#   8] IOD _timers: [0.14316 s] survived
   - [#   9] IOD _timers: [0.06563 s] survived
   - [#  10] IOP _timers: [0.15868 s] survived
   - [#  11] LCR _timers: [0.14151 s] survived
   - [#  12] LCR _timers: [0.12956 s] killed by PythonPUT/codetiming/test_timers.py::test_case_11
   - [#  13] LCR _timers: [0.12337 s] killed by PythonPUT/codetiming/test_timers.py::test_case_10
   - [#  14] LCR _timers: [0.14096 s] killed by PythonPUT/codetiming/test_timers.py::test_case_11
   - [#  15] ROR _timers: [0.13951 s] killed by PythonPUT/codetiming/test_timers.py::test_case_5
   - [#  16] ROR _timers: [0.15363 s] survived
   - [#  17] SCD _timers: [0.06935 s] killed by PythonPUT/codetiming/test_timers.py::test_case_0
   - [#  18] SCI _timers: [0.15569 s] survived
   - [#  19] SCI _timers: [0.14162 s] survived
[*] Mutation score [2.91665 s]: 00.89%
   - all: 19
   - killed: 8 (42.1%)
   - survived: 11 (57.9%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
"""


def find_numbers_before_percent(string):
    i = -1
    while True:
        if string[i] == '%':
            i -= 1
            break
        i -= 1
    dot_seen = False
    numbers = ''
    while True:
        if string[i].isdigit():
            numbers = string[i] + numbers
        elif string[i] == '.' and not dot_seen:
            dot_seen = True
            numbers = string[i] + numbers
        else:
            break
        i -= 1
    return float(numbers) if numbers else None

def get_statistics(terminal_output):
    start = terminal_output.find("[*] Mutation score [")
    end = terminal_output.find("- all:", start)
    target = terminal_output[start:end]
    return find_numbers_before_percent(target)

print(get_statistics(kk))