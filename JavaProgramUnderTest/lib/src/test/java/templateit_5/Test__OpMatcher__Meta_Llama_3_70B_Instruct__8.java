package templateit_5;
import java.util.regex.Pattern;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.regex.Matcher;
import static org.junit.jupiter.api.Assertions.*;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name", "param1", "param2"}, result);
}
@Test
public void testMatchTemplateName() {
    String text = "TemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}
@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}
@Test
public void testMatchTemplateParameter() {
    String text = "#parameterName";
    assertEquals("parameterName", OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateBeginWithTBegin() {
    String text = "@tbegin(name, param1, param2)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name", "param1", "param2"}, result);
}
@Test
public void testMatchTemplateBeginNullInput() {
    String text = null;
    assertNull(OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#123";
    assertEquals("123", OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateBeginWithoutParams() {
    String text = "@template_begin(name)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name"}, result);
}
}