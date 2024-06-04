package saxpath_24;
import java.util.Map;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.HashMap;
public class Test__Axis__Meta_Llama_3_70B_Instruct__5 {
@Test
public void testLookupAxis() {
    assertEquals(Axis.CHILD, Axis.lookup("child"));
}
@Test
public void testLookupAxisName() {
    assertEquals("descendant-or-self", Axis.lookup(Axis.DESCENDANT_OR_SELF));
}
@Test
public void testInvalidAxis() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup("invalid-axis"));
}
@Test
public void testLookupAxisNamespace() {
    assertEquals("namespace", Axis.lookup(Axis.NAMESPACE));
}
@Test
public void testLookupAxisAncestor() {
    assertEquals(Axis.ANCESTOR, Axis.lookup("ancestor"));
}
@Test
public void testLookupAxisWithMap() {
    Map<Integer, String> axisMap = new HashMap<>();
    for (int i = 1; i <= 13; i++) {
        axisMap.put(i, Axis.lookup(i));
    }
    assertEquals("ancestor-or-self", axisMap.get(Axis.ANCESTOR_OR_SELF));
}
@Test
public void testLookupAxisParent() {
    assertEquals("parent", Axis.lookup(Axis.PARENT));
}
@Test
public void testLookupAxisFollowingSibling() {
    assertEquals(Axis.FOLLOWING_SIBLING, Axis.lookup("following-sibling"));
}
}