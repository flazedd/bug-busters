package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testBase64EncodeDecode() {
    String originalString = "Hello, World!";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodeDecodeEmptyString() {
    String originalString = "";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodeDecodeSingleCharacter() {
    String originalString = "a";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
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
public void testBase64EncodeDecodeLargeString() {
    String originalString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64DecodeInvalidInput() {
    String invalidInput = "Invalid Base64 string";
    try {
        Base64Coder.decode(invalidInput);
        fail("Expected IllegalArgumentException");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testBase64EncodeDecodeSpecialCharacters() {
    String originalString = "!@#$%^&*()_+-=";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
@Test
public void testBase64EncodeDecodeMultipleLines() {
    String originalString = "This is a test string\nwith multiple lines.";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}
}