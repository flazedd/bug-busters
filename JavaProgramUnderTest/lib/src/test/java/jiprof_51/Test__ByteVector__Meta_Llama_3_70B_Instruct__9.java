package jiprof_51;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__9 {
@Test
public void putByteTest() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByte(10);
    byteVector.putByte(20);
    byte[] data = byteVector.data;
    assertEquals(2, byteVector.length);
    assertEquals(10, data[0]);
    assertEquals(20, data[1]);
}
@Test
public void putByteArrayTest() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {10, 20, 30, 40, 50};
    byteVector.putByteArray(array, 1, 3);
    byte[] data = byteVector.data;
    assertEquals(3, byteVector.length);
    assertEquals(20, data[0]);
    assertEquals(30, data[1]);
    assertEquals(40, data[2]);
}
@Test
public void putIntTest() {
    ByteVector byteVector = new ByteVector();
    byteVector.putInt(0x12345678);
    byte[] data = byteVector.data;
    assertEquals(4, byteVector.length);
    assertEquals(0x12, data[0]);
    assertEquals(0x34, data[1]);
    assertEquals(0x56, data[2]);
    assertEquals(0x78, data[3]);
}
@Test
public void putShortTest() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(0x1234);
    byte[] data = byteVector.data;
    assertEquals(2, byteVector.length);
    assertEquals(0x12, data[0]);
    assertEquals(0x34, data[1]);
}
@Test
public void put11Test() {
    ByteVector byteVector = new ByteVector();
    byteVector.put11(0x12, 0x34);
    byte[] data = byteVector.data;
    assertEquals(2, byteVector.length);
    assertEquals(0x12, data[0]);
    assertEquals(0x34, data[1]);
}
@Test
public void putByteArrayNullTest() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByteArray(null, 0, 5);
    byte[] data = byteVector.data;
    assertEquals(5, byteVector.length);
    for (int i = 0; i < 5; i++) {
        assertEquals(0, data[i]);
    }
}
@Test
public void putShortThenPutByteTest() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(0x1234);
    byteVector.putByte(0x56);
    byte[] data = byteVector.data;
    assertEquals(3, byteVector.length);
    assertEquals(0x12, data[0]);
    assertEquals(0x34, data[1]);
    assertEquals(0x56, data[2]);
}
@Test
public void testPutByte() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByte(10);
    assertEquals(1, byteVector.length);
}
}