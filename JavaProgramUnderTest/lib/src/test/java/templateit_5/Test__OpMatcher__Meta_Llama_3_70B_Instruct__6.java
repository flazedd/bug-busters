package templateit_5;
import java.util.regex.Matcher;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.regex.Pattern;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[] {"name", "param1", "param2"}, result);
}
@Test
public void testMatchTemplateName() {
    String text = "validTemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}
@Test
public void testMatchTemplateParameter() {
    String text = "#paramName";
    String result = OpMatcher.matchTemplateParameter(text);
    assertEquals("paramName", result);
}
@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}
@Test
public void testMatchTemplateBeginWithTbegin() {
    String text = "@tbegin(name, param1, param2)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[] {"name", "param1", "param2"}, result);
}
@Test
public void testMatchTemplateBeginWithNullInput() {
    String text = null;
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertNull(result);
}
@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#123";
    String result = OpMatcher.matchTemplateParameter(text);
    assertEquals("123", result);
}
@Test
public void testMatchStyleWithoutMatch() {
    String text = "invalidStyle";
    __NamedStyle result = OpMatcher.matchStyle(text);
    assertNull(result);
}
}