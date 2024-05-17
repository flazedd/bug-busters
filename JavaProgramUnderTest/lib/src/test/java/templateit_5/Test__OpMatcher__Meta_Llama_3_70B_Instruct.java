package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Test__OpMatcher__Meta_Llama_3_70B_Instruct {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(name, param1, param2)";
    String[] expected = {"name", "param1", "param2"};
    assertArrayEquals(expected, OpMatcher.matchTemplateBegin(text));
}

@Test
public void testMatchTemplateName() {
    String text = "ValidTemplateName";
    assertTrue(OpMatcher.matchTemplateName(text));
}

}