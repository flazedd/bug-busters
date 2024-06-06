package saxpath_24;
import java.util.HashMap;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Map;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
public class Test__Axis__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testLookup() {
    assertEquals(Axis.DESCENDANT, Axis.lookup("descendant"));
}
@Test
public void testLookup2() {
    assertEquals("ancestor-or-self", Axis.lookup(Axis.ANCESTOR_OR_SELF));
}
@Test
public void testLookup3() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup("invalid-axis"));
}
@Test
public void testLookup4() {
    assertEquals("attribute", Axis.lookup(Axis.ATTRIBUTE));
}
@Test
public void testLookup5() {
    assertEquals(null, Axis.lookup(15));
}
@Test
public void testLookup6() {
    assertEquals("following", Axis.lookup(Axis.FOLLOWING));
}
@Test
public void testLookup7() {
    assertEquals(Axis.PARENT, Axis.lookup("parent"));
}
@Test
public void testLookup8() {
    assertEquals("namespace", Axis.lookup(Axis.NAMESPACE));
}
}