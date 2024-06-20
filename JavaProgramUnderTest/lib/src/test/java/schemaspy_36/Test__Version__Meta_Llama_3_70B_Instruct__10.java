package schemaspy_36;
import java.util.List;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.StringTokenizer;
import java.util.ArrayList;
public class Test__Version__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testVersionComparison() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.10");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithDifferentLengths() {
    Version version1 = new Version("2.1");
    Version version2 = new Version("2.1.1");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithSameVersion() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.4");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithLeadingZero() {
    Version version1 = new Version("2.01.4");
    Version version2 = new Version("2.1.4");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithNull() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version(null);
    assertEquals(1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithEmptyString() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("");
    assertEquals(1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithNonNumericSegment() {
    try {
        new Version("2.1.a");
        assert false;
    } catch (NumberFormatException e) {
        // Expected
    }
}
@Test
public void testVersionComparisonWithDifferentDelimiters() {
    Version version1 = new Version("2-1.4");
    Version version2 = new Version("2.1.4");
    assertEquals(0, version1.compareTo(version2));
}
}