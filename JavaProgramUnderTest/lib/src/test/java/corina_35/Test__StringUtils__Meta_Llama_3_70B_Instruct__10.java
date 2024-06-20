package corina_35;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
import java.util.StringTokenizer;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testLeftPad() {
    assertEquals("  abc", StringUtils.leftPad("abc", 5));
}
@Test
public void testSplitByLines() {
    String input = "line1\nline2\nline3";
    String[] expected = {"line1", "line2", "line3"};
    assertArrayEquals(expected, StringUtils.splitByLines(input));
}
@Test
public void testExtractInts() {
    String input = "1 2 3 4 5";
    int[] expected = {1, 2, 3, 4, 5};
    assertArrayEquals(expected, StringUtils.extractInts(input));
}
@Test
public void testEscapeForXML() {
    String input = "<hello>&world;</hello>";
    String expected = "&lt;hello&gt;&amp;world;&lt;/hello&gt;";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
@Test
public void testSubstitute() {
    String input = "hello world";
    String source = "world";
    String target = "universe";
    String expected = "hello universe";
    assertEquals(expected, StringUtils.substitute(input, source, target));
}
@Test
public void testLeftPadShortString() {
    assertEquals("     a", StringUtils.leftPad("a", 6));
}
@Test
public void testSplitBy() {
    String input = "a,b,c,d,e";
    String[] expected = {"a", "b", "c", "d", "e"};
    assertArrayEquals(expected, StringUtils.splitBy(input, ','));
}
@Test
public void testEscapeForXMLSpecialChars() {
    String input = "hello\u0003world";
    String expected = "helloILLEGAL-XML-CHAR:0003;world";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
}