package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Contract__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testContractEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertTrue(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentConId() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentSecType() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "OPT", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentComboLegs() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Vector comboLegs = new Vector();
    comboLegs.add("leg1");
    Contract contract2 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = new __UnderComp(); // assume __UnderComp is a class
    Contract contract2 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractClone() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = null;
    
    try {
        contract2 = (Contract) contract1.clone();
    } catch (CloneNotSupportedException e) {
        fail("CloneNotSupportedException should not be thrown");
    }
    
    assertTrue(contract1.equals(contract2));
}
@Test
public void testContractEqualsNull() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertFalse(contract1.equals(null));
}
@Test
public void testContractEqualsDifferentClass() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Object obj = new Object();
    
    assertFalse(contract1.equals(obj));
}
}