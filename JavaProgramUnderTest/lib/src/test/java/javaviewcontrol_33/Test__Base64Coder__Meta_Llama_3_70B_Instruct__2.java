package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__2 {
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
public void testEncodeDecodeNullBytes() {
    byte[] original = new byte[] { 0, 0, 0, 0, 0 };
    char[] encodedChars = Base64Coder.encode(original);
    String encoded = new String(encodedChars);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    assertArrayEquals(original, decodedBytes);
}
@Test
public void testEncodeDecodeHelloWorld() {
    String originalString = "Hello, World!";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

@Test
public void testEncodeDecodeSingleCharacter() {
    String originalString = "a";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

@Test
public void testEncodeDecodeSpecialCharacters() {
    String originalString = "!@#$%^&*()";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

@Test
public void testEncodeDecodeNonAsciiCharacters() {
    String originalString = "Übermensch";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

@Test
public void testEncodeDecodeLongString() {
    String originalString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
    String encodedString = Base64Coder.encodeString(originalString);
    byte[] decodedBytes = Base64Coder.decode(encodedString);
    String decodedString = new String(decodedBytes);
    assertEquals(originalString, decodedString);
}

}