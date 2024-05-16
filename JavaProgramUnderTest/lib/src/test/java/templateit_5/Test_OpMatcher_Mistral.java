package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Test_OpMatcher_Mistral {
@Test
public void testMatchTemplateBegin() {
    String text = "@template_begin(myTemplate, param1, param2)";
    String[] expectedNames = {"myTemplate", "param1", "param2"};
    String[] resultNames = OpMatcher.matchTemplateBegin(text);

    // Assuming both arrays contain Strings
    assertEquals(expectedNames.length, resultNames.length);
    for (int i = 0; i < expectedNames.length; i++) {
        assertEquals(expectedNames[i], resultNames[i]);
    }
}

@Test
public void testMatchTemplateParameterWithNumberIdentifier() {
    String text = "#param3 myValue";
    String expectedParameterName = "param3";
    String resultParameterName = OpMatcher.matchTemplateParameter(text);

    assertEquals(expectedParameterName, resultParameterName);
}

}