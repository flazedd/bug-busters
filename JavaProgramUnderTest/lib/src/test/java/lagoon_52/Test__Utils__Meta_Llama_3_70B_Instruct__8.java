package lagoon_52;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Utils__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testEncodePath() {
    assertEquals("hello--world", Utils.encodePath("hello-world"));
}
@Test
public void testAbsoluteURL() {
    assertTrue(Utils.absoluteURL("http://example.com"));
}
@Test
public void testPseudoAbsoluteURL() {
    assertTrue(Utils.pseudoAbsoluteURL("/hello/world"));
}
@Test
public void testNChars() {
    assertEquals("*****", Utils.nChars(5, '*'));
}
@Test
public void testEncodePathWithTilde() {
    assertEquals("hello~~world", Utils.encodePath("hello~world"));
}
@Test
public void testAbsoluteURLWithNoColon() {
    assertFalse(Utils.absoluteURL("example.com"));
}
@Test
public void testPseudoAbsoluteURLWithRelativePath() {
    assertFalse(Utils.pseudoAbsoluteURL("hello/world"));
}
@Test
public void testNCharsWithZero() {
    assertEquals("", Utils.nChars(0, '*'));
}
}