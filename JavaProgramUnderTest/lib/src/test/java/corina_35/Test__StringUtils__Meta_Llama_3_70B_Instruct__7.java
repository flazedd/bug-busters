package corina_35;
import java.io.UnsupportedEncodingException;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.StringTokenizer;
import java.util.Arrays;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__7 {
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
    String s = "1 2 3";
    int[] expected = {1, 2, 3};
    assertArrayEquals(expected, StringUtils.extractInts(s));
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
public void testLeftPadWithShorterString() {
    assertEquals("abc", StringUtils.leftPad("abc", 2));
}
@Test
public void testSplitBy() {
    String text = "a,b,c";
    String[] expected = {"a", "b", "c"};
    assertArrayEquals(expected, StringUtils.splitBy(text, ','));
}
@Test
public void testEscapeForXMLWithUnprintableChar() {
    String input = "a\u0001b";
    String expected = "aILLEGAL-XML-CHAR:0001;b";
    assertEquals(expected, StringUtils.escapeForXML(input));
}
}