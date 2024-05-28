package corina_35;
import org.junit.jupiter.api.Test;
import java.text.Collator;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Comparator;
public class Test__StringComparator__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testEqualStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("hello", "hello"));
}
@Test
public void testCaseInsensitive() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "hello"));
}
@Test
public void testDifferentLengthStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("abc", "abcd"));
}
@Test
public void testCompareEqualStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("hello", "hello"));
}

@Test
public void testCompareStringsWithDifferentLength() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("hello", "hellooo"));
}

@Test
public void testCompareStringsDifferentCase() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "hello"));
}

@Test
public void testCompareEmptyStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("", ""));
}

@Test
public void testCompareNullStrings() {
    StringComparator comparator = new StringComparator();
    try {
        comparator.compare(null, "hello");
        fail("Expected NullPointerException to be thrown");
    } catch (NullPointerException e) {
        // Expected
    }
}

}