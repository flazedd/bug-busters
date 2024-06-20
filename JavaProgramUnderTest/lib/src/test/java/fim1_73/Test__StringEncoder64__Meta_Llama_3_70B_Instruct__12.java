package fim1_73;
import java.util.Arrays;
import java.io.OutputStream;
import static org.junit.jupiter.api.Assertions.*;
import java.io.UnsupportedEncodingException;
import org.junit.jupiter.api.Test;
import java.io.IOException;
import java.io.ByteArrayOutputStream;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__12 {
@Test
public void encodeDecodeTest() {
    String originalString = "Hello, World!";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void encodeDecodeEmptyStringTest() {
    String originalString = "";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void encodeDecodeSingleCharacterTest() {
    String originalString = "a";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void encodeDecodeMultipleBytesTest() {
    String originalString = "abcdefghijklmnopqrstuvwxyz";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void encodeDecodeWhitespaceTest() {
    String originalString = "   ";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void encodeDecodeNullInputTest() {
    String originalString = null;
    try {
        String encodedString = StringEncoder64.encodeStringUTF8(originalString);
        fail("Expected NullPointerException for null input");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void encodeDecodeVeryLongStringTest() {
    StringBuilder originalStringBuilder = new StringBuilder();
    for (int i = 0; i < 1000; i++) {
        originalStringBuilder.append("abcdefghijklmnopqrstuvwxyz");
    }
    String originalString = originalStringBuilder.toString();
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
@Test
public void encodeDecodeSpecialCharactersTest() {
    String originalString = "!@#$%^&*()_+-=";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}
}