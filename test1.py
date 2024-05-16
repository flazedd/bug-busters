



def get_signature(test_string):
    # Find the index of the first occurrence of "()"
    index = test_string.find("()")

    # Find the start index of the function name by searching backward from the index of "()"
    start_index = index
    while start_index > 0 and test_string[start_index - 1] != ' ':
        start_index -= 1

    # Extract the function name
    function_name = test_string[start_index:index].strip()

    return function_name


r = """
    @Test
    public void test4()  throws Throwable {
        String[] stringArray0 = OpMatcher.matchTemplateBegin("M=]#7L+IL");
        assertNull(stringArray0);
    }
"""

print(get_signature(r))