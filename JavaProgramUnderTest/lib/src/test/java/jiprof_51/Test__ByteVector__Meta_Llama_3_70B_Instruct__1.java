package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__ByteVector__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testPutByte() {
    ByteVector byteVector = new ByteVector();
    byteVector.putByte(1);
    assertEquals(1, byteVector.length);
}

@Test
public void testPutUTF8() {
    ByteVector byteVector = new ByteVector();
    byteVector.putUTF8("Hello");
    assertEquals(7, byteVector.length);
}

@Test
public void testPutShort() {
    ByteVector byteVector = new ByteVector();
    byteVector.putShort(256);
    assertEquals(2, byteVector.length);
}

@Test
public void testPutByteArray() {
    ByteVector byteVector = new ByteVector();
    byte[] array = {1, 2, 3};
    byteVector.putByteArray(array, 0, 3);
    assertEquals(3, byteVector.length);
}

@Test
public void testPutInt() {
    ByteVector byteVector = new ByteVector();
    byteVector.putInt(16777216);
    assertEquals(4, byteVector.length);
}

@Test
public void testPutLong() {
    ByteVector byteVector = new ByteVector();
    byteVector.putLong(4294967296L);
    assertEquals(8, byteVector.length);
}

@Test
public void testPut11() {
    ByteVector byteVector = new ByteVector();
    byteVector.put11(1, 2);
    assertEquals(2, byteVector.length);
}

@Test
public void testPut12() {
    ByteVector byteVector = new ByteVector();
    byteVector.put12(1, 256);
    assertEquals(3, byteVector.length);
}

}