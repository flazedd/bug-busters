package schemaspy_36;
import static org.junit.jupiter.api.Assertions.*;
import java.util.List;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import java.util.StringTokenizer;
public class Test__Version__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testVersionComparison() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.4");
    assertEquals(0, version1.compareTo(version2));
}

@Test
public void testVersionComparison_LessThan() {
    Version version1 = new Version("2.1.4");
    Version version2 = new Version("2.1.10");
    assertTrue(version1.compareTo(version2) < 0);
}

}