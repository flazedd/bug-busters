package templateit_5;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name", "param1", "param2"}, names);
}

@Test
public void testMatchTemplateName() {
    String text = "validTemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}

@Test
public void testMatchTemplateParameter() {
    String text = "#paramName";
    String parameterName = OpMatcher.matchTemplateParameter(text);
    assertEquals("paramName", parameterName);
}

@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}

@Test
public void testMatchTemplateBeginWithoutParams() {
    String text = "@template_begin(name)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertArrayEquals(new String[]{"name"}, names);
}

@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#123";
    String parameterName = OpMatcher.matchTemplateParameter(text);
    assertEquals("123", parameterName);
}

@Test
public void testMatchTemplateBeginWithNoMatch() {
    String text = "no match";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNull(names);
}

@Test
public void testMatchTemplateNameWithInvalidName() {
    String text = "invalid name!";
    assertFalse(OpMatcher.matchTemplateName(text));
}

}