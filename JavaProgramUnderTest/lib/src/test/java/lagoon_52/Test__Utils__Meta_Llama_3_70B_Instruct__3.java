package lagoon_52;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Utils__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testEncodePath() {
    assertEquals("hello--world", Utils.encodePath("hello-world"));
}

@Test
public void testEncodePathWithDollar() {
    assertEquals("hello$$world", Utils.encodePath("hello$world"));
}

@Test
public void testEncodePathWithTilde() {
    assertEquals("hello~~world", Utils.encodePath("hello~world"));
}

@Test
public void testEncodePathWithStar() {
    assertEquals("hello_world", Utils.encodePath("hello*world"));
}

@Test
public void testEncodePathWithColon() {
    assertEquals("hello~world", Utils.encodePath("hello:world"));
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

}