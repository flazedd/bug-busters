package tullibee_1;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Test__Util__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> v1 = new Vector<>();
    v1.add("apple");
    v1.add("banana");
    v1.add("orange");

    Vector<String> v2 = new Vector<>();
    v2.add("banana");
    v2.add("orange");
    v2.add("apple");

    assertTrue(Util.VectorEqualsUnordered(v1, v2));
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
public void testVectorEqualsUnorderedWithNull() {
    Vector<String> v1 = new Vector<>();
    v1.add("apple");
    v1.add("banana");
    v1.add("orange");

    Vector<String> v2 = null;

    assertFalse(Util.VectorEqualsUnordered(v1, v2));
}
}