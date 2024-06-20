package jiprof_51;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__10 {
@Test
    public void testPutByte() {
        ByteVector byteVector = new ByteVector();
        byteVector.putByte(10);
        assertEquals(1, byteVector.length);
    }
@Test
public void testPutShort() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(10);
    assertEquals(2, byteVector.length);
}
@Test
public void testPutByteArray() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3, 4, 5};
    byteVector.putByteArray(array, 0, 5);
    assertEquals(5, byteVector.length);
}
@Test
public void testPutInt() {
    ByteVector byteVector = new ByteVector();
    byteVector.putInt(10);
    assertEquals(4, byteVector.length);
}
@Test
public void testPutLong() {
    ByteVector byteVector = new ByteVector();
    byteVector.putLong(10L);
    assertEquals(8, byteVector.length);
}
@Test
public void testPut12() {
    ByteVector byteVector = new ByteVector();
    byteVector.put12(1, 2);
    assertEquals(3, byteVector.length);
}
@Test
public void testPut11() {
    ByteVector byteVector = new ByteVector();
    byteVector.put11(1, 2);
    assertEquals(2, byteVector.length);
}
@Test
public void testEnlarge() {
    ByteVector byteVector = new ByteVector(2);
    byteVector.putByte(1);
    byteVector.putByte(2);
    byteVector.putByte(3);
    assertEquals(3, byteVector.length);
}
}