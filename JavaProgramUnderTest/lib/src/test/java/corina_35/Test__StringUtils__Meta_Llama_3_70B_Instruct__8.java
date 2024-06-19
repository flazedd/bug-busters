package corina_35;
import java.util.StringTokenizer;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testLeftPad() {
    assertEquals("  abc", StringUtils.leftPad("abc", 5));
}
@Test
public void testSplitByLines() {
    String input = "Hello\nWorld\nJava";
    String[] expected = {"Hello", "World", "Java"};
    assertArrayEquals(expected, StringUtils.splitByLines(input));
}
@Test
public void testExtractInts() {
    String input = "1 2 3 4 5";
    int[] expected = {1, 2, 3, 4, 5};
    assertArrayEquals(expected, StringUtils.extractInts(input));
}
@Test
public void testSubstitute() {
    String input = "Hello World";
    String source = "World";
    String target = "Universe";
    String expected = "Hello Universe";
    assertEquals(expected, StringUtils.substitute(input, source, target));
}
@Test
public void testEscapeForXML() {
    String input = "<hello>&world</hello>";
    String expected = "&lt;hello&gt;&amp;world&lt;/hello&gt;";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
@Test
public void testLeftPadEqualLength() {
    assertEquals("abc", StringUtils.leftPad("abc", 3));
}
@Test
public void testSplitBy() {
    String input = "hello,world,java";
    String[] expected = {"hello", "world", "java"};
    assertArrayEquals(expected, StringUtils.splitBy(input, ','));
}
@Test
public void testEscapeForXMLAmpersand() {
    String input = "a&b";
    String expected = "a&amp;b";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
}