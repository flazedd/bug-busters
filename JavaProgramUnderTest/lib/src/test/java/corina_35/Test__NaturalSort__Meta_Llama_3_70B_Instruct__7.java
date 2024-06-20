package corina_35;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Comparator;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__7 {
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
public void testNaturalSortDifferentCharacters() {
    String a = "abc123def";
    String b = "abd123def";
    assertEquals(-1, NaturalSort.compare(a, b));
}

@Test
public void testNaturalSortIgnoreCase() {
    String a = "AbC123dEf";
    String b = "abc123def";
    assertEquals(0, NaturalSort.compareIgnoreCase(a, b));
}

@Test
public void testNaturalSortComparator() {
    String a = "abc123def";
    String b = "abc124def";
    Comparator<String> comparator = new NaturalSort.NaturalComparator();
    assertEquals(-1, comparator.compare(a, b));
}

@Test
public void testNaturalSortEmptyString() {
    String a = "abc123def";
    String b = "";
    assertEquals(1, NaturalSort.compare(a, b));
}

@Test
public void testNaturalSortMultipleNumbers() {
    String a = "abc123def456";
    String b = "abc124def456";
    assertEquals(-1, NaturalSort.compare(a, b));
}

@Test
public void testNaturalSortLeadingZerosDifferentNumbers() {
    String a = "abc00123def";
    String b = "abc00124def";
    assertEquals(-1, NaturalSort.compare(a, b));
}


}