package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testHtmlEncoder() {
    assertEquals("&lt;&gt;&quot;&amp;", HtmlEncoder.encode("<>\"&"));
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
public void testHtmlEncoderSpecialCharsOnly() {
    assertEquals("&amp;&lt;&gt;&quot;", HtmlEncoder.encode("&<>\""));
}

@Test
public void testHtmlEncoderMultipleSpecialChars() {
    assertEquals("Hello&amp;World&lt;&quot;&gt;", HtmlEncoder.encode("Hello&World<\">"));
}

@Test
public void testHtmlEncoderAlreadyEncoded() {
    assertEquals("&amp;amp;", HtmlEncoder.encode("&amp;"));
}

@Test
public void testHtmlEncoderNullInput() {
    try {
        HtmlEncoder.encode(null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}

@Test
public void testHtmlEncoderLargeInput() {
    String largeInput = new String(new char[10000]).replace('\0', '<');
    String encoded = HtmlEncoder.encode(largeInput);
    assertEquals(largeInput.length() * 4, encoded.length()); // each '<' becomes '&lt;'
}

}