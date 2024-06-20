package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__11 {
@Test
    public void testHtmlEncoder() {
        assertEquals("&lt;&gt;&amp;&quot;", HtmlEncoder.encode("<>&\""));
    }
@Test
    public void testHtmlEncoderOriginal() {
        assertEquals("&lt;&gt;&amp;&quot;", HtmlEncoder.encode("<>&\""));
    }
@Test
    public void testHtmlEncoderSimpleString() {
        assertEquals("Hello World", HtmlEncoder.encode("Hello World"));
    }
@Test
    public void testHtmlEncoderNewSimpleString() {
        assertEquals("Hello Universe", HtmlEncoder.encode("Hello Universe"));
    }
@Test
    public void testHtmlEncoderUtf8New() {
        assertEquals("abc", HtmlEncoder.encode("abc"));
    }
@Test
    public void testHtmlEncoderNewSpecialCharsAtStart() {
        assertEquals("&lt;&gt;&amp;&quot;abc", HtmlEncoder.encode("<>&\"abc"));
    }
@Test
    public void testHtmlEncoderNewSpecialCharsWithPunctuation() {
        assertEquals("&lt;a!&gt;&amp;b?&lt;c&gt;&quot;d.&quot;", HtmlEncoder.encode("<a!>&b?<c>\"d.\""));
    }
@Test
public void testHtmlEncoderSpecialChars() {
    assertEquals("&lt;a&gt; &amp; b &quot;c&quot;", HtmlEncoder.encode("<a> & b \"c\""));
}
}