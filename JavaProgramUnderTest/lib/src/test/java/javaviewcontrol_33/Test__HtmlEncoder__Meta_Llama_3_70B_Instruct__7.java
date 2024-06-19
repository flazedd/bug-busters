package javaviewcontrol_33;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__7 {
@Test
public void testHtmlEncoder() {
    assertEquals("&lt;a&gt;&amp;&quot;", HtmlEncoder.encode("<a>&\""));
}
@Test
public void testHtmlEncoderSimpleString() {
    assertEquals("Hello World", HtmlEncoder.encode("Hello World"));
}
@Test
public void testHtmlEncoderEmptyString() {
    assertEquals("", HtmlEncoder.encode(""));
}
@Test
public void testHtmlEncoderMultipleSpecialChars() {
    assertEquals("&amp;&lt;&gt;&quot;", HtmlEncoder.encode("&<>\""));
}
@Test
public void testHtmlEncoderOnlySpecialChars() {
    assertEquals("&amp;&amp;&lt;&lt;&gt;&gt;&quot;&quot;", HtmlEncoder.encode("&&<<>>\"\""));
}
@Test
public void testHtmlEncoderSpecialCharsAtStartAndEnd() {
    assertEquals("&lt;a&gt;&quot;&amp;&quot;", HtmlEncoder.encode("<a>\"&\""));
}
@Test
public void testHtmlEncoderConsecutiveSpecialChars() {
    assertEquals("&lt;&lt;&gt;&gt;&amp;&amp;&quot;&quot;", HtmlEncoder.encode("<<>>&&\"\""));
}
@Test
public void testHtmlEncoderSingleQuoteAlternative() {
    assertEquals("'", HtmlEncoder.encode("'"));
}
}