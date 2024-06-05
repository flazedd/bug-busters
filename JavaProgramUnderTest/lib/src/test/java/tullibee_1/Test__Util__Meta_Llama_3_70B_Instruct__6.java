package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class Test__Util__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> lhs = new Vector<String>();
    lhs.add("a");
    lhs.add("b");
    lhs.add("c");

    Vector<String> rhs = new Vector<String>();
    rhs.add("c");
    rhs.add("b");
    rhs.add("a");

    assertTrue(Util.VectorEqualsUnordered(lhs, rhs));
}
@Test
public void testStringCompareIgnCase() {
    assertEquals(0, Util.StringCompareIgnCase("Hello", "hElLo"));
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
public void testStringCompare() {
    assertEquals(0, Util.StringCompare("abc", "abc"));
}
@Test
public void testStringIsEmpty() {
    assertTrue(Util.StringIsEmpty(""));
}
@Test
public void testDoubleMaxString() {
    assertEquals("", Util.DoubleMaxString(Double.MAX_VALUE));
}
@Test
public void testVectorEqualsUnorderedDifferentSizes() {
    Vector<String> lhs = new Vector<String>();
    lhs.add("a");
    lhs.add("b");
    lhs.add("c");

    Vector<String> rhs = new Vector<String>();
    rhs.add("a");
    rhs.add("b");

    assertFalse(Util.VectorEqualsUnordered(lhs, rhs));
}
}