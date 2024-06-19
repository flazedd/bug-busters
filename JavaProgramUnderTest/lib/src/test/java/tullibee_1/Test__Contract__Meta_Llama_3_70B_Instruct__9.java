package tullibee_1;
import java.util.Arrays;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Contract__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testContractEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertTrue(contract1.equals(contract2));
}
@Test
public void testContractNotEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDueToSecType() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "OPT", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDueToComboLegs() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Vector comboLegs = new Vector();
    comboLegs.addElement("leg1");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractClone() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = null;
    try {
        contract2 = (Contract)contract1.clone();
    } catch (CloneNotSupportedException e) {
        fail("CloneNotSupportedException should not be thrown");
    }
    assertTrue(contract1.equals(contract2));
}
@Test
public void testContractEqualsWithNullUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = null;
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract2.m_underComp = null;
    assertTrue(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsWithDifferentUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = new __UnderComp(); // assuming __UnderComp has a default constructor
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractEqualsWithSameUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = new __UnderComp(); // assuming __UnderComp has a default constructor
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract2.m_underComp = new __UnderComp(); // assuming __UnderComp has a default constructor
    assertTrue(contract1.equals(contract2));
}
}