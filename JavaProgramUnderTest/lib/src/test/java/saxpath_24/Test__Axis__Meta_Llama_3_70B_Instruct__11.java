package saxpath_24;
import java.util.Map;
import java.util.Arrays;
import java.util.HashMap;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Axis__Meta_Llama_3_70B_Instruct__11 {
@Test
    public void lookupTest() {
        assertEquals("child", Axis.lookup(Axis.CHILD));
    }
@Test
    public void lookupTest2() {
        assertEquals(Axis.DESCENDANT, Axis.lookup("descendant"));
    }
@Test
    public void lookupTest3() {
        assertEquals(null, Axis.lookup(15));
    }
@Test
    public void lookupTest4() {
        assertEquals(Axis.INVALID_AXIS, Axis.lookup("invalid-axis"));
    }
@Test
    public void lookupTest5() {
        assertEquals("ancestor-or-self", Axis.lookup(Axis.ANCESTOR_OR_SELF));
    }
@Test
    public void lookupTest6() {
        assertEquals(Axis.FOLLOWING_SIBLING, Axis.lookup("following-sibling"));
    }
@Test
    public void lookupTest7() {
        assertEquals("namespace", Axis.lookup(Axis.NAMESPACE));
    }
@Test
    public void lookupTest8() {
        assertEquals(Axis.PARENT, Axis.lookup("parent"));
    }
}