package sfmis_7;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64__Meta_Llama_3_70B_Instruct__4 {
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
public void base64EncodingDecodingTestWithAlt() {
    String originalString = "This is a test string.";
    byte[] originalBytes = originalString.getBytes();
    String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingTestWithEmptyString() {
    String originalString = "";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingTestWithSingleCharacter() {
    String originalString = "a";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingTestWithMultipleLines() {
    String originalString = "This is a test string.\nIt has multiple lines.";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingTestWithSpecialCharacters() {
    String originalString = "!@#$%^&*()_+-=";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingTestWithLongString() {
    String originalString = "This is a very long test string that will require multiple chunks of base64 encoding.";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingTestWithNullInput() {
    byte[] originalBytes = null;
    try {
        Base64.byteArrayToBase64(originalBytes);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
}