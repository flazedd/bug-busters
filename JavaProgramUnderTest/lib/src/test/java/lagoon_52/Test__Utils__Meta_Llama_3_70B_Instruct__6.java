package lagoon_52;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Utils__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testEncodePath() {
    assertEquals("abc--def__ghi", Utils.encodePath("abc-def_ghi"));
}
@Test
public void testEncodePathWithSlash() {
    assertEquals("abc-def", Utils.encodePath("abc/def"));
}
@Test
public void testAbsoluteURL() {
    assertTrue(Utils.absoluteURL("http://example.com"));
}
@Test
public void testNotAbsoluteURL() {
    assertFalse(Utils.absoluteURL("example.com"));
}
@Test
public void testPseudoAbsoluteURL() {
    assertTrue(Utils.pseudoAbsoluteURL("/example.com"));
}
@Test
public void testNChars() {
    assertEquals("*****", Utils.nChars(5, '*'));
}
@Test
public void testNCharsZero() {
    assertEquals("", Utils.nChars(0, '*'));
}
@Test
public void testNCharsOne() {
    assertEquals("*", Utils.nChars(1, '*'));
}
}