package jiprof_51;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testPutByte() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByte(1);
    byteVector.putByte(2);
    byteVector.putByte(3);
    byte[] expected = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, expected, 0, byteVector.length);
    assertArrayEquals(expected, new byte[]{1, 2, 3});
}
@Test
public void testPutShort() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(0x1234);
    byte[] expected = new byte[]{(byte) 0x12, (byte) 0x34};
    assertArrayEquals(Arrays.copyOfRange(byteVector.data, 0, 2), expected);
}
@Test
public void testPutByteArray() {
    ByteVector byteVector = new ByteVector();
    byte[] array = new byte[]{1, 2, 3, 4, 5};
    byteVector.putByteArray(array, 1, 3);
    byte[] expected = new byte[]{2, 3, 4};
    assertArrayEquals(Arrays.copyOfRange(byteVector.data, 0, 3), expected);
}
@Test
public void testPutLong() {
    ByteVector byteVector = new ByteVector();
    byteVector.putLong(0x1234567890abcdefL);
    byte[] expected = new byte[]{(byte) 0x12, (byte) 0x34, (byte) 0x56, (byte) 0x78, (byte) 0x90, (byte) 0xab, (byte) 0xcd, (byte) 0xef};
    assertArrayEquals(Arrays.copyOfRange(byteVector.data, 0, 8), expected);
}
@Test
public void testPutInt() {
    ByteVector byteVector = new ByteVector();
    byteVector.putInt(0x12345678);
    byte[] expected = new byte[]{(byte) 0x12, (byte) 0x34, (byte) 0x56, (byte) 0x78};
    assertArrayEquals(Arrays.copyOfRange(byteVector.data, 0, 4), expected);
}
@Test
public void testEnlarge() {
    ByteVector byteVector = new ByteVector(2);
    byteVector.putByte(1);
    byteVector.putByte(2);
    byteVector.putByte(3);
    assertEquals(3, byteVector.length);
    assertEquals(4, byteVector.data.length);
}
@Test
public void testPutByteArrayOffset() {
    ByteVector byteVector = new ByteVector();
    byte[] array = new byte[]{1, 2, 3, 4, 5};
    byteVector.putByteArray(array, 1, 3);
    byte[] expected = new byte[]{2, 3, 4};
    assertArrayEquals(Arrays.copyOfRange(byteVector.data, 0, 3), expected);
}
@Test
public void testPutUTF82() {
    ByteVector byteVector = new ByteVector();
    byteVector.putUTF8("");
    byte[] data = byteVector.data;
    assertEquals(2, byteVector.length);
    assertEquals(0x00, data[0]);
    assertEquals(0x00, data[1]);
}
}