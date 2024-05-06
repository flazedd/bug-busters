package tullibee_1;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Collection;
import java.util.Vector;
public class UtilTest_LLM {
@Test
public void testVectorEqualsUnordered() {
    Vector<String> vec1 = new Vector<>();
    vec1.add("apple");
    vec1.add("banana");
    vec1.add("orange");

    Vector<String> vec2 = new Vector<>();
    vec2.add("banana");
    vec2.add("orange");
    vec2.add("apple");

    assertTrue(Util.VectorEqualsUnordered(vec1, vec2));
}

}