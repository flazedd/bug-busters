package javaviewcontrol_33;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testHtmlEncoder() {
    String input = "Hello, & World!";
    String expected = "Hello, &amp; World!";
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
    String input = "Hello <World>";
    String expected = "Hello &lt;World&gt;";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderMultipleEntities() {
    String input = "Hello \"World\" <and> & foo";
    String expected = "Hello &quot;World&quot; &lt;and&gt; &amp; foo";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderNoEntities() {
    String input = "Hello World";
    String expected = "Hello World";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderMixedCase() {
    String input = "Hello >World< and \"foo\" & bar";
    String expected = "Hello &gt;World&lt; and &quot;foo&quot; &amp; bar";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderEmptyString() {
    String input = "";
    String expected = "";
    assertEquals(expected, HtmlEncoder.encode(input));
}
@Test
public void testHtmlEncoderBackslash() {
    String input = "Hello \\World";
    String expected = "Hello \\World";
    assertEquals(expected, HtmlEncoder.encode(input));
}
}