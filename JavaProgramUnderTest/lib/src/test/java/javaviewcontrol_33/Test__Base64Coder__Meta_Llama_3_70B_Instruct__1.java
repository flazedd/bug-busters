package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__1 {
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
    assertEquals("", encoded);
}

@Test
public void testDecodeNullInput() {
    try {
        Base64Coder.decode((String)null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
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
public void testDecodeInvalidBase64() {
    try {
        Base64Coder.decode("Invalid Base64 string");
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}

@Test
public void testEncodeDecodeLargeString() {
    String input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
    String encoded = Base64Coder.encodeString(input);
    byte[] decoded = Base64Coder.decode(encoded);
    String output = new String(decoded);
    assertEquals(input, output);
}

@Test
public void testEncodeDecodeByteArray() {
    byte[] input = {1, 2, 3, 4, 5};
    char[] encoded = Base64Coder.encode(input);
    byte[] decoded = Base64Coder.decode(new String(encoded));
    assertArrayEquals(input, decoded);
}

@Test
public void testEncodeDecodeWhitespace() {
    String input = "   Hello, World!   ";
    String encoded = Base64Coder.encodeString(input);
    byte[] decoded = Base64Coder.decode(encoded);
    String output = new String(decoded);
    assertEquals(input, output);
}







}