package sfmis_7;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64__Meta_Llama_3_70B_Instruct__1 {
@Test
public void base64Test() {
    String original = "Hello, World!";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}

@Test
public void altBase64Test() {
    String original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    byte[] bytes = original.getBytes();
    String altBase64 = Base64.byteArrayToAltBase64(bytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}

@Test
public void base64TestWithEquals() {
    String original = "1234567890";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    assertEquals("MTIzNDU2Nzg5MA==", base64);
}

@Test
public void base64TestWithSingleCharacter() {
    String original = "a";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    assertEquals("YQ==", base64);
}

@Test
public void base64TestWithEmptyString() {
    String original = "";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    assertEquals("", base64);
}

@Test
public void base64TestWithNullInput() {
    try {
        Base64.base64ToByteArray(null);
        fail("Expected NullPointerException for null input");
    } catch (NullPointerException e) {
        // Expected exception
    }
}

@Test
public void altBase64TestWithLargeInput() {
    String original = new String(new char[1000]).replace("\0", "ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    byte[] bytes = original.getBytes();
    String altBase64 = Base64.byteArrayToAltBase64(bytes);
    byte[] decodedBytes = Base64.altBase64ToByteArray(altBase64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}

@Test
public void base64TestWithWhitespace() {
    String original = "Hello World!";
    byte[] bytes = original.getBytes();
    String base64 = Base64.byteArrayToBase64(bytes);
    byte[] decodedBytes = Base64.base64ToByteArray(base64);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}

}