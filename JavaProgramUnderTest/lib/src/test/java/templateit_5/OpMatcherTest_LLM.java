package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class OpMatcherTest_LLM {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2, param3)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name", "param1", "param2", "param3"}, result);
}

}