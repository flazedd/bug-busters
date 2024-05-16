package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Test_OpMatcher_Phi {
	@Test
    public void testMatchTemplateBegin() {
        String textWithTemplateBegin = "@template_begin(name1, param2, param3)";
        String[] expectedNames = new String[]{"name1", "param2", "param3"};
        String[] actualNames = OpMatcher.matchTemplateBegin(textWithTemplateBegin);
        assertArrayEquals(expectedNames, actualNames);
    }

}