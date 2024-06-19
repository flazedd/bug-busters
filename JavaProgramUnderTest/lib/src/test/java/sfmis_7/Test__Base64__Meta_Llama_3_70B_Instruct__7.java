package sfmis_7;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__Base64__Meta_Llama_3_70B_Instruct__7 {
@Test
    public void testBase64() {
        String s = "0123456789";
        byte b[] = s.getBytes();
        String base64 = Base64.byteArrayToBase64(b);
        byte b2[] = Base64.base64ToByteArray(base64);
        assertEquals(s, new String(b2));
    }
@Test
    public void testAltBase64() {
        String s = "Hello, World!";
        byte b[] = s.getBytes();
        String altBase64 = Base64.byteArrayToAltBase64(b);
        byte b2[] = Base64.altBase64ToByteArray(altBase64);
        assertEquals(s, new String(b2));
    }
@Test
    public void testEmptyString() {
        String s = "";
        byte b[] = s.getBytes();
        String base64 = Base64.byteArrayToBase64(b);
        byte b2[] = Base64.base64ToByteArray(base64);
        assertEquals(s, new String(b2));
    }
@Test
    public void testNullInput() {
        try {
            Base64.byteArrayToBase64(null);
            assert false;
        } catch (NullPointerException e) {
            assertNotNull(e.getMessage());
        }
    }
@Test
    public void testLargeInput() {
        String s = new String(new char[10000]).replace('\0', 'a');
        byte b[] = s.getBytes();
        String base64 = Base64.byteArrayToBase64(b);
        byte b2[] = Base64.base64ToByteArray(base64);
        assertEquals(s, new String(b2));
    }
@Test
    public void testInvalidBase64() {
        String invalidBase64 = "Invalid base64 string";
        try {
            Base64.base64ToByteArray(invalidBase64);
            assert false;
        } catch (IllegalArgumentException e) {
            assertNotNull(e.getMessage());
        }
    }
@Test
    public void testWhitespaceInput() {
        String s = "   ";
        byte b[] = s.getBytes();
        String base64 = Base64.byteArrayToBase64(b);
        byte b2[] = Base64.base64ToByteArray(base64);
        assertEquals(s, new String(b2));
    }
@Test
    public void testNonAsciiInput() {
        String s = "Hello, café!";
        byte b[] = s.getBytes();
        String base64 = Base64.byteArrayToBase64(b);
        byte b2[] = Base64.base64ToByteArray(base64);
        assertEquals(s, new String(b2));
    }
}