package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testEncode() {
    assertEquals("&lt;&quot;&amp;&gt;", HtmlEncoder.encode("<\"&>"));
}

@Test
public void testEncodeSpecialChars() {
    assertEquals("&#169;", HtmlEncoder.encode("©"));
}

@Test
public void testEncodeNonAscii() {
    assertEquals("H&#233;llo", HtmlEncoder.encode("Héllo"));
}

@Test
public void testEncodeNoChange() {
    assertEquals("Hello World", HtmlEncoder.encode("Hello World"));
}

@Test
public void testEncodeEmptyString() {
    assertEquals("", HtmlEncoder.encode(""));
}

@Test
public void testEncodeLongString() {
    String longString = "This is a very long string that needs to be encoded correctly";
    assertEquals(longString, HtmlEncoder.encode(longString));
}

@Test
public void testEncodeMixedCase() {
    assertEquals("&lt;a&gt;&quot;B&quot;&amp;c&lt;/a&gt;", HtmlEncoder.encode("<a>\"B\"&c</a>"));
}

@Test
public void testEncodeConsecutiveSpecialChars() {
    assertEquals("&lt;&amp;&gt;&quot;", HtmlEncoder.encode("<&>\""));
}

}