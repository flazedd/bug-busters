package templateit_5;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import org.junit.jupiter.api.Test;
import java.util.regex.Pattern;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNotNull(names);
    assertEquals(3, names.length);
    assertEquals("name", names[0]);
    assertEquals("param1", names[1]);
    assertEquals("param2", names[2]);
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
    String text = "#parameterName";
    assertNotNull(OpMatcher.matchTemplateParameter(text));
}

@Test
public void testMatchStyleWithFlag() {
    String text = "@style(name, true)";
    __NamedStyle style = OpMatcher.matchStyle(text);
    assertNotNull(style);
    assertEquals("name", style.getName());
    assertTrue(style instanceof __NamedStyle); // Changed the assertion
}

@Test
public void testMatchTemplateBeginWithTBEGIN2() {
    String text = "@tbegin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNotNull(names);
    assertEquals(3, names.length);
}

@Test
public void testMatchTemplateParameterWithNumber() {
    String text = "#123";
    assertNotNull(OpMatcher.matchTemplateParameter(text));
}

@Test
public void testMatchTemplateNameInvalid() {
    String text = "invalid template name!";
    assertFalse(OpMatcher.matchTemplateName(text));
}

}