package tullibee_1;
import java.util.Arrays;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__Contract__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testContractEquals() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentConId() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentSecType() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "OPT", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentMultiplier() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier1", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier2", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentComboLegs() {
    Vector comboLegs1 = new Vector();
    comboLegs1.add("leg1");
    comboLegs1.add("leg2");
    
    Vector comboLegs2 = new Vector();
    comboLegs2.add("leg2");
    comboLegs2.add("leg1");
    
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs1, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs2, "primaryExch", false, "secIdType", "secId");
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentUnderComp() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = new __UnderComp();
    
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsNull() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(null));
}
@Test
public void testContractEqualsDifferentClass() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    String str = "Contract";
    assertEquals(false, contract1.equals(str));
}
}