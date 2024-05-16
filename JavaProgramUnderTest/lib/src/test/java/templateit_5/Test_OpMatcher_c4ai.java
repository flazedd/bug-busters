package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Test_OpMatcher_c4ai {
@Test
    public void testMatchTemplateBegin() {
        String input = "@template_begin(header, title, author)";
        String[] expected = {"header", "title", "author"};
        String[] actual = OpMatcher.matchTemplateBegin(input);
        assertArrayEquals(expected, actual);
    }

@Test
    public void testMatchTemplateBeginWithTbegin() {
        String input = "@tbegin(footer, copyright, year)";
        String[] expected = {"footer", "copyright", "year"};
        String[] actual = OpMatcher.matchTemplateBegin(input);
        assertArrayEquals(expected, actual);
    }

}