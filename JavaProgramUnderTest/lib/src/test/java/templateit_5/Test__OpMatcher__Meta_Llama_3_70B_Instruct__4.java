package templateit_5;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Pattern;
import java.util.Arrays;
import java.util.regex.Matcher;
import org.junit.jupiter.api.Test;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__4 {
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
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}
@Test
public void testMatchTemplateParameter() {
    String text = "#paramName";
    String expected = "paramName";
    assertEquals(expected, OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateBeginWithTbegin() {
    String text = "@tbegin(name, param1, param2)";
    String[] expected = {"name", "param1", "param2"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#123";
    String expected = "123";
    assertEquals(expected, OpMatcher.matchTemplateParameter(text));
}
@Test
public void testMatchTemplateBeginWithNoParams() {
    String text = "@template_begin(name)";
    String[] expected = {"name"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}
@Test
public void testMatchTemplateNameWithInvalidName() {
    String text = "InvalidTemplateName!";
    assertFalse(OpMatcher.matchTemplateName(text));
}
}