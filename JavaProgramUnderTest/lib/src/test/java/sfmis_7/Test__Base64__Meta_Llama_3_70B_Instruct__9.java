package sfmis_7;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testBase64() {
    String original = "Hello, World!";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testBase64WithAlt() {
    String original = "Hello, World!";
    byte[] bytes = original.getBytes();
    String altBase64 = Base64.byteArrayToAltBase64(bytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testBase64WithEmptyString() {
    String original = "";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testBase64WithNull() {
    byte[] bytes = null;
    try {
        Base64.byteArrayToBase64(bytes);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected
    }
}
@Test
public void testBase64WithInvalidInput() {
    String invalidBase64 = "Invalid Base64 string";
    try {
        Base64.base64ToByteArray(invalidBase64);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // Expected
    }
}
@Test
public void testBase64WithLargeInput() {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < 1000; i++) {
        sb.append("Hello, World!");
    }
    String original = sb.toString();
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testBase64WithWhitespace() {
    String original = "Hello, World!";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    String base64WithWhitespace = base64.replace("=", " = ").replace("/", " / ");
    try {
        Base64.base64ToByteArray(base64WithWhitespace);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // Expected
    }
}
@Test
public void testBase64WithMultipleLines() {
    String original = "Hello, World!";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    String base64WithMultipleLines = base64.substring(0, 10) + "\n" + base64.substring(10);
    try {
        Base64.base64ToByteArray(base64WithMultipleLines);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // Expected
    }
}
}