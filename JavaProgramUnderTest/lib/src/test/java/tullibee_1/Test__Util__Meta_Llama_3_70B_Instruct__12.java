package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Util__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testVectorEqualsUnordered() {
    Vector<Integer> v1 = new Vector<>();
    v1.add(1);
    v1.add(2);
    v1.add(3);

    Vector<Integer> v2 = new Vector<>();
    v2.add(2);
    v2.add(3);
    v2.add(1);

    assertTrue(Util.VectorEqualsUnordered(v1, v2));
}
@Test
public void testStringCompareIgnCase() {
    assertEquals(0, Util.StringCompareIgnCase("Hello", "hELLO"));
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
public void testStringCompareDifferent() {
    assertEquals(1, Util.StringCompare("abcd", "abc"));
}
}