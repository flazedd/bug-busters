package corina_35;
import java.util.Arrays;
import java.util.StringTokenizer;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
import org.junit.jupiter.api.Test;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testLeftPad() {
    assertEquals("  abc", StringUtils.leftPad("abc", 5));
}
@Test
public void testSplitByLines() {
    String text = "hello\nworld\njava";
    String[] expected = {"hello", "world", "java"};
    assertArrayEquals(expected, StringUtils.splitByLines(text));
}
@Test
public void testExtractInts() {
    String input = "1 2 3 4 5";
    int[] expected = {1, 2, 3, 4, 5};
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
    String text = "hello,world,java";
    String[] expected = {"hello", "world", "java"};
    assertArrayEquals(expected, StringUtils.splitBy(text, ','));
}
@Test
public void testEscapeForXMLControlCharacter() {
    String input = "hello\u0001world";
    String expected = "helloILLEGAL-XML-CHAR:0001;world";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
}