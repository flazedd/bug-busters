package schemaspy_36;
import static org.junit.jupiter.api.Assertions.*;
import java.util.StringTokenizer;
import java.util.List;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;
public class Test__Version__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testVersionComparison() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.10");
    assertTrue(version1.compareTo(version2) < 0);
}

@Test
public void testVersionEquality() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.3");
    assertTrue(version1.equals(version2));
}

@Test
public void testVersionComparisonWithDifferentLengths() {
    Version version1 = new Version("1.2");
    Version version2 = new Version("1.2.3");
    assertTrue(version1.compareTo(version2) < 0);
}

@Test
public void testVersionComparisonWithSamePrefix() {
    Version version1 = new Version("1.2.3.4");
    Version version2 = new Version("1.2.3.5");
    assertTrue(version1.compareTo(version2) < 0);
}

@Test
public void testVersionToString() {
    Version version = new Version("1.2.3.4");
    assertEquals("1.2.3.4", version.toString());
}

@Test
public void testVersionComparisonWithNull() {
    Version version1 = new Version("1.2.3");
    assertFalse(version1.equals(null));
}

@Test
public void testVersionComparisonWithDifferentDelimiters() {
    Version version1 = new Version("1-2.3_4");
    Version version2 = new Version("1.2.3.4");
    assertTrue(version1.compareTo(version2) == 0);
}

@Test
public void testVersionComparisonWithEmptyString() {
    Version version1 = new Version("");
    Version version2 = new Version("1.2.3.4");
    assertTrue(version1.compareTo(version2) < 0);
}

}