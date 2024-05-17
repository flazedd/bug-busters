package tullibee_1;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class Test__Util__Meta_Llama_3_70B_Instruct {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> lhs = new Vector<>();
    lhs.add("a");
    lhs.add("b");
    lhs.add("c");

    Vector<String> rhs = new Vector<>();
    rhs.add("c");
    rhs.add("b");
    rhs.add("a");

    assertTrue(Util.VectorEqualsUnordered(lhs, rhs));
}

@Test
public void testStringCompareIgnCase() {
    assertEquals(0, Util.StringCompareIgnCase("Hello", "hello"));
}

}