package corina_35;
import java.util.Comparator;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__3 {
@Test
public void naturalSortTest() {
    assertEquals(0, NaturalSort.compare("abc123", "abc123"));
}

@Test
public void naturalSortTest2() {
    assertEquals(-1, NaturalSort.compare("abc123", "abc124"));
}

@Test
public void naturalSortTest3() {
    assertEquals(1, NaturalSort.compare("abc124", "abc123"));
}

@Test
public void naturalSortTest4() {
    assertEquals(0, NaturalSort.compareIgnoreCase("abc123", "ABC123"));
}

@Test
public void naturalSortTest5() {
    assertEquals(-1, NaturalSort.compare("abc012", "abc123"));
}

@Test
public void naturalSortTest6() {
    assertEquals(1, NaturalSort.compare("abc123", "abc012"));
}

@Test
public void naturalSortTest7() {
    assertEquals(-1, NaturalSort.compare("abc012a", "abc012b"));
}

@Test
public void naturalSortTest8() {
    assertEquals(0, NaturalSort.compare("abc012a", "abc012a"));
}

}