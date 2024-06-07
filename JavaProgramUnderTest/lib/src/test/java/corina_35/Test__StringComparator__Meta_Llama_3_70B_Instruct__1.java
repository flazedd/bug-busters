package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import java.text.Collator;
import java.util.Comparator;
import org.junit.jupiter.api.Test;
public class Test__StringComparator__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testCompareEqualStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("hello", "hello"));
}

@Test
public void testCompareDifferentCaseStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "hello"));
}

@Test
public void testCompareDifferentLengthStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("abc", "abcd"));
}

@Test
public void testCompareStringsStartingWithDifferentCharacters() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("apple", "banana"));
}

@Test
public void testCompareStringsEndingWithDifferentCharacters() {
    StringComparator comparator = new StringComparator();
    assertEquals(1, comparator.compare("abcdz", "abcdy"));
}

@Test
public void testCompareEmptyString() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("", ""));
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
public void testCompareStringWithNull() {
    StringComparator comparator = new StringComparator();
    try {
        comparator.compare("hello", null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}















}