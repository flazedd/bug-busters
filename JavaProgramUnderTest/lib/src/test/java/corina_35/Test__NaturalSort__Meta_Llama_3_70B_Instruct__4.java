package corina_35;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Comparator;
import java.util.Arrays;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testNaturalSort() {
    assertEquals(0, NaturalSort.compare("abc123def", "abc123def"));
}
@Test
public void testNaturalOrdering() {
    String a = "abc123";
    String b = "abc123";
    assertEquals(0, NaturalSort.compare(a, b));
}
@Test
public void testNaturalOrderingDifferentLength() {
    String a = "abc123";
    String b = "abc1234";
    assertEquals(1, NaturalSort.compare(b, a));
}
@Test
public void testNaturalOrderingDigitsFirst() {
    String a = "123abc";
    String b = "abc123";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalOrderingCaseInsensitive() {
    String a = "ABC123";
    String b = "abc123";
    assertEquals(0, NaturalSort.compareIgnoreCase(a, b));
}
@Test
public void testNaturalOrderingMultipleDigits() {
    String a = "abc123def456";
    String b = "abc123def457";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void testNaturalSortDifferentNumbers() {
    assertEquals(-1, NaturalSort.compare("abc1", "abc2"));
}

@Test
public void testNaturalSortSameString() {
    assertEquals(0, NaturalSort.compare("abc1", "abc1"));
}

}