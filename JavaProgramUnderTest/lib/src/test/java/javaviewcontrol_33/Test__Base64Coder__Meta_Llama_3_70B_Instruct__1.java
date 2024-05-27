package javaviewcontrol_33;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Base64Coder__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testEncodeDecode() {
    String original = "Hello, World!";
    String encoded = Base64Coder.encodeString(original);
    String decoded = new String(Base64Coder.decode(encoded));
    assertEquals(original, decoded);
}

@Test
public void testEncodeDecodeByteArray() {
    byte[] original = {1, 2, 3, 4, 5};
    char[] encoded = Base64Coder.encode(original);
    byte[] decoded = Base64Coder.decode(new String(encoded));
    assertArrayEquals(original, decoded);
}

}