package saxpath_24;
import java.util.Map;
import org.junit.jupiter.api.Test;
import java.util.HashMap;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Axis__Meta_Llama_3_70B_Instruct__2 {
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
public void testLookupNamespace() {
    assertEquals("namespace", Axis.lookup(Axis.NAMESPACE));
}

@Test
public void testLookupAncestor() {
    assertEquals(Axis.ANCESTOR, Axis.lookup("ancestor"));
}

@Test
public void testLookupSelf() {
    assertEquals("self", Axis.lookup(Axis.SELF));
}

@Test
public void testLookupMap() {
    Map<Integer, String> axisMap = new HashMap<>();
    for (int i = 1; i <= 13; i++) {
        axisMap.put(i, Axis.lookup(i));
    }
    assertEquals(13, axisMap.size());
}

@Test
public void testLookupParent() {
    assertEquals(Axis.PARENT, Axis.lookup("parent"));
}

}