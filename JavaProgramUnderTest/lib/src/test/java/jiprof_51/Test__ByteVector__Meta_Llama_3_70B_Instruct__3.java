package jiprof_51;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testPutByte() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByte(1);
    byteVector.putByte(2);
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(new byte[] {1, 2}, actual);
}

@Test
public void testPutShort() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(0x1234);
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(new byte[] {(byte) 0x12, (byte) 0x34}, actual);
}

@Test
public void testPutUTF8() {
    ByteVector byteVector = new ByteVector();
    byteVector.putUTF8("Hello");
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(new byte[] {0x00, 0x05, 'H', 'e', 'l', 'l', 'o'}, actual);
}

@Test
public void testPutByteArray() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3, 4, 5};
    byteVector.putByteArray(array, 1, 3);
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(new byte[] {2, 3, 4}, actual);
}

@Test
public void testPutLong() {
    ByteVector byteVector = new ByteVector();
    byteVector.putLong(0x1234567890abcdefL);
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(new byte[] {
        (byte) 0x12, (byte) 0x34, (byte) 0x56, (byte) 0x78,
        (byte) 0x90, (byte) 0xab, (byte) 0xcd, (byte) 0xef
    }, actual);
}

@Test
public void testPutInt() {
    ByteVector byteVector = new ByteVector();
    byteVector.putInt(0x12345678);
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(new byte[] {
        (byte) 0x12, (byte) 0x34, (byte) 0x56, (byte) 0x78
    }, actual);
}

@Test
public void testPut12() {
    ByteVector byteVector = new ByteVector();
    byteVector.put12(1, 0x1234);
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(new byte[] {1, (byte) 0x12, (byte) 0x34}, actual);
}

@Test
public void testPut11() {
    ByteVector byteVector = new ByteVector();
    byteVector.put11(1, 2);
    byte[] actual = new byte[byteVector.length];
    System.arraycopy(byteVector.data, 0, actual, 0, byteVector.length);
    assertArrayEquals(new byte[] {1, 2}, actual);
}

}