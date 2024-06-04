package fim1_73;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import static org.junit.jupiter.api.Assertions.*;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.io.OutputStream;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__5 {
@Test
public void testEncodeDecode() {
    String data = "Hello, World!";
    String encoded = StringEncoder64.encodeStringUTF8(data);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(data, decoded);
}
@Test
public void testEncodeDecodeEmptyString() {
    String data = "";
    String encoded = StringEncoder64.encodeStringUTF8(data);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(data, decoded);
}
@Test
public void testEncodeDecodeSingleCharacter() {
    String data = "a";
    String encoded = StringEncoder64.encodeStringUTF8(data);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(data, decoded);
}
@Test
public void testEncodeDecodeLargeString() {
    String data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.";
    String encoded = StringEncoder64.encodeStringUTF8(data);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(data, decoded);
}
@Test
public void testEncodeDecodeNull() {
    String data = null;
    try {
        StringEncoder64.encodeStringUTF8(data);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testEncodeDecodeWhitespace() {
    String data = "   ";
    String encoded = StringEncoder64.encodeStringUTF8(data);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(data, decoded);
}
@Test
public void testEncodeDecodeSpecialCharacters() {
    String data = "!@#$%^&*()_+-=";
    String encoded = StringEncoder64.encodeStringUTF8(data);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(data, decoded);
}
@Test
public void testEncodeDecodeMultiByteCharacters() {
    String data = "abcdefabcde";
    String encoded = StringEncoder64.encodeStringUTF8(data);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(data, decoded);
}
}