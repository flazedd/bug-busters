package lagoon_52;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Utils__Meta_Llama_3_70B_Instruct__11 {
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
    assertTrue(Utils.pseudoAbsoluteURL("/example/path"));
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
public void testAbsoluteURLWithHttps() {
    assertTrue(Utils.absoluteURL("https://example.com"));
}
@Test
public void testAbsoluteURLWithNoProtocol() {
    assertFalse(Utils.absoluteURL("example.com"));
}
@Test
public void testNCharsWithZero() {
    assertEquals("", Utils.nChars(0, '*'));
}
}