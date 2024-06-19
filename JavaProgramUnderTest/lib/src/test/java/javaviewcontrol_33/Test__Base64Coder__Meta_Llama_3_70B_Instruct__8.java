package javaviewcontrol_33;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testEncodeDecode() {
    String original = "Hello, World!";
    String encoded = Base64Coder.encodeString(original);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeEmptyString() {
    String original = "";
    String encoded = Base64Coder.encodeString(original);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeNullByte() {
    byte[] original = new byte[] {0, 1, 2, 0, 3, 4, 5};
    String encoded = new String(Base64Coder.encode(original));
    byte[] decodedBytes = Base64Coder.decode(encoded);
    assertArrayEquals(original, decodedBytes);
}
@Test
public void testDecodeInvalidBase64() {
    String invalidBase64 = "Invalid Base64 string";
    try {
        Base64Coder.decode(invalidBase64);
        fail("Expected IllegalArgumentException for invalid Base64 string");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testEncodeDecodeLargeString() {
    String original = "";
    for (int i = 0; i < 1000; i++) {
        original += "abcdefghijklmnopqrstuvwxyz";
    }
    String encoded = Base64Coder.encodeString(original);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeWhitespace() {
    String original = "   Hello   World!   ";
    String encoded = Base64Coder.encodeString(original);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String original = "!@#$%^&*()_+-={}:<>?";
    String encoded = Base64Coder.encodeString(original);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testDecodeWithPadding() {
    String encoded = "SGVsbG8sIFdvcmxkIQ==";
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals("Hello, World!", decoded);
}
}