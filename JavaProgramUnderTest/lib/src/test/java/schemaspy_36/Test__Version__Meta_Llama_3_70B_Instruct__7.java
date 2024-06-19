package schemaspy_36;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import java.util.StringTokenizer;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Version__Meta_Llama_3_70B_Instruct__7 {
@Test
public void testVersionComparison() {
    Version v1 = new Version("2.1.4");
    Version v2 = new Version("2.1.10");
    assertEquals(-1, v1.compareTo(v2));
}
@Test
public void testVersionComparisonEqual() {
    Version v1 = new Version("1.2.3");
    Version v2 = new Version("1.2.3");
    assertEquals(0, v1.compareTo(v2));
}
@Test
public void testVersionComparisonMoreSegments() {
    Version v1 = new Version("1.2");
    Version v2 = new Version("1.2.3");
    assertEquals(-1, v1.compareTo(v2));
}
@Test
public void testVersionComparisonMoreSegmentsReversed() {
    Version v1 = new Version("1.2.3");
    Version v2 = new Version("1.2");
    assertEquals(1, v1.compareTo(v2));
}
@Test
public void testVersionComparisonWithNullVersion() {
    Version v1 = new Version("1.2.3");
    Version v2 = null;
    try {
        v1.compareTo(v2);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // Expected
    }
}
@Test
public void testVersionComparisonWithVersionHavingDifferentDelimiters() {
    Version v1 = new Version("1-2.3");
    Version v2 = new Version("1.2.3");
    assertEquals(0, v1.compareTo(v2));
}
@Test
public void testVersionToString() {
    Version v1 = new Version("1.2.3");
    assertEquals("1.2.3", v1.toString());
}
@Test
public void testVersionHashCode() {
    Version v1 = new Version("1.2.3");
    Version v2 = new Version("1.2.3");
    assertEquals(v1.hashCode(), v2.hashCode());
}
}