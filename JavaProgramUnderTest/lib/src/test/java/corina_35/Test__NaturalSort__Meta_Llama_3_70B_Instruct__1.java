package corina_35;
import org.junit.jupiter.api.Test;
import java.util.Comparator;
import static org.junit.jupiter.api.Assertions.*;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testNaturalSort() {
    assertEquals(0, NaturalSort.compare("abc123", "abc123"));
}

@Test
public void testNaturalSortDifferentLength() {
    assertEquals(-1, NaturalSort.compare("abc123", "abc1234"));
}

@Test
public void testNaturalSortIgnoreCase() {
    assertEquals(0, NaturalSort.compareIgnoreCase("ABC123", "abc123"));
}

@Test
public void testNaturalSortFractional() {
    assertEquals(-1, NaturalSort.compare("abc0123", "abc01230"));
}

@Test
public void testNaturalSortLeadingSpaces() {
    assertEquals(0, NaturalSort.compare("   abc123", "abc123"));
}

@Test
public void testNaturalSortEmptyString() {
    assertEquals(-1, NaturalSort.compare("", "abc123"));
}

@Test
public void testNaturalSortComparator() {
    String[] array = {"abc123", "abc012", "abc0123", "abc1234"};
    java.util.Arrays.sort(array, new NaturalSort.NaturalComparator());
    assertEquals("abc012", array[0]);
}

@Test
public void testNaturalSortIgnoreCaseComparator() {
    String[] array = {"ABC123", "abc012", "abc0123", "abc1234"};
    java.util.Arrays.sort(array, new NaturalSort.CINaturalComparator());
    assertEquals("abc012", array[0]);
}

}