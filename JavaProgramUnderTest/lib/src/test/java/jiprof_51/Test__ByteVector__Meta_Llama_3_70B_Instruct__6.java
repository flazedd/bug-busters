package jiprof_51;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testPutByte() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByte(10);
    byteVector.putByte(20);
    byte[] data = byteVector.data;
    assertEquals(data[0], 10);
    assertEquals(data[1], 20);
}
@Test
public void testPutShort() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(256);
    byte[] data = byteVector.data;
    assertEquals(data[0], 1);
    assertEquals(data[1], 0);
}
@Test
public void testPutUTF8() {
    ByteVector byteVector = new ByteVector();
    byteVector.putUTF8("Hello");
    byte[] data = byteVector.data;
    assertEquals(data[0], 0);
    assertEquals(data[1], 5);
    assertEquals(data[2], 'H');
    assertEquals(data[3], 'e');
    assertEquals(data[4], 'l');
    assertEquals(data[5], 'l');
    assertEquals(data[6], 'o');
}
@Test
public void testPutByteArray() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3, 4, 5};
    byteVector.putByteArray(array, 1, 3);
    byte[] data = byteVector.data;
    assertEquals(data[0], 2);
    assertEquals(data[1], 3);
    assertEquals(data[2], 4);
}
@Test
public void testPutInt() {
    ByteVector byteVector = new ByteVector();
    byteVector.putInt(16777216);
    byte[] data = byteVector.data;
    assertEquals(data[0], 1);
    assertEquals(data[1], 0);
    assertEquals(data[2], 0);
    assertEquals(data[3], 0);
}
@Test
public void testPut11() {
    ByteVector byteVector = new ByteVector();
    byteVector.put11(10, 20);
    byte[] data = byteVector.data;
    assertEquals(data[0], 10);
    assertEquals(data[1], 20);
}
@Test
public void testPut12() {
    ByteVector byteVector = new ByteVector();
    byteVector.put12(10, 256);
    byte[] data = byteVector.data;
    assertEquals(data[0], 10);
    assertEquals(data[1], 1);
    assertEquals(data[2], 0);
}
@Test
public void testEnlarge() {
    ByteVector byteVector = new ByteVector(10);
    for (int i = 0; i < 20; i++) {
        byteVector.putByte((byte) i);
    }
    assertEquals(byteVector.length, 20);
}
}