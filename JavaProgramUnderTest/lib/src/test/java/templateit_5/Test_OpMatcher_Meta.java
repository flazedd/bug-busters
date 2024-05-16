package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Test_OpMatcher_Meta {
	@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2, param3)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name", "param1", "param2", "param3"}, result);
}
	@Test
public void testMatchTemplateName() {
    String text = "validTemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}
}