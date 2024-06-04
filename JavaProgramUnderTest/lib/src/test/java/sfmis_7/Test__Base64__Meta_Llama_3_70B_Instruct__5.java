package sfmis_7;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__Base64__Meta_Llama_3_70B_Instruct__5 {
@Test
public void base64EncodingDecoding() {
    String originalString = "Hello, World!";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithAltBase64() {
    String originalString = "This is a test string";
    byte[] originalBytes = originalString.getBytes();
    String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithEmptyString() {
    String originalString = "";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithSingleCharacter() {
    String originalString = "a";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithMultipleLines() {
    String originalString = "This is a test string that spans multiple lines.\nIt has multiple sentences.";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithSpecialCharacters() {
    String originalString = "!@#$%^&*()_+-={}:<>?";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithLargeString() {
    StringBuilder originalStringBuilder = new StringBuilder();
    for (int i = 0; i < 1000; i++) {
        originalStringBuilder.append("This is a test string ");
    }
    String originalString = originalStringBuilder.toString();
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void base64EncodingDecodingWithNullInput() {
    try {
        Base64.byteArrayToBase64(null);
        fail("Expected NullPointerException for null input");
    } catch (NullPointerException e) {
        // Expected
    }
}
}