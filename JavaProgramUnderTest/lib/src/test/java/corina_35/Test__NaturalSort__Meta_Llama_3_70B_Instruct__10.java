package corina_35;
import java.util.Arrays;
import java.util.Comparator;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__10 {
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
public void testNaturalSortDifferentLetters() {
    String a = "abc123";
    String b = "abd123";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortFractional() {
    String a = "abc1.23";
    String b = "abc1.24";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortMultipleNumbers() {
    String a = "abc123def456";
    String b = "abc123def457";
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
        fail("Expected NullPointerException to be thrown");
    } catch (NullPointerException e) {
        // Expected
    }
}
@Test
public void testNaturalSortIgnoreCase() {
    String a = "abc123";
    String b = "ABC123";
    assertEquals(0, NaturalSort.compareIgnoreCase(a, b));
}
}