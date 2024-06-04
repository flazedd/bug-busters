package schemaspy_36;
import java.util.StringTokenizer;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import java.util.List;
public class Test__Version__Meta_Llama_3_70B_Instruct__5 {
@Test
public void versionComparisonTest() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.10");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void equalVersionTest() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void versionWithDifferentNumberOfSegmentsTest() {
    Version version1 = new Version("1.2");
    Version version2 = new Version("1.2.3");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void versionWithNullTest() {
    Version version1 = new Version(null);
    Version version2 = new Version("1.2.3");
    assertEquals(-1, version1.compareTo(version2));
}
@Test
public void versionWithStringTokenTest() {
    Version version1 = new Version("1-2_3");
    Version version2 = new Version("1.2.3");
    assertEquals(0, version1.compareTo(version2));
}
@Test
public void equalsTest() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.3");
    assertTrue(version1.equals(version2));
}
@Test
public void hashCodeTest() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.3");
    assertEquals(version1.hashCode(), version2.hashCode());
}
@Test
public void notEqualTest() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.4");
    assertFalse(version1.equals(version2));
}
}