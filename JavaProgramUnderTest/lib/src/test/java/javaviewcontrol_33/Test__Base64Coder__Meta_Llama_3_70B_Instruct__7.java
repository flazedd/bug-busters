package javaviewcontrol_33;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__7 {
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
public void testEncodeDecodeSingleCharacter() {
    String original = "a";
    String encoded = Base64Coder.encodeString(original);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
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
    String original = "This is a very large string that needs to be encoded and decoded correctly. It should work even with very large inputs.";
    String encoded = Base64Coder.encodeString(original);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeNull() {
    try {
        Base64Coder.encodeString(null);
        fail("Expected NullPointerException for null input");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testEncodeDecodeWhitespace() {
    String original = "   Hello, World!   ";
    String encoded = Base64Coder.encodeString(original);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(original, decoded);
}
@Test
public void testDecodeNullInput() {
    try {
        Base64Coder.decode((String)null);
        fail("Expected NullPointerException for null input");
    } catch (NullPointerException e) {
        // expected
    }
}
}