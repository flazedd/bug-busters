package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testHtmlEncoder() {
    assertEquals("&lt;&amp;&quot;&gt;", HtmlEncoder.encode("<&\">"));
}
@Test
public void testHtmlEncoder2() {
    assertEquals("normal text", HtmlEncoder.encode("normal text"));
}
@Test
public void testHtmlEncoder3() {
    assertEquals("a&amp;b", HtmlEncoder.encode("a&b"));
}
@Test
public void testHtmlEncoder4() {
    assertEquals("&quot;Hello&quot;", HtmlEncoder.encode("\"Hello\""));
}
@Test
public void testHtmlEncoder5() {
    assertEquals("a&lt;b&gt;c", HtmlEncoder.encode("a<b>c"));
}
@Test
public void testHtmlEncoder6() {
    assertEquals("a&amp;&lt;&gt;&quot;b", HtmlEncoder.encode("a&<>\"b"));
}
@Test
public void testHtmlEncoder7() {
    assertEquals("", HtmlEncoder.encode(""));
}
@Test
public void testHtmlEncoder8() {
    assertEquals("Hello&amp;World", HtmlEncoder.encode("Hello&World"));
}
}