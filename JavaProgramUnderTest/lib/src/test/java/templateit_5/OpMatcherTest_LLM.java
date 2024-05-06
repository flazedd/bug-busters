package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class OpMatcherTest_LLM {
@Test
void testMatchTemplateName() {
    assertTrue(OpMatcher.matchTemplateName("validTemplateName"));
}

}