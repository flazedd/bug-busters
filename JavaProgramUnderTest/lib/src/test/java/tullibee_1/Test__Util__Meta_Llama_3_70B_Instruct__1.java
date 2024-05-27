package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
import org.junit.jupiter.api.Test;
public class Test__Util__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testStringIsEmpty() {
    assertTrue(Util.StringIsEmpty(""));
}

@Test
public void testStringCompareIgnCase() {
    assertEquals(0, Util.StringCompareIgnCase("Hello", "hello"));
}

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
public void testIntMaxString() {
    assertEquals("", Util.IntMaxString(Integer.MAX_VALUE));
}

@Test
public void testNormalizeString() {
    assertEquals("", Util.NormalizeString(null));
}

@Test
public void testDoubleMaxString() {
    assertEquals("", Util.DoubleMaxString(Double.MAX_VALUE));
}

@Test
public void testStringCompare() {
    assertEquals(0, Util.StringCompare("abc", "abc"));
}

@Test
public void testNormalizeStringNotNull() {
    assertEquals("hello", Util.NormalizeString("hello"));
}



}