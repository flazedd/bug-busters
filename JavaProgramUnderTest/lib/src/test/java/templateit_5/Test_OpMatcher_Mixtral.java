package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Test_OpMatcher_Mixtral {
	@Test
    public void testMatchTemplateBegin() {
        String input = "@template_begin(name, param1, param2) some content here...";
        String[] expected = {"name", "param1", "param2"};
        assertArrayEquals(expected, OpMatcher.matchTemplateBegin(input));
    }
	@Test
    public void testMatchTemplateEnd() {
        String input = "some content here... @template_end or @tend";
        assertTrue(OpMatcher.matchTemplateEnd(input));
    }
}