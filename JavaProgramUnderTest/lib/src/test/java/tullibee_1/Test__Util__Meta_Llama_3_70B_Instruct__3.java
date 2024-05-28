package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Util__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> vec1 = new Vector<String>();
    vec1.add("hello");
    vec1.add("world");
    
    Vector<String> vec2 = new Vector<String>();
    vec2.add("world");
    vec2.add("hello");
    
    assertTrue(Util.VectorEqualsUnordered(vec1, vec2));
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
public void testVectorEqualsUnorderedNull() {
    Vector<String> vec1 = null;
    Vector<String> vec2 = null;
    assertTrue(Util.VectorEqualsUnordered(vec1, vec2));
}

}