package corina_35;
import java.util.StringTokenizer;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testLeftPad() {
    assertEquals("  abc", StringUtils.leftPad("abc", 5));
}
@Test
public void testSplitByLines() {
    String text = "a\nb\nc";
    String[] expected = {"a", "b", "c"};
    assertArrayEquals(expected, StringUtils.splitByLines(text));
}
@Test
public void testEscapeForXML() {
    String input = "<>&";
    String expected = "&lt;&gt;&amp;";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
@Test
public void testExtractInts() {
    String s = "1 2 3";
    int[] expected = {1, 2, 3};
    assertArrayEquals(expected, StringUtils.extractInts(s));
}
@Test
public void testSubstitute() {
    String str = "hello world";
    String source = "world";
    String target = "universe";
    String expected = "hello universe";
    assertEquals(expected, StringUtils.substitute(str, source, target));
}
@Test
public void testLeftPadShorterThanSize() {
    assertEquals("abc", StringUtils.leftPad("abc", 2));
}
@Test
public void testSplitBy() {
    String text = "a,b,c";
    String[] expected = {"a", "b", "c"};
    assertArrayEquals(expected, StringUtils.splitBy(text, ','));
}
@Test
public void testEscapeForXMLControlChar() {
    String input = "\u0003";
    String expected = "ILLEGAL-XML-CHAR:0003;";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
}