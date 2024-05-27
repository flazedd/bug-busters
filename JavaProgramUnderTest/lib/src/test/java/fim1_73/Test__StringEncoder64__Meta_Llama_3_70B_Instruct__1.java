package fim1_73;
import java.io.UnsupportedEncodingException;
import org.junit.jupiter.api.Test;
import java.io.IOException;
import static org.junit.jupiter.api.Assertions.*;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__1 {
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
public void testEncodeDecodeNonASCIICharacters() {
    String originalString = "Hello, Übermensch!";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}

@Test
public void testEncodeDecodeLargeString() {
    String originalString = new String(new char[1000]).replace("\0", "a");
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
public void testEncodeDecodeWhitespace() {
    String originalString = "   \t\n\r ";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}

@Test
public void testDecodeNullInput() {
    String invalidInput = null;
    try {
        String decodedString = StringEncoder64.decodeStringUTF8(invalidInput);
        fail("Expected NullPointerException for null input");
    } catch (NullPointerException e) {
        // expected
    }
}

}