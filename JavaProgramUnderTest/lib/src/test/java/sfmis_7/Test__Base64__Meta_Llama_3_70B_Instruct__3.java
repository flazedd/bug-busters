package sfmis_7;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testBase64Encoding() {
    String originalString = "Hello, World!";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

@Test
public void testAltBase64Encoding() {
    String originalString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    byte[] originalBytes = originalString.getBytes();
    String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

@Test
public void testBase64EncodingWithEquals() {
    String originalString = "Hello";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    assertEquals(base64String.endsWith("="), true);
}

@Test
public void testBase64EncodingWithShortInput() {
    String originalString = "";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    assertEquals(base64String, "");
}

@Test
public void testBase64EncodingWithSingleCharacter() {
    String originalString = "a";
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    assertEquals(base64String, "YQ==");
}

@Test
public void testBase64EncodingWithNullInput() {
    try {
        Base64.byteArrayToBase64(null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected
    }
}

@Test
public void testAltBase64EncodingWithMultipleCharacters() {
    String originalString = "abcdef";
    byte[] originalBytes = originalString.getBytes();
    String altBase64String = Base64.byteArrayToAltBase64(originalBytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

@Test
public void testBase64EncodingWithLargeInput() {
    String originalString = new String(new char[1000]).replace("\0", "a");
    byte[] originalBytes = originalString.getBytes();
    String base64String = Base64.byteArrayToBase64(originalBytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64String);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

}