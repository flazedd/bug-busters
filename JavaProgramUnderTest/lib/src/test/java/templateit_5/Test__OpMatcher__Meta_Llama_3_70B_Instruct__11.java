package templateit_5;
import java.util.Arrays;
import java.util.regex.Matcher;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.regex.Pattern;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name", "param1", "param2"}, result);
}
@Test
public void testMatchTemplateName() {
    String text = "TemplateName";
    boolean result = OpMatcher.matchTemplateName(text);
    assertTrue(result);
}
@Test
public void testMatchTemplateParameter() {
    String text = "#param1";
    String result = OpMatcher.matchTemplateParameter(text);
    assertEquals("param1", result);
}
@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    boolean result = OpMatcher.matchTemplateEnd(text);
    assertTrue(result);
}
@Test
public void testMatchTemplateBeginNoParams() {
    String text = "@template_begin(name)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name"}, result);
}
@Test
public void testMatchTemplateParameterNumber() {
    String text = "#123";
    String result = OpMatcher.matchTemplateParameter(text);
    assertEquals("123", result);
}
@Test
public void testMatchTemplateNameInvalid() {
    String text = "123TemplateName";
    boolean result = OpMatcher.matchTemplateName(text);
    assertFalse(result);
}
@Test
public void testMatchStyleNoMatch() {
    String text = "invalid style";
    __NamedStyle result = OpMatcher.matchStyle(text);
    assertNull(result);
}
}