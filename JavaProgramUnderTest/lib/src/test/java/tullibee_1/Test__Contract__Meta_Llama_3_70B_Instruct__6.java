package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class Test__Contract__Meta_Llama_3_70B_Instruct__6 {
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
public void testContractEqualsWithComboLegs() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Vector comboLegs = new Vector();
    comboLegs.addElement("leg1");
    comboLegs.addElement("leg2");
    contract1.m_comboLegs = comboLegs;
    
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Vector comboLegs2 = new Vector();
    comboLegs2.addElement("leg1");
    comboLegs2.addElement("leg2");
    contract2.m_comboLegs = comboLegs2;
    
    assertTrue(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsWithComboLegs() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Vector comboLegs = new Vector();
    comboLegs.addElement("leg1");
    comboLegs.addElement("leg2");
    contract1.m_comboLegs = comboLegs;
    
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Vector comboLegs2 = new Vector();
    comboLegs2.addElement("leg1");
    comboLegs2.addElement("leg3");
    contract2.m_comboLegs = comboLegs2;
    
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractEqualsWithUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    __UnderComp underComp1 = new __UnderComp(); // assuming __UnderComp has a default constructor
    contract1.m_underComp = underComp1;
    
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    __UnderComp underComp2 = new __UnderComp(); // assuming __UnderComp has a default constructor
    contract2.m_underComp = underComp2;
    
    assertTrue(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsWithUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    __UnderComp underComp1 = new __UnderComp(); // assuming __UnderComp has a default constructor
    contract1.m_underComp = underComp1;
    
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract2.m_underComp = null;
    
    assertFalse(contract1.equals(contract2));
}
@Test
public void testContractEqualsWithSecId() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId1");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId1");
    assertTrue(contract1.equals(contract2));
}
@Test
public void testContractNotEqualsWithSecId() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId1");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId2");
    assertFalse(contract1.equals(contract2));
}
}