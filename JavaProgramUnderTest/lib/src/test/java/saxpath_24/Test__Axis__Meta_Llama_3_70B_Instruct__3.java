package saxpath_24;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
public class Test__Axis__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testLookupAxisName() {
    assertEquals("child", Axis.lookup(Axis.CHILD));
}

@Test
public void testLookupAxisNumber() {
    assertEquals(Axis.DESCENDANT, Axis.lookup("descendant"));
}

@Test
public void testLookupInvalidAxis() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup("invalid-axis"));
}

@Test
public void testLookupAxisNameCaseInsensitive() {
    assertEquals("ancestor-or-self", Axis.lookup(Axis.ANCESTOR_OR_SELF));
}

@Test
public void testLookupAxisNameLowerCase() {
    assertEquals(Axis.DESCENDANT, Axis.lookup("descendant".toLowerCase()));
}

@Test
public void testLookupAxisNameHyphen() {
    assertEquals(Axis.FOLLOWING_SIBLING, Axis.lookup("following-sibling"));
}

@Test
public void testLookupAxisNameWithSpaces() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup(" ancestor "));
}

@Test
public void testLookupAxisNameNull() {
    assertEquals(Axis.INVALID_AXIS, Axis.lookup(null));
}

}