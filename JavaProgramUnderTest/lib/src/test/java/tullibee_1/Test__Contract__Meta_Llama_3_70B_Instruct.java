package tullibee_1;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class Test__Contract__Meta_Llama_3_70B_Instruct {
@Test
public void testContractEquals() {
    Contract contract1 = new Contract(1, "symbol1", "secType1", "expiry1", 10.0, "right1", "multiplier1", "exchange1", "currency1", "localSymbol1", new Vector(), "primaryExch1", false, "secIdType1", "secId1");
    Contract contract2 = new Contract(1, "symbol1", "secType1", "expiry1", 10.0, "right1", "multiplier1", "exchange1", "currency1", "localSymbol1", new Vector(), "primaryExch1", false, "secIdType1", "secId1");
    assertEquals(true, contract1.equals(contract2));
}

@Test
public void testContractClone() {
    Contract contract1 = new Contract(1, "symbol1", "secType1", "expiry1", 10.0, "right1", "multiplier1", "exchange1", "currency1", "localSymbol1", new Vector(), "primaryExch1", false, "secIdType1", "secId1");
    Contract contract2 = null;
    try {
        contract2 = (Contract) contract1.clone();
    } catch (CloneNotSupportedException e) {
        fail("CloneNotSupportedException should not be thrown");
    }
    assertEquals(contract1.m_conId, contract2.m_conId);
}

}