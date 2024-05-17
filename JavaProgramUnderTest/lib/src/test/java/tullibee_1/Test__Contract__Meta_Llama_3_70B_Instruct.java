package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Contract__Meta_Llama_3_70B_Instruct {
@Test
public void testEquals() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "SMART", "USD", "ABC", new Vector(), "SMART", false, "", "");
    Contract contract2 = new Contract(1, "ABC", "STK", "", 0, "", "", "SMART", "USD", "ABC", new Vector(), "SMART", false, "", "");
    assertEquals(true, contract1.equals(contract2));
}

@Test
public void testClone() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "SMART", "USD", "ABC", new Vector(), "SMART", false, "", "");
    try {
        Contract contract2 = (Contract) contract1.clone();
        assertEquals(true, contract1.equals(contract2));
    } catch (CloneNotSupportedException e) {
        fail("CloneNotSupportedException should not be thrown");
    }
}

}