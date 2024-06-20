package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testEncodeDecode() {
    String input = "Hello, World!";
    String encoded = Base64Coder.encodeString(input);
    byte[] decoded = Base64Coder.decode(encoded);
    String output = new String(decoded);
    assertEquals(input, output);
}
@Test
public void testEncodeDecodeEmptyString() {
    String input = "";
    String encoded = Base64Coder.encodeString(input);
    byte[] decoded = Base64Coder.decode(encoded);
    String output = new String(decoded);
    assertEquals(input, output);
}
@Test
public void testEncodeDecodeSingleCharacter() {
    String input = "a";
    String encoded = Base64Coder.encodeString(input);
    byte[] decoded = Base64Coder.decode(encoded);
    String output = new String(decoded);
    assertEquals(input, output);
}
@Test
public void testEncodeDecodeLongString() {
    String input = "This is a very long string that will be encoded and decoded by the Base64Coder class.";
    String encoded = Base64Coder.encodeString(input);
    byte[] decoded = Base64Coder.decode(encoded);
    String output = new String(decoded);
    assertEquals(input, output);
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
public void testEncodeNullString() {
    try {
        Base64Coder.encodeString(null);
        fail("Expected NullPointerException for null input string");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testDecodeNullString() {
    try {
        Base64Coder.decodeString(null);
        fail("Expected NullPointerException for null input string");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String input = "!@#$%^&*()_+-=";
    String encoded = Base64Coder.encodeString(input);
    byte[] decoded = Base64Coder.decode(encoded);
    String output = new String(decoded);
    assertEquals(input, output);
}
}