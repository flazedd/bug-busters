package schemaspy_36;
import java.util.Arrays;
import java.util.StringTokenizer;
import static org.junit.jupiter.api.Assertions.*;
import java.util.List;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
public class Test__Version__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testVersionComparison() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.10");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonEqual() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionComparisonMoreSegments() {
    Version version1 = new Version("1.2");
    Version version2 = new Version("1.2.3");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonLessSegments() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2");
    assertEquals(1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonEmptyString() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("");
    assertEquals(1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonMultipleDots() {
    Version version1 = new Version("1.2.3.4");
    Version version2 = new Version("1.2.3");
    assertEquals(1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonLeadingZero() {
    Version version1 = new Version("1.02.3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionComparisonUnderscore() {
    Version version1 = new Version("1.2_3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
}