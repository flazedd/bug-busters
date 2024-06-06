package javaviewcontrol_33;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testEncodeDecode() {
    String original = "Hello, World!";
    String encoded = Base64Coder.encodeString(original);
    String decoded = Base64Coder.decodeString(encoded);
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeEmptyString() {
    String original = "";
    String encoded = Base64Coder.encodeString(original);
    String decoded = Base64Coder.decodeString(encoded);
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeNullByte() {
    byte[] original = new byte[] {0, 1, 2, 3, 4, 5, 6, 7, 8, 0};
    String encoded = new String(Base64Coder.encode(original));
    byte[] decoded = Base64Coder.decode(encoded);
    assertArrayEquals(original, decoded);
}
@Test
public void testEncodeDecodeLargeString() {
    String original = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
    String encoded = Base64Coder.encodeString(original);
    String decoded = Base64Coder.decodeString(encoded);
    assertEquals(original, decoded);
}
@Test
public void testDecodeInvalidBase64() {
    String invalidBase64 = "ABCDEFG";
    try {
        Base64Coder.decodeString(invalidBase64);
        fail("Should throw IllegalArgumentException for invalid Base64 input");
    } catch (IllegalArgumentException e) {
        // expected
    }
}
@Test
public void testEncodeDecodeByteArray() {
    byte[] original = new byte[] {65, 66, 67, 68, 69, 70, 71, 72, 73, 74};
    String encoded = new String(Base64Coder.encode(original));
    byte[] decoded = Base64Coder.decode(encoded);
    assertArrayEquals(original, decoded);
}
@Test
public void testEncodeDecodeSingleByte() {
    byte[] original = new byte[] {65};
    String encoded = new String(Base64Coder.encode(original));
    byte[] decoded = Base64Coder.decode(encoded);
    assertArrayEquals(original, decoded);
}
@Test
public void testEncodeDecodeMultipleLines() {
    String original = "This is a test string that spans multiple lines.\n"
                     + "It should be encoded and decoded correctly.";
    String encoded = Base64Coder.encodeString(original);
    String decoded = Base64Coder.decodeString(encoded);
    assertEquals(original, decoded);
}
}