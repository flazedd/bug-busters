package sfmis_7;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64__Meta_Llama_3_70B_Instruct__11 {
@Test
    public void base64EncodingDecodingTest() {
        String originalString = "Hello, World!";
        byte[] originalBytes = originalString.getBytes();
        String base64String = Base64.byteArrayToBase64(originalBytes);
        byte[] decodedBytes = Base64.base64ToByteArray(base64String);
        String decodedString = new String(decodedBytes);
        assertEquals(originalString, decodedString);
    }
@Test
    public void base64EncodingDecodingTest2() {
        String originalString = "This is a test string";
        byte[] originalBytes = originalString.getBytes();
        String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
        byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
        String decodedString = new String(decodedBytes);
        assertEquals(originalString, decodedString);
    }
@Test
    public void base64EncodingDecodingTest3() {
        String originalString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        byte[] originalBytes = originalString.getBytes();
        String base64String = Base64.byteArrayToBase64(originalBytes);
        byte[] decodedBytes = Base64.base64ToByteArray(base64String);
        String decodedString = new String(decodedBytes);
        assertEquals(originalString, decodedString);
    }
@Test
    public void base64EncodingDecodingTest4() {
        String originalString = "abcdefghijklmnopqrstuvwxyz";
        byte[] originalBytes = originalString.getBytes();
        String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
        byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
        String decodedString = new String(decodedBytes);
        assertEquals(originalString, decodedString);
    }
@Test
    public void base64EncodingDecodingTest5() {
        String originalString = "1234567890";
        byte[] originalBytes = originalString.getBytes();
        String base64String = Base64.byteArrayToBase64(originalBytes);
        byte[] decodedBytes = Base64.base64ToByteArray(base64String);
        String decodedString = new String(decodedBytes);
        assertEquals(originalString, decodedString);
    }
@Test
    public void base64EncodingDecodingTest6() {
        String originalString = "!@#$%^&*()_+";
        byte[] originalBytes = originalString.getBytes();
        String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
        byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
        String decodedString = new String(decodedBytes);
        assertEquals(originalString, decodedString);
    }
@Test
    public void base64EncodingDecodingTest7() {
        String originalString = " ";
        byte[] originalBytes = originalString.getBytes();
        String base64String = Base64.byteArrayToBase64(originalBytes);
        byte[] decodedBytes = Base64.base64ToByteArray(base64String);
        String decodedString = new String(decodedBytes);
        assertEquals(originalString, decodedString);
    }
@Test
    public void base64EncodingDecodingTest8() {
        String originalString = "";
        byte[] originalBytes = originalString.getBytes();
        String base64String = Base64.byteArrayToBase64(originalBytes);
        byte[] decodedBytes = Base64.base64ToByteArray(base64String);
        String decodedString = new String(decodedBytes);
        assertEquals(originalString, decodedString);
    }
}