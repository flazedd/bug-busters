package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Test_OpMatcher_Meta {
@Test
    public void testMatchTemplateBegin() {
        String input = "@template_begin(templateName, param1, param2)";
        String[] expected = {"templateName", "param1", "param2"};

        String[] actual = OpMatcher.matchTemplateBegin(input);
        assertArrayEquals(expected, actual);
    }

@Test
    public void testMatchTemplateEnd() {
        String input = "@template_end";

        boolean actual = OpMatcher.matchTemplateEnd(input);
        boolean expected = true;

        assertEquals(expected, actual);
    }

}