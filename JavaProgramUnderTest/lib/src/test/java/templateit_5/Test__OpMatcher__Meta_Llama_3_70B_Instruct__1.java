package templateit_5;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.junit.jupiter.api.Test;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] result = OpMatcher.matchTemplateBegin(text);
    assertNotNull(result);
    assertEquals(3, result.length);
    assertEquals("name", result[0]);
    assertEquals("param1", result[1]);
    assertEquals("param2", result[2]);
}

@Test
public void testMatchTemplateName() {
    String text = "validTemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}



}