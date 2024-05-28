package corina_35;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.StringTokenizer;
import java.io.UnsupportedEncodingException;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testLeftPad() {
    assertEquals("abc", StringUtils.leftPad("abc", 3));
}

@Test
public void testEscapeForXML() {
    assertEquals("&lt;&gt;&amp;&quot;&apos;", StringUtils.escapeForXML("<>&\"'"));
}

@Test
public void testSplitByLines() {
    String[] result = StringUtils.splitByLines("hello\nworld\nfoo");
    assertEquals("hello", result[0]);
    assertEquals("world", result[1]);
    assertEquals("foo", result[2]);
}

@Test
public void testExtractInts() {
    int[] result = StringUtils.extractInts("1 2 3 4 5");
    assertEquals(1, result[0]);
    assertEquals(2, result[1]);
    assertEquals(3, result[2]);
    assertEquals(4, result[3]);
    assertEquals(5, result[4]);
}

@Test
public void testSubstitute() {
    assertEquals("hello world", StringUtils.substitute("hello foo", "foo", "world"));
}

@Test
public void testSubstituteNoMatch() {
    assertEquals("hello foo", StringUtils.substitute("hello foo", "bar", "world"));
}

@Test
public void testLeftPadEmptyString() {
    assertEquals("    ", StringUtils.leftPad("", 4));
}

@Test
public void testEscapeForXMLNonISOControl() {
    String input = "hello\u0001world";
    String expected = "helloILLEGAL-XML-CHAR:0001;world";
    assertEquals(expected, StringUtils.escapeForXML(input));
}

}