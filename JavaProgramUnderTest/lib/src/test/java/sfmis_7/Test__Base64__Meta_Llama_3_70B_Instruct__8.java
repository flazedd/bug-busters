package sfmis_7;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64__Meta_Llama_3_70B_Instruct__8 {
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
public void base64EncodingDecodingWithAltTest() {
    String originalString = "This is a test string";
    byte[] originalBytes = originalString.getBytes();
    String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithEmptyStringTest() {
    String originalString = "";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithNullTest() {
    byte[] originalBytes = null;
    try {
        String base64String = Base64.byteArrayToBase64(originalBytes);
        fail("Expected NullPointerException to be thrown");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void base64EncodingDecodingWithLargeStringTest() {
    String originalString = new String(new char[10000]).replace('\0', 'a');
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithSpaceTest() {
    String originalString = "Hello World";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithNonAsciiCharactersTest() {
    String originalString = "Hello, Welt!";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithByteArrayOfLengthOneTest() {
    byte[] originalBytes = new byte[] { 0x01 };
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    assertArrayEquals(originalBytes, decodedBytes);
}
}