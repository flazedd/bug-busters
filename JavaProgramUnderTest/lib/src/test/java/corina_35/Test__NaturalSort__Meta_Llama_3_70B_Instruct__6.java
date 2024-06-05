package corina_35;
import java.util.Arrays;
import java.util.Comparator;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__6 {
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
public void naturalSortTest() {
    assertEquals(0, NaturalSort.compare("abc123def", "abc123def"));
}
@Test
public void naturalSortTest2() {
    assertEquals(-1, NaturalSort.compare("abc123def", "abc124def"));
}
@Test
public void naturalSortTest3() {
    assertEquals(1, NaturalSort.compare("abc124def", "abc123def"));
}
@Test
public void naturalSortTest4() {
    assertEquals(0, NaturalSort.compareIgnoreCase("ABC123DEF", "abc123def"));
}
@Test
public void naturalSortTest5() {
    assertEquals(-1, NaturalSort.compare("abc123def", "abc123xyz"));
}
@Test
public void naturalSortTest6() {
    assertEquals(1, NaturalSort.compare("abc123xyz", "abc123def"));
}
}