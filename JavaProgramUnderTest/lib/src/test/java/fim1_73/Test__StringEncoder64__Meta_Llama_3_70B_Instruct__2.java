package fim1_73;
import java.io.OutputStream;
import java.io.ByteArrayOutputStream;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
public class Test__StringEncoder64__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testEncodeAndDecode() {
    String originalString = "Hello, World!";
    String encodedString = StringEncoder64.encodeStringUTF8(originalString);
    String decodedString = StringEncoder64.decodeStringUTF8(encodedString);
    assertEquals(originalString, decodedString);
}

@Test
public void testEncodeByteArray() {
    byte[] originalBytes = {1, 2, 3, 4, 5};
    String encodedString = StringEncoder64.encode(originalBytes);
    byte[] decodedBytes = StringEncoder64.decode(encodedString);
    assertArrayEquals(originalBytes, decodedBytes);
}

@Test
public void testEncodeWithOutputStream() {
    byte[] originalBytes = {1, 2, 3, 4, 5};
    ByteArrayOutputStream bos = new ByteArrayOutputStream();
    assertTrue(StringEncoder64.encode(originalBytes, 0, originalBytes.length, bos));
    byte[] decodedBytes = StringEncoder64.decode(bos.toString());
    assertArrayEquals(originalBytes, decodedBytes);
}

@Test
public void testDecodeWithOutputStream() {
    String encodedString = "SGVsbG8sIFdvcmxkIQ==";
    ByteArrayOutputStream bos = new ByteArrayOutputStream();
    try {
        StringEncoder64.decode(encodedString, bos);
    } catch (IOException e) {
        fail("IOException should not be thrown");
    }
    byte[] decodedBytes = bos.toByteArray();
    byte[] expectedBytes = "Hello, World!".getBytes();
    assertArrayEquals(expectedBytes, decodedBytes);
}

@Test
public void testEncodeEmptyByteArray() {
    byte[] originalBytes = new byte[0];
    assertNotNull(StringEncoder64.encode(originalBytes));
    assertEquals("", StringEncoder64.encode(originalBytes));
}

@Test
public void testDecodeEmptyString() {
    byte[] decodedBytes = StringEncoder64.decode("");
    assertNotNull(decodedBytes);
    assertEquals(0, decodedBytes.length);
}

@Test
public void testEncodeByteArrayWithPadding() {
    byte[] originalBytes = {1, 2};
    String encodedString = StringEncoder64.encode(originalBytes);
    assertEquals("AQI=", encodedString);
}

@Test
public void testDecodeStringWithPadding() {
    String encodedString = "AQI=";
    byte[] decodedBytes = StringEncoder64.decode(encodedString);
    byte[] expectedBytes = {1, 2};
    assertArrayEquals(expectedBytes, decodedBytes);
}

}