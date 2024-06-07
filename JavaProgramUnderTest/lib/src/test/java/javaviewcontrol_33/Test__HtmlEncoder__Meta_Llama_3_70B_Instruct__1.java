package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testHtmlEncoder() {
    assertEquals("&lt;hello&gt;", HtmlEncoder.encode("<hello>"));
}

@Test
public void testHtmlEncoderDoubleQuote() {
    assertEquals("&quot;hello&quot;", HtmlEncoder.encode("\"hello\""));
}

@Test
public void testHtmlEncoderAmpersand() {
    assertEquals("hello&amp;world", HtmlEncoder.encode("hello&world"));
}

@Test
public void testHtmlEncoderUnicode() {
    assertEquals("&#161;", HtmlEncoder.encode("\u00A1"));
}

@Test
public void testHtmlEncoderNoEscapingNeeded() {
    assertEquals("hello world", HtmlEncoder.encode("hello world"));
}

@Test
public void testHtmlEncoderEmptyString() {
    assertEquals("", HtmlEncoder.encode(""));
}

@Test
public void testEncode() {
    assertEquals("&lt;&quot;&amp;&gt;", HtmlEncoder.encode("<\"&>"));
}

@Test
public void testEncodeNonAscii() {
    assertEquals("&#169;", HtmlEncoder.encode("\u00A9"));
}







}