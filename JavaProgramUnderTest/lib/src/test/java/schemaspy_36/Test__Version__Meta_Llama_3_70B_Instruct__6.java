package schemaspy_36;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
import org.junit.jupiter.api.Test;
import java.util.List;
public class Test__Version__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testVersionComparison() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.10");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithDifferentSegmentCounts() {
    Version version1 = new Version("2.1");
    Version version2 = new Version("2.1.10");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithEqualVersions() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.4");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithNullVersion() {
    Version version1 = new Version("2.1.4");
    Version version2 = null;
    assertFalse(version1.equals(version2));
}
@Test
public void testVersionComparisonWithDifferentSegmentValues() {
    Version version1 = new Version("2.1.10");
    Version version2 = new Version("2.2.0");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithNonVersionObject() {
    Version version1 = new Version("2.1.4");
    String version2 = "2.1.4";
    assertFalse(version1.equals(version2));
}
@Test
public void testVersionComparisonWithEmptyVersion() {
    Version version1 = new Version("1.0.0");
    Version version2 = new Version("");
    assertEquals(1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithVersionHavingSpecialCharacters() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1-4");
    assertEquals(0, version1.compareTo(version2));
}
}