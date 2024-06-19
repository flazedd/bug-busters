package schemaspy_36;
import java.util.StringTokenizer;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Version__Meta_Llama_3_70B_Instruct__8 {
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
public void testVersionComparisonWithDifferentLength() {
    Version version1 = new Version("1.2");
    Version version2 = new Version("1.2.3");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithLeadingZero() {
    Version version1 = new Version("1.02.3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionComparisonWithNull() {
    Version version1 = new Version("1.2.3");
    try {
        version1.compareTo(null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}
@Test
public void testVersionComparisonWithDifferentDelimiters() {
    Version version1 = new Version("1-2.3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void testVersionToString() {
    Version version = new Version("1.2.3");
    assertEquals("1.2.3", version.toString());
}
@Test
public void testVersionHashCode() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.3");
    assertEquals(version1.hashCode(), version2.hashCode());
}
}