package fim1_73;
import org.junit.jupiter.api.Test;
import java.io.UnsupportedEncodingException;
import java.io.IOException;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testEncodeAndDecode() {
    String input = "Hello, World!";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeAndDecodeEmptyString() {
    String input = "";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeAndDecodeSingleCharacter() {
    String input = "a";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeAndDecodeMultipleLines() {
    String input = "Hello,\nWorld!";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeAndDecodeSpecialCharacters() {
    String input = "!@#$%^&*()_+-=";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeAndDecodeLargeString() {
    String input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
@Test
public void testEncodeAndDecodeNullInput() {
    String input = null;
    try {
        StringEncoder64.encodeStringUTF8(input);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testEncodeAndDecodeWhiteSpace() {
    String input = "   ";
    String encoded = StringEncoder64.encodeStringUTF8(input);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(input, decoded);
}
}