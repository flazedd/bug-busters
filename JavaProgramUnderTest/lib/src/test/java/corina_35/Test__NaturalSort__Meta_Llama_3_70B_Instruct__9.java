package corina_35;
import java.util.Arrays;
import java.util.Comparator;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testNaturalSort() {
    String a = "abc123def";
    String b = "abc123def";
    assertEquals(0, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortDifferentNumbers() {
    String a = "abc123def";
    String b = "abc124def";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortIgnoreCase() {
    String a = "ABC123def";
    String b = "abc123def";
    assertEquals(0, NaturalSort.compareIgnoreCase(a, b));
}
@Test
public void testNaturalSortDifferentNumbersAtEnd() {
    String a = "abcdef123";
    String b = "abcdef124";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortWithLeadingSpaces() {
    String a = "  abc123def";
    String b = "abc123def";
    assertEquals(0, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortWithTrailingSpaces() {
    String a = "abc123def  ";
    String b = "abc123def";
    assertEquals(0, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortWithMultipleNumbers() {
    String a = "abc123def456";
    String b = "abc123def457";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortWithNonNumericCharacters() {
    String a = "abc123defghi";
    String b = "abc123defhgi";
    assertEquals(-1, NaturalSort.compare(a, b));
}
}