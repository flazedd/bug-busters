package templateit_5;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNotNull(names);
    assertEquals(3, names.length);
}

@Test
public void testMatchTemplateName() {
    String text = "TemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}

@Test
public void testMatchTemplateParameter() {
    String text = "#paramName";
    String paramName = OpMatcher.matchTemplateParameter(text);
    assertNotNull(paramName);
    assertEquals("paramName", paramName);
}

@Test
public void testMatchTemplateEnd() {
    String text = "@template_end";
    assertTrue(OpMatcher.matchTemplateEnd(text));
}

@Test
public void testMatchTemplateBeginWithTbegin() {
    String text = "@tbegin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNotNull(names);
    assertEquals(3, names.length);
}

@Test
public void testMatchTemplateBeginWithNoMatch() {
    String text = "random text";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNull(names);
}

@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#123";
    String paramName = OpMatcher.matchTemplateParameter(text);
    assertNotNull(paramName);
    assertEquals("123", paramName);
}

@Test
public void testMatchTemplateNameWithInvalidName() {
    String text = "Invalid Name";
    assertFalse(OpMatcher.matchTemplateName(text));
}

}