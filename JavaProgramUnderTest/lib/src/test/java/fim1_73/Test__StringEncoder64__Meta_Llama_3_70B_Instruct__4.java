package fim1_73;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;
import java.io.IOException;
import org.junit.jupiter.api.Test;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__4 {
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
    String originalString = "This is a very long string that will be encoded and decoded";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String originalString = "!@#$%^&*()_+-={};:<>?,./~\"";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void testEncodeDecodeNullString() {
    String originalString = null;
    try {
        String encodedString = StringEncoder64.encodeStringUTF8(originalString);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testDecodeInvalidBase64String() {
    String invalidBase64String = "Invalid Base64 string";
    try {
        String decodedString = StringEncoder64.decodeStringUTF8(invalidBase64String);
        fail("Expected RuntimeException");
    } catch (RuntimeException e) {
        // expected
    }
}
@Test
public void testEncodeDecodeLargeString() {
    StringBuilder originalStringBuilder = new StringBuilder();
    for (int i = 0; i < 10000; i++) {
        originalStringBuilder.append("Hello, World!");
    }
    String originalString = originalStringBuilder.toString();
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
}