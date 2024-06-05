package saxpath_24;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.HashMap;
import java.util.Map;
public class Test__Axis__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testLookup() {
    assertEquals(Axis.CHILD, Axis.lookup("child"));
}
@Test
public void testLookupDescendantOrSelf() {
    assertEquals(Axis.DESCENDANT_OR_SELF, Axis.lookup("descendant-or-self"));
}
@Test
public void testLookupInvalidAxis() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup("invalid-axis"));
}
@Test
public void testLookupNamespace() {
    assertEquals(Axis.NAMESPACE, Axis.lookup("namespace"));
}
@Test
public void testLookupString() {
    assertEquals("ancestor-or-self", Axis.lookup(Axis.ANCESTOR_OR_SELF));
}
@Test
public void testLookupParent() {
    assertEquals("parent", Axis.lookup(Axis.PARENT));
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