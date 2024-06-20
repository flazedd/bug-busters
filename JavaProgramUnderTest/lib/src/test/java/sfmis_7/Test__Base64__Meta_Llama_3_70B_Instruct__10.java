package sfmis_7;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testBase64Encoding() {
    String input = "Hello, World!";
    byte[] bytes = input.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decodedString = new String(decodedBytes);
    assertEquals(input, decodedString);
}
@Test
public void testBase64EncodingWithAltCharset() {
    String input = "Hello, World!";
    byte[] bytes = input.getBytes();
    String altBase64 = Base64.byteArrayToAltBase64(bytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64);
    String decodedString = new String(decodedBytes);
    assertEquals(input, decodedString);
}
@Test
public void testBase64EncodingWithEmptyString() {
    String input = "";
    byte[] bytes = input.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    assertEquals("", base64);
}
@Test
public void testBase64EncodingWithNullInput() {
    byte[] bytes = null;
    try {
        Base64.byteArrayToBase64(bytes);
        fail("Expected NullPointerException to be thrown");
    } catch (NullPointerException e) {
        // Expected
    }
}
@Test
public void testBase64EncodingWithLargeInput() {
    String input = new String(new char[10000]).replace('\0', 'a');
    byte[] bytes = input.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decodedString = new String(decodedBytes);
    assertEquals(input, decodedString);
}
@Test
public void testBase64EncodingWithInvalidInput() {
    String input = "Invalid base64 string";
    try {
        Base64.base64ToByteArray(input);
        fail("Expected IllegalArgumentException to be thrown");
    } catch (IllegalArgumentException e) {
        // Expected
    }
}
@Test
public void testAltBase64EncodingWithSameInput() {
    String input = "Hello, World!";
    byte[] bytes = input.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    String altBase64 = Base64.byteArrayToAltBase64(bytes);
    assertNotEquals(base64, altBase64);
}
@Test
public void testBase64EncodingWithNonAsciiCharacters() {
    String input = "Hello, Welt!";
    byte[] bytes = input.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decodedString = new String(decodedBytes);
    assertEquals(input, decodedString);
}
}