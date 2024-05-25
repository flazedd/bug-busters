package corina_35;
import org.junit.jupiter.api.Test;
import java.text.Collator;
import java.util.Comparator;
import static org.junit.jupiter.api.Assertions.*;
public class Test__StringComparator__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testEqualStrings() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "Hello"));
}

@Test
public void testCaseInsensitiveComparison() {
    StringComparator comparator = new StringComparator();
    assertEquals(0, comparator.compare("Hello", "hello"));
}

}