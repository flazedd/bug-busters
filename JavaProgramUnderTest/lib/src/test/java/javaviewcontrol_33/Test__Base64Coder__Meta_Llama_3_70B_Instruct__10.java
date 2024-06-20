package javaviewcontrol_33;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__10 {
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
public void testEncodeDecodeNullString() {
    String original = null;
    try {
        Base64Coder.encodeString(original);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testEncodeDecodeSingleCharacter() {
    String original = "a";
    String encoded = Base64Coder.encodeString(original);
    String decoded = Base64Coder.decodeString(encoded);
    assertEquals(original, decoded);
}
@Test
public void testDecodeNullByteArray() {
    try {
        Base64Coder.decode((char[]) null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testEncodeByteArray() {
    byte[] original = {1, 2, 3, 4, 5};
    char[] encoded = Base64Coder.encode(original);
    byte[] decoded = Base64Coder.decode(new String(encoded));
    assertArrayEquals(original, decoded);
}
@Test
public void testEncodeDecodeLargeString() {
    String original = new String(new char[1000]).replace("\0", "abc");
    String encoded = Base64Coder.encodeString(original);
    String decoded = Base64Coder.decodeString(encoded);
    assertEquals(original, decoded);
}
@Test
public void testEncodeDecodeWhitespace() {
    String original = "   Hello, World!   ";
    String encoded = Base64Coder.encodeString(original);
    String decoded = Base64Coder.decodeString(encoded);
    assertEquals(original, decoded);
}
}