package corina_35;
import java.util.Comparator;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import java.text.Collator;
import org.junit.jupiter.api.Test;
public class Test__StringComparator__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testCompare() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("hello", "hello"));
}
@Test
public void testCompareIgnoreCase() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "hello"));
}
@Test
public void testCompareDifferentLength() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("abc", "abcd"));
}
@Test
public void testCompareEmptyString() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("", "hello"));
}
@Test
public void testCompareNullString() {
    StringComparator comparator = new StringComparator();
    try {
        comparator.compare(null, "hello");
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testCompareSameString() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("hello", "hello"));
}
@Test
public void testCompareNullAndNonNullString() {
    StringComparator comparator = new StringComparator();
    try {
        comparator.compare("hello", null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testCompareMultipleCharacters() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("abcdefg", "abcdefgh"));
}
}