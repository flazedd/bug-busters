package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Util__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testVectorEqualsUnordered() {
    Vector<Integer> vec1 = new Vector<>();
    vec1.add(1);
    vec1.add(2);
    vec1.add(3);

    Vector<Integer> vec2 = new Vector<>();
    vec2.add(2);
    vec2.add(1);
    vec2.add(3);

    assertTrue(Util.VectorEqualsUnordered(vec1, vec2));
}

@Test
public void testStringCompareIgnCase() {
    assertTrue(Util.StringCompareIgnCase("hello", "HELLO") == 0);
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
    assertTrue(Util.StringCompare("hello", "hello") == 0);
}

@Test
public void testVectorEqualsUnorderedNull() {
    Vector<Integer> vec1 = null;
    Vector<Integer> vec2 = null;
    assertTrue(Util.VectorEqualsUnordered(vec1, vec2));
}

}