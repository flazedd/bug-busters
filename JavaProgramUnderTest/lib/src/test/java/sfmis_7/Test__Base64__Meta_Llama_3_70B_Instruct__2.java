package sfmis_7;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testBase64Encoding() {
    String original = "Hello, World!";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}

@Test
public void testAltBase64Encoding() {
    String original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    byte[] bytes = original.getBytes();
    String altBase64 = Base64.byteArrayToAltBase64(bytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}

@Test
public void testBase64EncodingWithEquals() {
    String original = "Hello";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    assertEquals("SGVsbG8=", base64);
}

@Test
public void testBase64EncodingEmptyString() {
    String original = "";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    assertEquals("", base64);
}

@Test
public void testBase64EncodingNull() {
    byte[] bytes = null;
    try {
        Base64.byteArrayToBase64(bytes);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected
    }
}

@Test
public void testAltBase64EncodingNull() {
    byte[] bytes = null;
    try {
        Base64.byteArrayToAltBase64(bytes);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected
    }
}

@Test
public void testBase64Decoding() {
    String base64 = "SGVsbG8=";
    byte[] bytes = Base64.base64ToByteArray(base64);
    String original = new String(bytes);
    assertEquals("Hello", original);
}

@Test
public void testBase64DecodingInvalidInput() {
    String base64 = "InvalidBase64String";
    try {
        Base64.base64ToByteArray(base64);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // Expected
    }
}

}