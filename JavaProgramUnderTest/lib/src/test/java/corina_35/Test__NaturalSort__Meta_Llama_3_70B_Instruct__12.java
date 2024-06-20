package corina_35;
import org.junit.jupiter.api.Test;
import java.util.Comparator;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__12 {
@Test
public void naturalSortTest() {
    String a = "abc123def";
    String b = "abc123def";
    assertEquals(0, NaturalSort.compare(a, b));
}
@Test
public void naturalSortTest2() {
    String a = "abc123def";
    String b = "abc124def";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void naturalSortTest3() {
    String a = "abc123def";
    String b = "abc123dEf";
    assertEquals(0, NaturalSort.compareIgnoreCase(a, b));
}
@Test
public void naturalSortTest4() {
    String a = "abc123def";
    String b = "abcd123ef";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void naturalSortTest5() {
    String a = "abc123def";
    String b = "abc0123def";
    assertEquals(1, NaturalSort.compare(a, b));
}
@Test
public void naturalSortTest6() {
    String a = "abc123def";
    String b = "abc123de";
    assertEquals(1, NaturalSort.compare(a, b));
}
@Test
public void naturalSortTest7() {
    String a = "abc123def";
    String b = "abcd1234ef";
    assertEquals(-1, NaturalSort.compare(a, b));
}
@Test
public void naturalSortTest8() {
    String a = "abc012def";
    String b = "abc123def";
    assertEquals(-1, NaturalSort.compare(a, b));
}
}