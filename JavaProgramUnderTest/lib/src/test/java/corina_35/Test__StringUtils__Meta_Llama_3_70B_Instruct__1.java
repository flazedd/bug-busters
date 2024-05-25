package corina_35;
import java.io.UnsupportedEncodingException;
import java.util.StringTokenizer;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__StringUtils__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testExtractInts() {
    int[] result = StringUtils.extractInts("1 2 3");
    assertEquals(1, result[0]);
}

@Test
public void testLeftPad() {
    assertEquals("abc", StringUtils.leftPad("abc", 3));
}

}