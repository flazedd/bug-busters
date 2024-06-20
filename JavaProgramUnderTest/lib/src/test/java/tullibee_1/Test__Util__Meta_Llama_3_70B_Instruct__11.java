package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Util__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> lhs = new Vector<>();
    lhs.add("apple");
    lhs.add("banana");
    Vector<String> rhs = new Vector<>();
    rhs.add("banana");
    rhs.add("apple");
    assertTrue(Util.VectorEqualsUnordered(lhs, rhs));
}
@Test
public void testStringCompareIgnCase() {
    assertTrue(Util.StringCompareIgnCase("Hello", "hELLO") == 0);
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
    assertTrue(Util.StringCompare("abc", "abc") == 0);
}
@Test
public void testDoubleMaxString() {
    assertEquals("", Util.DoubleMaxString(Double.MAX_VALUE));
}
@Test
public void testVectorEqualsUnorderedNull() {
    Vector<String> lhs = null;
    Vector<String> rhs = null;
    assertTrue(Util.VectorEqualsUnordered(lhs, rhs));
}
}