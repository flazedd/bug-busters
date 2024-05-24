package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Test__Util__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> v1 = new Vector<String>();
    v1.add("apple");
    v1.add("banana");
    Vector<String> v2 = new Vector<String>();
    v2.add("banana");
    v2.add("apple");
    assertTrue(Util.VectorEqualsUnordered(v1, v2));
}

@Test
public void testStringCompareIgnCase() {
    assertTrue(Util.StringCompareIgnCase("Hello", "hello") == 0);
}



}