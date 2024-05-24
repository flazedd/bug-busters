package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Test__Contract__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testContractEquality() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertTrue(contract1.equals(contract2));
}

@Test
public void testContractCloning() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = null;
    try {
        contract2 = (Contract)contract1.clone();
    } catch (CloneNotSupportedException e) {
        fail("CloneNotSupportedException should not be thrown");
    }
    assertEquals(contract1.m_conId, contract2.m_conId);
}



}