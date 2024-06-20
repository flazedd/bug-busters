package templateit_5;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.regex.Pattern;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] expected = {"name", "param1", "param2"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateName() {
    String text = "TemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}
@Test
public void testMatchTemplateParameter() {
    String text = "#param1";
    assertEquals("param1", OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}
@Test
public void testMatchTemplateBeginWithoutParams() {
    String text = "@template_begin(name)";
    String[] expected = {"name"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchStyleNullInput() {
    String text = null;
    assertNull(OpMatcher.matchStyle(text));
}
@Test
public void testMatchTemplateBeginWithNoParams() {
    String text = "@template_begin";
    assertNull(OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#1";
    assertEquals("1", OpMatcher.matchTemplateParameter(text));
}
}