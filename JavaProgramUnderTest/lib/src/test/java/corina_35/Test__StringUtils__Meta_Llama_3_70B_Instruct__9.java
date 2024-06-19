package corina_35;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.io.UnsupportedEncodingException;
import java.util.StringTokenizer;
import static org.junit.jupiter.api.Assertions.*;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testLeftPad() {
    assertEquals("  abc", StringUtils.leftPad("abc", 5));
}
@Test
public void testSplitByLines() {
    String text = "Hello\nWorld\nJava";
    String[] expected = {"Hello", "World", "Java"};
    assertArrayEquals(expected, StringUtils.splitByLines(text));
}
@Test
public void testExtractInts() {
    String text = "1 2 3 4 5";
    int[] expected = {1, 2, 3, 4, 5};
    assertArrayEquals(expected, StringUtils.extractInts(text));
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
    String target = "java";
    String expected = "hello java";
    assertEquals(expected, StringUtils.substitute(str, source, target));
}
@Test
public void testLeftPadEqualLength() {
    assertEquals("abc", StringUtils.leftPad("abc", 3));
}
@Test
public void testSplitBy() {
    String text = "a,b,c,d,e";
    String[] expected = {"a", "b", "c", "d", "e"};
    assertArrayEquals(expected, StringUtils.splitBy(text, ','));
}
@Test
public void testEscapeForXMLQuotes() {
    String input = "\"hello\" 'world'";
    String expected = "&quot;hello&quot; &apos;world&apos;";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
}