package corina_35;
import java.util.Comparator;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__5 {
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
public void testNaturalSortDifferentLetters() {
    String a = "abc123def";
    String b = "abd123def";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortIgnoreCase() {
    String a = "ABC123def";
    String b = "abc123def";
    assertEquals(0, NaturalSort.compareIgnoreCase(a, b));
}
@Test
public void testNaturalSortMultipleNumbers() {
    String a = "abc123def456";
    String b = "abc123def457";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortWithNonDigitCharacters() {
    String a = "abc123defghi";
    String b = "abc123defghj";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortEmptyString() {
    String a = "abc123def";
    String b = "";
    assertEquals(1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortNullString() {
    String a = "abc123def";
    String b = null;
    try {
        NaturalSort.compare(a, b);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
}