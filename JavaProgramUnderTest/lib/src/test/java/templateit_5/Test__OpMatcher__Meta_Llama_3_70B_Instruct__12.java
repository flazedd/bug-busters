package templateit_5;
import java.util.Arrays;
import java.util.regex.Matcher;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.regex.Pattern;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name", "param1", "param2"}, names);
}
@Test
public void testMatchTemplateName() {
    String text = "TemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}
@Test
public void testMatchTemplateParameter() {
    String text = "#parameterName";
    String parameterName = OpMatcher.matchTemplateParameter(text);
    assertEquals("parameterName", parameterName);
}
@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}
@Test
public void testMatchStyleWithoutFlag() {
    String text = "@style(name)";
    __NamedStyle style = OpMatcher.matchStyle(text);
    assertNotNull(style);
    assertEquals("name", style.getName());
}
@Test
public void testMatchTemplateBeginWithNoParams() {
    String text = "@template_begin(name)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name"}, names);
}
@Test
public void testMatchTemplateBeginWithNullInput() {
    String text = null;
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNull(names);
}
@Test
public void testMatchTemplateEndWithTend() {
    String text = "@tend";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}
}