package corina_35;
import java.util.StringTokenizer;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__5 {
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
public void testExtractInts() {
    String input = "1 2 3";
    int[] expected = {1, 2, 3};
    assertArrayEquals(expected, StringUtils.extractInts(input));
}
@Test
public void testEscapeForXML() {
    String input = "<>&";
    String expected = "&lt;&gt;&amp;";
    assertEquals(expected, StringUtils.escapeForXML(input));
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
public void testLeftPadLongerString() {
    assertEquals("  abcdef", StringUtils.leftPad("abcdef", 8));
}
@Test
public void testSplitBy() {
    String text = "a,b,c";
    String[] expected = {"a", "b", "c"};
    assertArrayEquals(expected, StringUtils.splitBy(text, ','));
}
@Test
public void testEscapeForXMLQuotes() {
    String input = "\"'";
    String expected = "&quot;&apos;";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
}