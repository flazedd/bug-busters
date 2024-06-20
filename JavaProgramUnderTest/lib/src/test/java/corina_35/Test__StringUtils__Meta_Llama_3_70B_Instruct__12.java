package corina_35;
import java.util.Arrays;
import java.util.StringTokenizer;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
import org.junit.jupiter.api.Test;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testLeftPad() {
    assertEquals("  abc", StringUtils.leftPad("abc", 5));
}
@Test
public void testSplitByLines() {
    String input = "a\nb\nc";
    String[] expected = {"a", "b", "c"};
    assertArrayEquals(expected, StringUtils.splitByLines(input));
}
@Test
public void testExtractInts() {
    String input = "1 2 3";
    int[] expected = {1, 2, 3};
    assertArrayEquals(expected, StringUtils.extractInts(input));
}
@Test
public void testEscapeForXML() {
    String input = "<hello>&world</hello>";
    String expected = "&lt;hello&gt;&amp;world&lt;/hello&gt;";
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
public void testLeftPadWithLongString() {
    String input = "abcdefghij";
    String expected = "  abcdefghij";
    assertEquals(expected, StringUtils.leftPad(input, 12));
}
@Test
public void testSplitBy() {
    String input = "a,b,c";
    String[] expected = {"a", "b", "c"};
    assertArrayEquals(expected, StringUtils.splitBy(input, ','));
}
@Test
public void testLeftPadWithEqualLength() {
    String input = "abc";
    String expected = "abc";
    assertEquals(expected, StringUtils.leftPad(input, 3));
}
}