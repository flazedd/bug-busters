package schemaspy_36;
import java.util.StringTokenizer;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.List;
public class Test__Version__Meta_Llama_3_70B_Instruct__1 {
@Test
public void versionComparisonTest() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.4");
    assertEquals(0, version1.compareTo(version2));
}

@Test
public void versionComparisonTest2() {
    Version version1 = new Version("2.1.3");
    Version version2 = new Version("2.1.4");
    assertTrue(version1.compareTo(version2) < 0);
}

@Test
public void versionComparisonTest3() {
    Version version1 = new Version("2.1.10");
    Version version2 = new Version("2.1.4");
    assertTrue(version1.compareTo(version2) > 0);
}

@Test
public void versionComparisonTest4() {
    Version version1 = new Version("1.2.3");
    Version version2 = new Version("1.2.3.4");
    assertTrue(version1.compareTo(version2) < 0);
}

@Test
public void versionComparisonTest5() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1");
    assertTrue(version1.compareTo(version2) > 0);
}

@Test
public void versionComparisonTest6() {
    Version version1 = new Version("2.10.4");
    Version version2 = new Version("2.2.4");
    assertTrue(version1.compareTo(version2) > 0);
}

@Test
public void versionComparisonTest8() {
    Version version1 = new Version("2.1.4");
    assertEquals("2.1.4", version1.toString());
}

@Test
public void versionComparisonTest10() {
    Version version1 = new Version("1.2.3");
    assertEquals("1.2.3", version1.toString());
}







}