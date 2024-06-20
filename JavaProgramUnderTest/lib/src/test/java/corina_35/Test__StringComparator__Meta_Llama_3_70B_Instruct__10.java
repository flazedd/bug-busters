package corina_35;
import java.text.Collator;
import java.util.Arrays;
import java.util.Comparator;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__StringComparator__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testCompareStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("hello", "hello"));
}
@Test
public void testCompareDifferentCaseStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "hello"));
}
@Test
public void testCompareShorterString() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("abc", "abcd"));
}
@Test
public void testCompareLongerString() {
    StringComparator comparator = new StringComparator();
    assertEquals(1, comparator.compare("abcd", "abc"));
}
@Test
public void testCompareDifferentStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("abc", "def"));
}
@Test
public void testCompareEmptyString() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("", "a"));
}
@Test
public void testCompareNullString() {
    StringComparator comparator = new StringComparator();
    try {
        comparator.compare(null, "a");
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testCompareSamePrefixAndLength() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("abcd", "abcd"));
}
}