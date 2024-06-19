package templateit_5;
import java.util.Arrays;
import java.util.regex.Matcher;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Pattern;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__7 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] expected = {"name", "param1", "param2"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateName() {
    String text = "myTemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}
@Test
public void testMatchTemplateParameter() {
    String text = "#myParameter";
    assertEquals("myParameter", OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}
@Test
public void testMatchTemplateBeginWithTBEGIN2() {
    String text = "@tbegin(name, param1, param2)";
    String[] expected = {"name", "param1", "param2"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateBeginWithNullInput() {
    String text = null;
    assertNull(OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#123";
    assertEquals("123", OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateNameWithInvalidInput() {
    String text = "invalidTemplateName!";
    assertFalse(OpMatcher.matchTemplateName(text));
}
}