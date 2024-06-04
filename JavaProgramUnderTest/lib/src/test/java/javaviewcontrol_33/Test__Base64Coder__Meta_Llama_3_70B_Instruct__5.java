package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__5 {
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
public void testEncodeDecodeNull() {
    String original = null;
    try {
        Base64Coder.encodeString(original);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testDecodeInvalidBase64() {
    String invalidBase64 = "Invalid Base64 string";
    try {
        Base64Coder.decode(invalidBase64);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testEncodeDecodeSingleByte() {
    String original = "a";
    String encoded = Base64Coder.encodeString(original);
    String decoded = new String(Base64Coder.decode(encoded));
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeLongString() {
    String original = "This is a very long string that needs to be encoded and decoded correctly.";
    String encoded = Base64Coder.encodeString(original);
    String decoded = new String(Base64Coder.decode(encoded));
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String original = "!@#$%^&*()_+-=";
    String encoded = Base64Coder.encodeString(original);
    String decoded = new String(Base64Coder.decode(encoded));
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeWhitespace() {
    String original = "   \t\n\r  ";
    String encoded = Base64Coder.encodeString(original);
    String decoded = new String(Base64Coder.decode(encoded));
    assertEquals(original, decoded);
}
}