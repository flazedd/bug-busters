package corina_35;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Comparator;
public class Test__NaturalSort__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testNaturalComparator() {
    NaturalSort.NaturalComparator comparator = new NaturalSort.NaturalComparator();
    assertEquals(-1, comparator.compare("abc1", "abc2"));
}

@Test
public void testCINaturalComparator() {
    NaturalSort.CINaturalComparator comparator = new NaturalSort.CINaturalComparator();
    assertEquals(0, comparator.compare("ABC10", "abc10"));
}

@Test
public void testCompare() {
    assertEquals(1, NaturalSort.compare("abc10", "abc9"));
}

@Test
public void testCompareIgnoreCase() {
    assertEquals(-1, NaturalSort.compareIgnoreCase("abc9", "ABC10"));
}

@Test
public void testCompareIdentical() {
    assertEquals(0, NaturalSort.compare("version1.2", "version1.2"));
}

@Test
public void testCompareSuffix() {
    assertEquals(-1, NaturalSort.compare("abc10xyz", "abc11xyz"));
}

@Test
public void testComparePrefixSuffix() {
    assertEquals(1, NaturalSort.compare("helloabc10world", "helloabc9world"));
}

@Test
public void testCompareComplex() {
    assertEquals(-1, NaturalSort.compare("helloabc10def123world", "helloabc10def124world"));
}



}