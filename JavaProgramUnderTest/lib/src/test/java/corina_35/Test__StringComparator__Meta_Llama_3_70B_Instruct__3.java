package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Comparator;
import java.text.Collator;
public class Test__StringComparator__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testCompare() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "hello"));
}

@Test
public void testCompareDifferentLength() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("abc", "abcd"));
}

@Test
public void testCompareCaseSensitive() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("apple", "Banana"));
}

@Test
public void testCompareSamePrefix() {
    StringComparator comparator = new StringComparator();
    assertEquals(1, comparator.compare("abcde", "abcd"));
}

@Test
public void testCompareEmptyString() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("", "a"));
}

@Test
public void testCompareSameString() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("hello", "hello"));
}

@Test
public void testCompareNull() {
    StringComparator comparator = new StringComparator();
    try {
        comparator.compare(null, "hello");
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}

@Test
public void testCompareDifferentWords() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("apple", "banana"));
}

}