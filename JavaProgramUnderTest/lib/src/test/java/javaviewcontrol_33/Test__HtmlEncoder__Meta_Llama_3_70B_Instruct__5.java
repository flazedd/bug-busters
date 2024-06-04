package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__5 {
@Test
public void testHtmlEncoder() {
    assertEquals("&lt;&amp;&quot;&gt;", HtmlEncoder.encode("<&\">"));
}
@Test
public void testHtmlEncoderNoEscape() {
    assertEquals("Hello World", HtmlEncoder.encode("Hello World"));
}
@Test
public void testHtmlEncoderOnlyGT() {
    assertEquals("Hello &gt; World", HtmlEncoder.encode("Hello > World"));
}
@Test
public void testHtmlEncoderMultipleQuotes() {
    assertEquals("Hello &quot;World&quot;", HtmlEncoder.encode("Hello \"World\""));
}
@Test
public void testHtmlEncoderEmptyString() {
    assertEquals("", HtmlEncoder.encode(""));
}
@Test
public void testHtmlEncoderAmpersandOnly() {
    assertEquals("&amp;", HtmlEncoder.encode("&"));
}
@Test
public void testHtmlEncoderLessThanOnly() {
    assertEquals("&lt;", HtmlEncoder.encode("<"));
}
@Test
public void testHtmlEncoderGreaterThanOnly() {
    assertEquals("&gt;", HtmlEncoder.encode(">"));
}
}