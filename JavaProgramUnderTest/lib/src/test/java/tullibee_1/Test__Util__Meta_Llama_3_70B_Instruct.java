package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Util__Meta_Llama_3_70B_Instruct {
@Test
public void testStringCompare() {
    assertEquals(0, Util.StringCompare("hello", "hello"));
}

@Test
public void testVectorEqualsUnordered() {
    Vector<String> v1 = new Vector<String>();
    v1.add("a");
    v1.add("b");
    Vector<String> v2 = new Vector<String>();
    v2.add("b");
    v2.add("a");
    assertTrue(Util.VectorEqualsUnordered(v1, v2));
}





}