package schemaspy_36;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.ArrayList;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Version__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testVersionComparison() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.10");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionEquality() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithDifferentLengths() {
    Version version1 = new Version("1.2");
    Version version2 = new Version("1.2.3");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithNullSegment() {
    Version version1 = new Version("1.2.");
    Version version2 = new Version("1.2.1");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionEqualityWithNull() {
    Version version1 = new Version("1.2.3");
    assertEquals(false, version1.equals(null));
}
@Test
public void testVersionComparisonWithMultipleDots() {
    Version version1 = new Version("1.2..3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithDifferentSeparators() {
    Version version1 = new Version("1-2_3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionToString() {
    Version version = new Version("1.2.3");
    assertEquals("1.2.3", version.toString());
}
}