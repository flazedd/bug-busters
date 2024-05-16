package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Test_OpMatcher_gemma {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name", "param1", "param2"}, names);
}

@Test
public void testMatchTemplateName() {
    String text = "templateName";
    boolean result = OpMatcher.matchTemplateName(text);
    assertTrue(result);
}

}