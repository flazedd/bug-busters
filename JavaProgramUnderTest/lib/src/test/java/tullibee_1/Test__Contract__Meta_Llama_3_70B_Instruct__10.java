package tullibee_1;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Test__Contract__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testContractEquals() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractNotEquals() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsWithComboLegs() {
    Vector comboLegs1 = new Vector();
    comboLegs1.addElement("leg1");
    comboLegs1.addElement("leg2");
    
    Vector comboLegs2 = new Vector();
    comboLegs2.addElement("leg1");
    comboLegs2.addElement("leg2");
    
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs1, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs2, "primaryExch", false, "secIdType", "secId");
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractNotEqualsWithDifferentComboLegs() {
    Vector comboLegs1 = new Vector();
    comboLegs1.addElement("leg1");
    comboLegs1.addElement("leg2");
    
    Vector comboLegs2 = new Vector();
    comboLegs2.addElement("leg1");
    comboLegs2.addElement("leg3");
    
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs1, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs2, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractClone() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = null;
    try {
        contract2 = (Contract)contract1.clone();
    } catch (CloneNotSupportedException e) {
        fail("CloneNotSupportedException should not be thrown");
    }
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractEqualsWithDifferentUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = new __UnderComp(); // assume __UnderComp has a default constructor
    
    Contract contract2 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsWithNullUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = null;
    
    Contract contract2 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract2.m_underComp = new __UnderComp(); // assume __UnderComp has a default constructor
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsWithDifferentSecId() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId1");
    Contract contract2 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId2");
    assertEquals(false, contract1.equals(contract2));
}
}