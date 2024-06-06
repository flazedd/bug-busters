package jiprof_51;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__4 {
@Test
    public void putByteTest() {
        ByteVector byteVector = new ByteVector();
        byteVector.putByte(10);
        assertEquals(1, byteVector.length);
    }
@Test
public void putUTF8Test() {
    ByteVector byteVector = new ByteVector();
    byteVector.putUTF8("Hello");
    assertEquals(7, byteVector.length);
}
@Test
public void putByteArrayTest() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3};
    byteVector.putByteArray(array, 0, 3);
    assertEquals(3, byteVector.length);
}
@Test
public void putShortTest() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(10);
    assertEquals(2, byteVector.length);
}
@Test
public void putIntTest() {
    ByteVector byteVector = new ByteVector();
    byteVector.putInt(10);
    assertEquals(4, byteVector.length);
}
@Test
public void putLongTest() {
    ByteVector byteVector = new ByteVector();
    byteVector.putLong(10);
    assertEquals(8, byteVector.length);
}
@Test
public void put11Test() {
    ByteVector byteVector = new ByteVector();
    byteVector.put11(10, 20);
    assertEquals(2, byteVector.length);
}
@Test
public void put12Test() {
    ByteVector byteVector = new ByteVector();
    byteVector.put12(10, 20);
    assertEquals(3, byteVector.length);
}
}