package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testBase64EncodeDecode() {
    String originalString = "Hello, World!";
    String encodedString = Base64Coder.encodeString(originalString);
    String decodedString = new String(Base64Coder.decode(encodedString));
    assertEquals(originalString, decodedString);
}

@Test
public void testBase64EncodeDecodeByteArray() {
    byte[] originalBytes = {1, 2, 3, 4, 5};
    char[] encodedBytes = Base64Coder.encode(originalBytes);
    byte[] decodedBytes = Base64Coder.decode(new String(encodedBytes));
    assertArrayEquals(originalBytes, decodedBytes);
}

@Test
public void testBase64EncodeDecodeEmptyString() {
    String originalString = "";
    String encodedString = Base64Coder.encodeString(originalString);
    String decodedString = new String(Base64Coder.decode(encodedString));
    assertEquals(originalString, decodedString);
}

@Test
public void testBase64EncodeDecodeNull() {
    String originalString = null;
    try {
        Base64Coder.encodeString(originalString);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}

@Test
public void testBase64DecodeInvalidInput() {
    String invalidInput = "Invalid Base64 input";
    try {
        Base64Coder.decode(invalidInput);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}

@Test
public void testBase64EncodeDecodeLargeString() {
    String originalString = "This is a very large string that will be encoded and decoded using Base64.";
    String encodedString = Base64Coder.encodeString(originalString);
    String decodedString = new String(Base64Coder.decode(encodedString));
    assertEquals(originalString, decodedString);
}

@Test
public void testBase64EncodeDecodeWithPadding() {
    String originalString = "Hello";
    String encodedString = Base64Coder.encodeString(originalString);
    assertEquals("SGVsbG8=", encodedString);
    String decodedString = new String(Base64Coder.decode(encodedString));
    assertEquals(originalString, decodedString);
}

@Test
public void testBase64EncodeDecodeUnicodeCharacters() {
    String originalString = "Hello, \u00A5!";
    String encodedString = Base64Coder.encodeString(originalString);
    String decodedString = new String(Base64Coder.decode(encodedString));
    assertEquals(originalString, decodedString);
}

}