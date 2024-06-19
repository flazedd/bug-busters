package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__Util__Meta_Llama_3_70B_Instruct__7 {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> vec1 = new Vector<String>();
    vec1.add("apple");
    vec1.add("banana");
    vec1.add("orange");

    Vector<String> vec2 = new Vector<String>();
    vec2.add("banana");
    vec2.add("orange");
    vec2.add("apple");

    assertTrue(Util.VectorEqualsUnordered(vec1, vec2));
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
public void testStringIsEmpty() {
    assertTrue(Util.StringIsEmpty(""));
}
@Test
public void testDoubleMaxString() {
    assertEquals("", Util.DoubleMaxString(Double.MAX_VALUE));
}
@Test
public void testStringCompare() {
    assertEquals(0, Util.StringCompare("hello", "hello"));
}
@Test
public void testStringIsEmptyNonNull() {
    assertFalse(Util.StringIsEmpty("non-empty string"));
}
}