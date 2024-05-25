package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Comparator;
import org.junit.jupiter.api.Test;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testNaturalSort() {
    assertEquals(-1, NaturalSort.compare("abc1", "abc2"));
}

@Test
public void testNaturalSortIgnoreCase() {
    assertEquals(0, NaturalSort.compareIgnoreCase("ABC10", "abc10"));
}

}