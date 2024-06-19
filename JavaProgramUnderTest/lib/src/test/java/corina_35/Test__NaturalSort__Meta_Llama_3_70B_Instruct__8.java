package corina_35;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Comparator;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testNaturalSort() {
    String a = "abc123";
    String b = "abc123";
    assertEquals(0, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortDifferentNumbers() {
    String a = "abc123";
    String b = "abc124";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortCaseInsensitive() {
    String a = "ABC123";
    String b = "abc123";
    assertEquals(0, NaturalSort.compareIgnoreCase(a, b));
}
@Test
public void testNaturalSortDifferentLengthNumbers() {
    String a = "abc123";
    String b = "abc1234";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortDifferentStrings() {
    String a = "abc123";
    String b = "def123";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortEmptyString() {
    String a = "abc123";
    String b = "";
    assertEquals(1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortNullString() {
    String a = "abc123";
    String b = null;
    try {
        NaturalSort.compare(a, b);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testNaturalSortComparator() {
    String[] array = {"abc123", "def456", "abc124", "def123"};
    Arrays.sort(array, new NaturalSort.NaturalComparator());
    String[] expected = {"abc123", "abc124", "def123", "def456"};
    assertArrayEquals(expected, array);
}
}