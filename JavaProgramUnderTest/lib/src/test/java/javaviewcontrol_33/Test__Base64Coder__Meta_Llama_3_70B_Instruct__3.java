package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testEncodeDecode() {
    String original = "Hello, World!";
    String encoded = Base64Coder.encodeString(original);
    byte[] decoded = Base64Coder.decode(encoded);
    String decodedString = new String(decoded);
    assertEquals(original, decodedString);
}

@Test
public void testEncodeDecodeEmptyString() {
    String original = "";
    String encoded = Base64Coder.encodeString(original);
    byte[] decoded = Base64Coder.decode(encoded);
    String decodedString = new String(decoded);
    assertEquals(original, decodedString);
}

@Test
public void testEncodeDecodeNull() {
    String original = null;
    try {
        Base64Coder.encodeString(original);
        fail("Expected NullPointerException to be thrown");
    } catch (NullPointerException e) {
        // expected
    }
}

@Test
public void testEncodeDecodeSingleCharacter() {
    String original = "a";
    String encoded = Base64Coder.encodeString(original);
    byte[] decoded = Base64Coder.decode(encoded);
    String decodedString = new String(decoded);
    assertEquals(original, decodedString);
}

@Test
public void testDecodeInvalidBase64() {
    String invalidBase64 = " invalid_base64_string ";
    try {
        Base64Coder.decode(invalidBase64);
        fail("Expected IllegalArgumentException to be thrown");
    } catch (IllegalArgumentException e) {
        // expected
    }
}

@Test
public void testEncodeDecodeLongString() {
    String original = "This is a very long string that needs to be encoded and decoded";
    String encoded = Base64Coder.encodeString(original);
    byte[] decoded = Base64Coder.decode(encoded);
    String decodedString = new String(decoded);
    assertEquals(original, decodedString);
}

@Test
public void testEncodeDecodeMultipleBytes() {
    byte[] originalBytes = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x10};
    char[] encodedChars = Base64Coder.encode(originalBytes);
    String encodedString = new String(encodedChars);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    assertArrayEquals(originalBytes, decodedBytes);
}

@Test
public void testEncodeDecodeWhitespace() {
    String original = "   Hello   World!   ";
    String encoded = Base64Coder.encodeString(original);
    byte[] decoded = Base64Coder.decode(encoded);
    String decodedString = new String(decoded);
    assertEquals(original, decodedString);
}

}