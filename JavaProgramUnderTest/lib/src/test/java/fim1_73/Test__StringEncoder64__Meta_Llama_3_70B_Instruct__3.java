package fim1_73;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testEncodeDecode() {
    String original = "Hello, World!";
    String encoded = StringEncoder64.encodeStringUTF8(original);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(original, decoded);
}

@Test
public void testEncodeDecodeEmptyString() {
    String original = "";
    String encoded = StringEncoder64.encodeStringUTF8(original);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(original, decoded);
}

@Test
public void testEncodeDecodeSingleByte() {
    String original = "a";
    String encoded = StringEncoder64.encodeStringUTF8(original);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(original, decoded);
}

@Test
public void testEncodeDecodeMultiByte() {
    String original = "abcdef";
    String encoded = StringEncoder64.encodeStringUTF8(original);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(original, decoded);
}

@Test
public void testEncodeDecodeNull() {
    String original = null;
    try {
        StringEncoder64.encodeStringUTF8(original);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}

@Test
public void testEncodeDecodeLargeString() {
    String original = "";
    for (int i = 0; i < 1000; i++) {
        original += "abcdefghijklmnopqrstuvwxyz";
    }
    String encoded = StringEncoder64.encodeStringUTF8(original);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(original, decoded);
}

@Test
public void testEncodeDecodeSpecialChars() {
    String original = "!@#$%^&*()_+-=[]{};':,.<>?/";
    String encoded = StringEncoder64.encodeStringUTF8(original);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(original, decoded);
}

@Test
public void testEncodeDecodeWhitespace() {
    String original = "   \t\n\r";
    String encoded = StringEncoder64.encodeStringUTF8(original);
    String decoded = StringEncoder64.decodeStringUTF8(encoded);
    assertEquals(original, decoded);
}

}