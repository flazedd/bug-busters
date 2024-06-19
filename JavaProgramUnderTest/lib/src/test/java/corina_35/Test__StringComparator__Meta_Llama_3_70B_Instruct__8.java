package corina_35;
import java.util.Comparator;
import java.text.Collator;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__StringComparator__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testCompareEqualStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "Hello"));
}
@Test
public void testCompareDifferentCaseStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "hello"));
}
@Test
public void testCompareStringsOfDifferentLength() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("Hello", "HelloWorld"));
}
@Test
public void testCompareStringsInOrder() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("Apple", "Banana"));
}
@Test
public void testCompareStringsInReverseOrder() {
    StringComparator comparator = new StringComparator();
    assertEquals(1, comparator.compare("Banana", "Apple"));
}
@Test
public void testCompareStringsStartingWithSameLetter() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("Ant", "Ape"));
}
@Test
public void testCompareStringsStartingWithDifferentLetters() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("Dog", "Elephant"));
}
@Test
public void testCompareStringsStartingWithSameLetterAndDigits() {
    StringComparator comparator = new StringComparator();
    assertEquals(-1, comparator.compare("Cote1", "Cote2"));
}
}