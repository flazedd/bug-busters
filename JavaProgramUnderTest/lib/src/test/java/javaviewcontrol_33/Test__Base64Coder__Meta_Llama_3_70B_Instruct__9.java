package javaviewcontrol_33;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testEncodeDecode() {
    String original = "Hello, World!";
    String encoded = Base64Coder.encodeString(original);
    String decoded = new String(Base64Coder.decode(encoded));
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeEmptyString() {
    String original = "";
    String encoded = Base64Coder.encodeString(original);
    String decoded = new String(Base64Coder.decode(encoded));
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeNullBytes() {
    byte[] original = new byte[0];
    char[] encoded = Base64Coder.encode(original);
    byte[] decoded = Base64Coder.decode(new String(encoded));
    assertArrayEquals(original, decoded);
}
@Test
public void testDecodeInvalidBase64() {
    String invalidBase64 = "Invalid Base64 string";
    try {
        Base64Coder.decode(invalidBase64);
        fail("Expected IllegalArgumentException for invalid Base64 string");
    } catch (IllegalArgumentException e) {
        // Expected exception
    }
}
@Test
public void testEncodeDecodeSingleByte() {
    byte[] original = new byte[] { 0x12 };
    char[] encoded = Base64Coder.encode(original);
    byte[] decoded = Base64Coder.decode(new String(encoded));
    assertArrayEquals(original, decoded);
}
@Test
public void testEncodeDecodeMultipleBytes() {
    byte[] original = new byte[] { 0x12, 0x34, 0x56, 0x78 };
    char[] encoded = Base64Coder.encode(original);
    byte[] decoded = Base64Coder.decode(new String(encoded));
    assertArrayEquals(original, decoded);
}
@Test
public void testEncodeDecodeLargeByteArray() {
    byte[] original = new byte[1024];
    for (int i = 0; i < 1024; i++) {
        original[i] = (byte) (i % 256);
    }
    char[] encoded = Base64Coder.encode(original);
    byte[] decoded = Base64Coder.decode(new String(encoded));
    assertArrayEquals(original, decoded);
}
@Test
public void testDecodeBase64StringWithPadding() {
    String base64String = "SGVsbG8sIFdvcmxkIQ==";
    byte[] decoded = Base64Coder.decode(base64String);
    String decodedString = new String(decoded);
    assertEquals("Hello, World!", decodedString);
}
}