package fim1_73;
import java.util.Arrays;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
import java.io.OutputStream;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testEncodeDecode() {
    String originalString = "Hello, World!";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeEmptyString() {
    String originalString = "";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeSingleCharacter() {
    String originalString = "a";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeLargeString() {
    String originalString = "This is a very large string that needs to be encoded and decoded correctly.";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String originalString = "!@#$%^&*()_+-={}:<>?";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeNullString() {
    String originalString = null;
    try {
        StringEncoder64.encodeStringUTF8(originalString);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected exception
    }
}
@Test
public void testEncodeDecodeWhiteSpace() {
    String originalString = "   ";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeBinaryData() {
    byte[] binaryData = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x10};
    String encodedString = StringEncoder64.encode(binaryData);
    byte[] decodedData = StringEncoder64.decode(encodedString);
    assertArrayEquals(binaryData, decodedData);
}
}