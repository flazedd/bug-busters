package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class OpMatcherTest_LLM {
@Test
void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] names = OpMatcher.matchTemplateBegin(text);
    assertNotNull(names);
    assertEquals(3, names.length);
    assertEquals("name", names[0]);
    assertEquals("param1", names[1]);
    assertEquals("param2", names[2]);
}

}