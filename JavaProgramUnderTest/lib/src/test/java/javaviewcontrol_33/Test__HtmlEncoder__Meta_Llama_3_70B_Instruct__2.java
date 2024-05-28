package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__2 {
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
public void testHtmlEncoderNoEncodingNeeded() {
    assertEquals("hello", HtmlEncoder.encode("hello"));
}

@Test
public void testHtmlEncoderMultipleSpecialCharacters() {
    assertEquals("&lt;hello&amp;&gt;", HtmlEncoder.encode("<hello&>"));
}

@Test
public void testHtmlEncoderEmptyString() {
    assertEquals("", HtmlEncoder.encode(""));
}

@Test
public void testHtmlEncoderNullInput() {
    try {
        HtmlEncoder.encode(null);
        fail("Expected NullPointerException to be thrown");
    } catch (NullPointerException e) {
        // expected
    }
}

@Test
public void testHtmlEncoderMixedCase() {
    assertEquals("&lt;HeLlO&gt;", HtmlEncoder.encode("<HeLlO>"));
}

}