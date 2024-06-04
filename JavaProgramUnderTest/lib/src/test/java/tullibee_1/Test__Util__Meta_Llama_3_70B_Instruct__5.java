package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__Util__Meta_Llama_3_70B_Instruct__5 {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> lhs = new Vector<String>();
    lhs.add("apple");
    lhs.add("banana");
    lhs.add("orange");

    Vector<String> rhs = new Vector<String>();
    rhs.add("banana");
    rhs.add("orange");
    rhs.add("apple");

    assertTrue(Util.VectorEqualsUnordered(lhs, rhs));
}
@Test
public void testStringCompareIgnCase() {
    assertEquals(0, Util.StringCompareIgnCase("Hello", "hello"));
}
@Test
public void testIntMaxString() {
    assertEquals("", Util.IntMaxString(Integer.MAX_VALUE));
}
@Test
public void testNormalizeString() {
    assertEquals("", Util.NormalizeString(null));
}
@Test
public void testStringIsEmpty() {
    assertTrue(Util.StringIsEmpty(""));
}
@Test
public void testStringCompare() {
    assertEquals(0, Util.StringCompare("abc", "abc"));
}
@Test
public void testDoubleMaxString() {
    assertEquals("", Util.DoubleMaxString(Double.MAX_VALUE));
}
@Test
public void testStringCompareNull() {
    assertEquals(0, Util.StringCompare(null, null));
}
}