package saxpath_24;
import java.util.HashMap;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Map;
import org.junit.jupiter.api.Test;
public class Test__Axis__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testLookupAxisName() {
    assertEquals("child", Axis.lookup(Axis.CHILD));
}

@Test
public void testLookupAxisNumber() {
    assertEquals(Axis.DESCENDANT, Axis.lookup("descendant"));
}

}