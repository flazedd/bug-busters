package saxpath_24;
import static org.junit.jupiter.api.Assertions.*;
import java.util.HashMap;
import java.util.Map;
import org.junit.jupiter.api.Test;
public class Test__Axis__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testLookup() {
    assertEquals("child", Axis.lookup(Axis.CHILD));
}

@Test
public void testLookupInverse() {
    assertEquals(Axis.DESCENDANT_OR_SELF, Axis.lookup("descendant-or-self"));
}

@Test
public void testLookupInvalid() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup("unknown-axis"));
}

@Test
public void testLookupAncestor() {
    assertEquals("ancestor", Axis.lookup(Axis.ANCESTOR));
}

@Test
public void testLookupNamespace() {
    assertEquals(Axis.NAMESPACE, Axis.lookup("namespace"));
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
public void testLookupSelf() {
    assertEquals(Axis.SELF, Axis.lookup("self"));
}



}