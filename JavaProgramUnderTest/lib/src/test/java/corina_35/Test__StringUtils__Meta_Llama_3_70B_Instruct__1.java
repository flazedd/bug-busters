package corina_35;
import java.io.UnsupportedEncodingException;
import static org.junit.jupiter.api.Assertions.*;
import java.util.StringTokenizer;
import org.junit.jupiter.api.Test;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__1 {
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
    String[] result = StringUtils.splitByLines("a\nb\nc");
    assertEquals("a", result[0]);
    assertEquals("b", result[1]);
    assertEquals("c", result[2]);
}

@Test
public void testExtractInts() {
    int[] result = StringUtils.extractInts("1 2 3");
    assertEquals(1, result[0]);
    assertEquals(2, result[1]);
    assertEquals(3, result[2]);
}

@Test
public void testSubstitute() {
    assertEquals("hello world", StringUtils.substitute("hello universe", "universe", "world"));
}

@Test
public void testLeftPadEmptyString() {
    assertEquals("    ", StringUtils.leftPad("", 4));
}

@Test
public void testSplitBy() {
    String[] result = StringUtils.splitBy("a,b,c", ',');
    assertEquals("a", result[0]);
    assertEquals("b", result[1]);
    assertEquals("c", result[2]);
}

@Test
public void testEscapeForXMLSpecialChars() {
    assertEquals("&lt;&amp;&gt;&apos;&quot;", StringUtils.escapeForXML("<&>'\""));
}















}