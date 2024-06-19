package templateit_5;
import org.junit.jupiter.api.Test;
import java.util.regex.Pattern;
import java.util.Arrays;
import java.util.regex.Matcher;
import static org.junit.jupiter.api.Assertions.*;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] expected = {"name", "param1", "param2"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateName() {
    String text = "validTemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}
@Test
public void testMatchTemplateParameter() {
    String text = "#paramName";
    String expected = "paramName";
    assertEquals(expected, OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}
@Test
public void testMatchTemplateBeginWithNoParams() {
    String text = "@template_begin(name)";
    String[] expected = {"name"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateBeginWithNoMatch() {
    String text = "no match";
    assertNull(OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#123";
    String expected = "123";
    assertEquals(expected, OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateNameWithInvalidName() {
    String text = "invalid name!";
    assertFalse(OpMatcher.matchTemplateName(text));
}
}