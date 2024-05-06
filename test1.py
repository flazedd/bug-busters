import constant

r = """"
package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class OpMatcherTest_EvoSuite {

    @Test
    public void test0()  throws Throwable  {
        OpMatcher opMatcher0 = new OpMatcher();
        assertNotNull(opMatcher0);
"""


def get_imports(package, test_name):
    with open('JavaProgramUnderTest/lib/src/test/java/' + package + '/' + test_name + '.java', 'r') as java_test_file:
        # Read the contents of the file
        contents = java_test_file.read()
        result = ""
        s2 = 0
        while True:
            s1 = contents.find('import', s2)
            if s1 == -1:
                break
            s2 = contents.find('\n', s1)
            if s2 == -1:
                with constant.PRINT_LOCK:
                    print('Could not find newline after import was found')
            result += contents[s1:s2] + '\n'
        return result


k = get_imports('a4j_2', 'DirectorsTest_EvoSuite')
print(k)