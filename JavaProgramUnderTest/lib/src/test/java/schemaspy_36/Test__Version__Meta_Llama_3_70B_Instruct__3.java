package schemaspy_36;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.StringTokenizer;
public class Test__Version__Meta_Llama_3_70B_Instruct__3 {
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
public void testVersionGreater() {
    Version version1 = new Version("2.1.10");
    Version version2 = new Version("2.1.4");
    assertEquals(1, version1.compareTo(version2));
}

@Test
public void testVersionWithDifferentSegmentCounts() {
    Version version1 = new Version("1.2");
    Version version2 = new Version("1.2.3");
    assertEquals(-1, version1.compareTo(version2));
}

@Test
public void testVersionWithNull() {
    Version version1 = new Version("1.2.3");
    try {
        version1.compareTo(null);
        fail("Expected NullPointerException");
    } catch (NullPointerException e) {
        // expected
    }
}

@Test
public void testVersionWithEmptyString() {
    Version version1 = new Version("");
    assertEquals(0, version1.compareTo(new Version("")));
}

@Test
public void testVersionWithLeadingZero() {
    Version version1 = new Version("1.02.3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}

@Test
public void testVersionWithMultipleLeadingZeros() {
    Version version1 = new Version("1.002.003");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}

}