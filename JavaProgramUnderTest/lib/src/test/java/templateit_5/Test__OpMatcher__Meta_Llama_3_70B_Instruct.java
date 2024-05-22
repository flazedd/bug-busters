package templateit_5;
import org.junit.jupiter.api.Test;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import static org.junit.jupiter.api.Assertions.*;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNotNull(names);
    assertEquals(3, names.length);
    assertEquals("name", names[0]);
    assertEquals("param1", names[1]);
    assertEquals("param2", names[2]);
}@Test
public void testMatchTemplateName() {
    String text = "TemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}

}