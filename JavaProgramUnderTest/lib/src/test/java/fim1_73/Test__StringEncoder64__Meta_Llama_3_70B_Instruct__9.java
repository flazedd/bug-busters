package fim1_73;
import java.io.ByteArrayOutputStream;
import org.junit.jupiter.api.Test;
import java.io.UnsupportedEncodingException;
import java.io.OutputStream;
import java.util.Arrays;
import java.io.IOException;
import static org.junit.jupiter.api.Assertions.*;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__9 {
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
public void testEncodeDecodeLongString() {
    String originalString = "This is a very long string that needs to be encoded and decoded";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String originalString = "!@#$%^&*()_+-=";
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
        // Expected
    }
}
@Test
public void testEncodeDecodeLargeString() {
    StringBuilder originalStringBuilder = new StringBuilder();
    for (int i = 0; i < 1000; i++) {
        originalStringBuilder.append("This is a large string that needs to be encoded and decoded ");
    }
    String originalString = originalStringBuilder.toString();
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testDecodeInvalidBase64String() {
    String invalidBase64String = "This is not a valid Base64 string";
    try {
        StringEncoder64.decodeStringUTF8(invalidBase64String);
        fail("Expected RuntimeException to be thrown");
    } catch (RuntimeException e) {
        // Expected
    }
}
}