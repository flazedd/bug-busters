package lagoon_52;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Utils__Meta_Llama_3_70B_Instruct__12 {
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
    assertTrue(Utils.pseudoAbsoluteURL("/example"));
}
@Test
public void testNChars() {
    assertEquals("*****", Utils.nChars(5, '*'));
}
@Test
public void testEncodePathSlash() {
    assertEquals("hello-world", Utils.encodePath("hello/world"));
}
@Test
public void testEncodePathAsIdentifierNull() {
    assertThrows(NullPointerException.class, () -> Utils.encodePathAsIdentifier(null));
}
@Test
public void testNCharsZero() {
    assertEquals("", Utils.nChars(0, '*'));
}
@Test
public void testAbsoluteURLNoProtocol() {
    assertFalse(Utils.absoluteURL("example.com"));
}
}