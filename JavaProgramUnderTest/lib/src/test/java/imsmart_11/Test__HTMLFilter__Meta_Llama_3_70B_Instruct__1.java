package imsmart_11;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__HTMLFilter__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testHTMLFilter() {
    assertEquals("&lt;script&gt;", HTMLFilter.filter("<script>"));
}

@Test
public void testHTMLFilter_ampersand() {
    assertEquals("a&amp;b", HTMLFilter.filter("a&b"));
}

}