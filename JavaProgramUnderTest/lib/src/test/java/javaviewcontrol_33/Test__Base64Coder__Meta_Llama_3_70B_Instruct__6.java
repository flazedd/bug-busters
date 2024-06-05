package javaviewcontrol_33;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testBase64EncodeDecode() {
    String input = "Hello, World!";
    String encoded = Base64Coder.encodeString(input);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(input, decoded);
}
@Test
public void testBase64EncodeDecodeEmptyString() {
    String input = "";
    String encoded = Base64Coder.encodeString(input);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(input, decoded);
}
@Test
public void testBase64EncodeDecodeNullByte() {
    byte[] input = {0, 1, 2, 0, 3, 4, 5, 0};
    String encoded = Base64Coder.encodeString(new String(input));
    byte[] decodedBytes = Base64Coder.decode(encoded);
    assertArrayEquals(input, decodedBytes);
}
@Test
public void testBase64EncodeDecodeLargeString() {
    String input = "";
    for (int i = 0; i < 1000; i++) {
        input += "Hello, World!";
    }
    String encoded = Base64Coder.encodeString(input);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(input, decoded);
}
@Test
public void testBase64EncodeDecodeSingleCharacter() {
    String input = "a";
    String encoded = Base64Coder.encodeString(input);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(input, decoded);
}
@Test
public void testBase64EncodeDecodeWhitespace() {
    String input = "   \t\n";
    String encoded = Base64Coder.encodeString(input);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(input, decoded);
}
@Test
public void testBase64EncodeDecodeSpecialCharacters() {
    String input = "!@#$%^&*()_+-=";
    String encoded = Base64Coder.encodeString(input);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(input, decoded);
}
@Test
public void testBase64EncodeDecodeUtf8Characters() {
    String input = "üöäÜÖÄ";
    String encoded = Base64Coder.encodeString(input);
    byte[] decodedBytes = Base64Coder.decode(encoded);
    String decoded = new String(decodedBytes);
    assertEquals(input, decoded);
}
}