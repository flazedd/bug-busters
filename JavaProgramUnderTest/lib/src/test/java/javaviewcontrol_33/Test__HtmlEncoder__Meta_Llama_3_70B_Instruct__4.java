package javaviewcontrol_33;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testHtmlEncoder() {
    String input = "Hello & World!";
    String expected = "Hello &amp; World!";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderQuotes() {
    String input = "Hello \"World\"";
    String expected = "Hello &quot;World&quot;";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderLessThan() {
    String input = "Hello < World";
    String expected = "Hello &lt; World";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderGreaterThan() {
    String input = "Hello > World";
    String expected = "Hello &gt; World";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderMixed() {
    String input = "Hello \"World\" < & >";
    String expected = "Hello &quot;World&quot; &lt; &amp; &gt;";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderNoChange() {
    String input = "Hello World";
    String expected = "Hello World";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderEmptyString() {
    String input = "";
    String expected = "";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderMultipleAmpersands() {
    String input = "Hello &&& World";
    String expected = "Hello &amp;&amp;&amp; World";
    assertEquals(expected, HtmlEncoder.encode(input));
}
}