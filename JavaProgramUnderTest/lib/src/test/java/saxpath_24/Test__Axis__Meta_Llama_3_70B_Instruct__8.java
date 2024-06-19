package saxpath_24;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.Map;
import static org.junit.jupiter.api.Assertions.*;
import java.util.HashMap;
public class Test__Axis__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testLookup() {
    assertEquals(Axis.CHILD, Axis.lookup("child"));
}
@Test
public void testLookupAxisName() {
    assertEquals("ancestor-or-self", Axis.lookup(Axis.ANCESTOR_OR_SELF));
}
@Test
public void testLookupInvalidAxis() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup("invalid-axis"));
}
@Test
public void testLookupDescendant() {
    assertEquals("descendant", Axis.lookup(Axis.DESCENDANT));
}
@Test
public void testLookupParent() {
    assertEquals("parent", Axis.lookup(Axis.PARENT));
}
@Test
public void testLookupNamespace() {
    assertEquals("namespace", Axis.lookup(Axis.NAMESPACE));
}
@Test
public void testLookupFollowingSibling() {
    assertEquals("following-sibling", Axis.lookup(Axis.FOLLOWING_SIBLING));
}
@Test
public void testLookupPreceding() {
    assertEquals("preceding", Axis.lookup(Axis.PRECEDING));
}
}