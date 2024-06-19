package fim1_73;
import java.io.UnsupportedEncodingException;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.io.IOException;
import java.io.OutputStream;
import java.io.ByteArrayOutputStream;
import java.util.Arrays;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__7 {
@Test
public void testEncodeDecode() {
    String input = "Hello, World!";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeDecodeEmptyString() {
    String input = "";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeDecodeSingleCharacter() {
    String input = "a";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeDecodeLongString() {
    String input = "This is a very long string that needs to be encoded and decoded correctly";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeDecodeNull() {
    String input = null;
    try {
        StringEncoder64.encodeStringUTF8(input);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected
    }
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String input = "!@#$%^&*()_+-=";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeDecodeWhitespace() {
    String input = "   \t\n\r";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeDecodeBoundaryCase() {
    String input = "abcd";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
}