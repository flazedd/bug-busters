package saxpath_24;
import java.util.Arrays;
import java.util.Map;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.HashMap;
public class Test__Axis__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testLookupAxis() {
    assertEquals(Axis.CHILD, Axis.lookup("child"));
}
@Test
public void testLookupAxisName() {
    assertEquals("descendant-or-self", Axis.lookup(Axis.DESCENDANT_OR_SELF));
}
@Test
public void testLookupInvalidAxis() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup("unknown-axis"));
}
@Test
public void testLookupNamespaceAxis() {
    assertEquals("namespace", Axis.lookup(Axis.NAMESPACE));
}
@Test
public void testLookupAncestorAxis() {
    assertEquals(Axis.ANCESTOR, Axis.lookup("ancestor"));
}
@Test
public void testLookupFollowingAxis() {
    assertEquals("following", Axis.lookup(Axis.FOLLOWING));
}
@Test
public void testLookupParentAxis() {
    assertEquals("parent", Axis.lookup(Axis.PARENT));
}
@Test
public void testLookupAttributeAxis() {
    assertEquals(Axis.ATTRIBUTE, Axis.lookup("attribute"));
}
}