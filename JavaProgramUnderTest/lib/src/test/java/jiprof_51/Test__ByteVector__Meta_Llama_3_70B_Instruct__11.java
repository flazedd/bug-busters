package jiprof_51;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__11 {
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
public void testPutInt() {
    ByteVector byteVector = new ByteVector();
    byteVector.putInt(16777216);
    byte[] expected = new byte[4];
    expected[0] = 1;
    expected[1] = 0;
    expected[2] = 0;
    expected[3] = 0;
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(expected, Arrays.copyOfRange(actual, 0, 4));
}
@Test
public void testPutByteArray() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3, 4, 5};
    byteVector.putByteArray(array, 0, 5);
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(array, Arrays.copyOfRange(actual, 0, 5));
}
@Test
public void testPut11() {
    ByteVector byteVector = new ByteVector();
    byteVector.put11(1, 2);
    byte[] expected = new byte[2];
    expected[0] = 1;
    expected[1] = 2;
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(expected, Arrays.copyOfRange(actual, 0, 2));
}
@Test
public void testPut12() {
    ByteVector byteVector = new ByteVector();
    byteVector.put12(1, 256);
    byte[] expected = new byte[3];
    expected[0] = 1;
    expected[1] = 1;
    expected[2] = 0;
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(expected, actual);
}
@Test
public void testPutByteArrayNull() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByteArray(null, 0, 0);
    assertEquals(0, byteVector.length);
}
@Test
public void testPutByteArrayOutOfBounds() {
    ByteVector byteVector = new ByteVector();
    byte[] array = new byte[5];
    try {
        byteVector.putByteArray(array, 10, 2);
        fail("Expected IndexOutOfBoundsException");
    } catch (IndexOutOfBoundsException e) {
        // expected
    }
}
@Test
public void putByteArrayTest() {
    ByteVector byteVector = new ByteVector();
    byte[] byteArray = {1, 2, 3, 4, 5};
    byteVector.putByteArray(byteArray, 0, 5);
    assertArrayEquals(byteArray, Arrays.copyOfRange(byteVector.data, 0, byteVector.length));
}
}