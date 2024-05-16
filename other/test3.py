sk = """
```java
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TemplateParserTest {

    @Test
    public void testExtractParameterName() {
        String text = "This is a #sample text with a parameter #123 and another #Sample2";
        String parameterName = TemplateParser.extractParameterName(text);
        assertNotNull("Parameter name should not be null", parameterName);
        assertEquals("First parameter name should be 'sample'", "sample", parameterName);
    }

    private static class TemplateParser {
        public static String extractParameterName(String text) {
            Pattern pattern = Pattern.compile("#(\\p{Alpha}\\w*)");
            Matcher matcher = pattern.matcher(text);
            if (matcher.find()) {
                return matcher.group(1);
            }
            return null;
        }
    }

```
kankerrrr
"""


def get_codek(ai_output):
    start = ai_output.find('```java')
    if start == -1:
        print('[+] begin java code not found')
        return None
    begin = ai_output.find("@Test")
    if begin == -1:
        return None  # @Test not found

    counter = 0
    end = begin

    for char in ai_output[begin:]:
        if char == "{":
            counter += 1
        elif char == "}":
            counter -= 1

        if counter < 0 or char == '`':
            return '\t' + ai_output[begin:end]

        end += 1

    return '\t' + ai_output[begin:end]


print(get_codek(sk))