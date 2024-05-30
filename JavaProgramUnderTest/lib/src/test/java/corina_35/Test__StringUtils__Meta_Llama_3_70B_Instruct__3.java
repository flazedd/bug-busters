package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__3 {
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
public void testEscapeForXML() {
    String input = "<hello>&world</hello>";
    String expected = "&lt;hello&gt;&amp;world&lt;/hello&gt;";
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
    assertEquals("   1", StringUtils.leftPad("1", 4));
}

@Test
public void testSplitBy() {
    String input = "hello,world,java";
    String[] expected = {"hello", "world", "java"};
    assertArrayEquals(expected, StringUtils.splitBy(input, ','));
}

@Test
public void testLeftPadLongString() {
    String input = "abcdefghijklmnopqrstuvwxyz";
    assertEquals("abcdefghijklmnopqrstuvwxyz", StringUtils.leftPad(input, 10));
}

}