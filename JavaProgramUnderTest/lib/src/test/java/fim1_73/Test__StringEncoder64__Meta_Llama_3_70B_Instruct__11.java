package fim1_73;
import java.util.Arrays;
import java.io.OutputStream;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
import org.junit.jupiter.api.Test;
import java.io.IOException;
import java.io.ByteArrayOutputStream;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__11 {
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
    String originalString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeNullString() {
    String originalString = null;
    try {
        StringEncoder64.encodeStringUTF8(originalString);
        fail("Expected NullPointerException to be thrown");
    } catch (NullPointerException e) {
        // Expected behavior
    }
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String originalString = "!@#$%^&*()_+-={}|[]:;<>?,./";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeWhitespace() {
    String originalString = "   \t\n\r";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeRepeatedCharacters() {
    String originalString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
}