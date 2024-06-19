package saxpath_24;
import org.junit.jupiter.api.Test;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Map;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Axis__Meta_Llama_3_70B_Instruct__9 {
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
        assertEquals(Axis.INVALID_AXIS, Axis.lookup("unknown-axis"));
    }
@Test
    public void testLookupAncestor() {
        assertEquals("ancestor", Axis.lookup(Axis.ANCESTOR));
    }
@Test
    public void testLookupNamespace() {
        assertEquals("namespace", Axis.lookup(Axis.NAMESPACE));
    }
@Test
    public void testLookupInvalidAxisNum() {
        assertNull(Axis.lookup(14));
    }
@Test
    public void testLookupFollowingSibling() {
        assertEquals("following-sibling", Axis.lookup(Axis.FOLLOWING_SIBLING));
    }
@Test
    public void testLookupParent() {
        assertEquals("parent", Axis.lookup(Axis.PARENT));
    }
}