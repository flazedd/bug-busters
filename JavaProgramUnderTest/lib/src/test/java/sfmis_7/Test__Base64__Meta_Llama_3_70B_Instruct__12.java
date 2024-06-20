package sfmis_7;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testBase64EncodingAndDecoding() {
    String originalString = "Hello, World!";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodingAndDecodingWithAltBase64() {
    String originalString = "This is a test string";
    byte[] originalBytes = originalString.getBytes();
    String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodingAndDecodingWithEmptyString() {
    String originalString = "";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodingAndDecodingWithSingleCharacter() {
    String originalString = "a";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodingAndDecodingWithMultipleOfFourBytes() {
    String originalString = "abcdefghijklmnop";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodingAndDecodingWithNonMultipleOfFourBytes() {
    String originalString = "abcdefghi";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodingAndDecodingWithNullInput() {
    byte[] originalBytes = null;
    try {
        Base64.byteArrayToBase64(originalBytes);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected exception
    }
}
@Test
public void testBase64EncodingAndDecodingWithLargeInput() {
    String originalString = "";
    for (int i = 0; i < 1000; i++) {
        originalString += "abcdefghijklmnopqrstuvwxyz";
    }
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
}