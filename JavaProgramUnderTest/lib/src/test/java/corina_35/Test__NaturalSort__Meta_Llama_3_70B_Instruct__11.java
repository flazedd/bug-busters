package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Comparator;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testNaturalSort() {
    assertEquals(0, NaturalSort.compare("abc123", "abc123"));
}
@Test
public void testNaturalSortDifferentDigits() {
    assertEquals(-1, NaturalSort.compare("abc123", "abc124"));
}
@Test
public void testNaturalSortLeadingZero() {
    assertEquals(-1, NaturalSort.compare("abc012", "abc12"));
}
@Test
public void testNaturalSortCaseInsensitive() {
    assertEquals(0, NaturalSort.compareIgnoreCase("abc123", "ABC123"));
}
@Test
public void testNaturalSortDifferentLength() {
    assertEquals(-1, NaturalSort.compare("abc123", "abc1234"));
}
@Test
public void testNaturalSortNonNumeric() {
    assertEquals(-1, NaturalSort.compare("abc123", "abcxyz"));
}
@Test
public void testNaturalSortComparator() {
    String[] arr = {"abc123", "abc12", "abc124"};
    Arrays.sort(arr, new NaturalSort.NaturalComparator());
    assertEquals("abc12", arr[0]);
}
@Test
public void testNaturalSortEmptyString() {
    assertEquals(0, NaturalSort.compare("", ""));
}
}