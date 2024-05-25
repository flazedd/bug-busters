package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__HtmlEncoder__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testHtmlEncoder() {
    assertEquals("&lt;hello&gt;", HtmlEncoder.encode("<hello>"));
}

@Test
public void testHtmlEncoderQuotes() {
    assertEquals("&quot;Hello&amp;World&quot;", HtmlEncoder.encode("\"Hello&World\""));
}

}