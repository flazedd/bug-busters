package schemaspy_36;
import java.util.StringTokenizer;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.Test;
public class Test__Version__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testVersionComparison() {
    Version v1 = new Version("2.1.4");
    Version v2 = new Version("2.1.10");
    assertEquals(-1, v1.compareTo(v2));
}
@Test
public void testVersionEquality() {
    Version v1 = new Version("1.2.3");
    Version v2 = new Version("1.2.3");
    assertEquals(0, v1.compareTo(v2));
}
@Test
public void testVersionComparisonWithDifferentLengths() {
    Version v1 = new Version("1.2");
    Version v2 = new Version("1.2.3");
    assertEquals(-1, v1.compareTo(v2));
}
@Test
public void testVersionComparisonWithZeroSegments() {
    Version v1 = new Version("");
    Version v2 = new Version("1");
    assertEquals(-1, v1.compareTo(v2));
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
public void testVersionEqualityWithDifferentDelimiters() {
    Version v1 = new Version("1-2_3");
    Version v2 = new Version("1.2.3");
    assertEquals(0, v1.compareTo(v2));
}
@Test
public void testVersionComparisonWithLeadingZero() {
    Version v1 = new Version("1.02.3");
    Version v2 = new Version("1.2.3");
    assertEquals(0, v1.compareTo(v2));
}
@Test
public void testVersionComparisonWithTrailingZeros() {
    Version v1 = new Version("1.2.030");
    Version v2 = new Version("1.2.30");
    assertEquals(0, v1.compareTo(v2));
}
}