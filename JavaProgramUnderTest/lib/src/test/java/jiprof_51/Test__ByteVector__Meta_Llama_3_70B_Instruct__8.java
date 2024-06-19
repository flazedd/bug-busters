package jiprof_51;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testPutByte() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByte(1);
    byteVector.putByte(2);
    byteVector.putByte(3);
    byte[] expected = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, expected, 0, byteVector.length);
    assertArrayEquals(new byte[]{1, 2, 3}, expected);
}
@Test
public void testPutShort() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(256);
    byte[] expected = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, expected, 0, byteVector.length);
    assertArrayEquals(new byte[]{1, 0}, expected);
}
@Test
public void testPutLong() {
    ByteVector byteVector = new ByteVector();
    byteVector.putLong(4294967296L);
    byte[] expected = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, expected, 0, byteVector.length);
    assertArrayEquals(new byte[]{0, 0, 0, 1, 0, 0, 0, 0}, expected);
}
@Test
public void testPutUTF8() {
    ByteVector byteVector = new ByteVector();
    byteVector.putUTF8("Hello");
    byte[] expected = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, expected, 0, byteVector.length);
    assertArrayEquals(new byte[]{0x05, 'H', 'e', 'l', 'l', 'o'}, Arrays.copyOfRange(expected, 1, expected.length));
}
@Test
public void testPutByteArray() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3, 4, 5};
    byteVector.putByteArray(array, 0, 5);
    byte[] expected = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, expected, 0, byteVector.length);
    assertArrayEquals(new byte[]{1, 2, 3, 4, 5}, expected);
}
@Test
public void testPutByteArrayNull() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByteArray(null, 0, 5);
    byte[] expected = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, expected, 0, byteVector.length);
    assertArrayEquals(new byte[]{0, 0, 0, 0, 0}, expected);
}
@Test
public void testPutByteArrayOutOfBounds() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3, 4, 5};
    try {
        byteVector.putByteArray(array, 0, 10);
        fail("Expected IndexOutOfBoundsException");
    } catch (IndexOutOfBoundsException e) {
        // Expected
    }
}
@Test
public void testPutByteArrayNegativeOffset() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3, 4, 5};
    try {
        byteVector.putByteArray(array, -1, 5);
        fail("Expected IndexOutOfBoundsException");
    } catch (IndexOutOfBoundsException e) {
        // Expected
    }
}
}