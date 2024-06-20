package schemaspy_36;
import java.util.Arrays;
import java.util.StringTokenizer;
import static org.junit.jupiter.api.Assertions.*;
import java.util.List;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
public class Test__Version__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testVersionComparison() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.10");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithDifferentSegmentCount() {
    Version version1 = new Version("2.1");
    Version version2 = new Version("2.1.10");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithSameSegments() {
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
public void testVersionComparisonWithNullVersion() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version(null);
    assertEquals(1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithEmptyStringVersion() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("");
    assertEquals(1, version1.compareTo(version2));
}
@Test
public void testVersionEquals() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.4");
    assertTrue(version1.equals(version2));
}
@Test
public void testVersionHashCode() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.4");
    assertEquals(version1.hashCode(), version2.hashCode());
}
}