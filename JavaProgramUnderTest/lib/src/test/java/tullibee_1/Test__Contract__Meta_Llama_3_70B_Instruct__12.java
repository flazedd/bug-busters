package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Contract__Meta_Llama_3_70B_Instruct__12 {
@Test
public void testContractEquality() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractInequality() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractInequalityWithDifferentSecType() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "OPT", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractInequalityWithDifferentComboLegs() {
    Vector comboLegs1 = new Vector();
    comboLegs1.add("leg1");
    comboLegs1.add("leg2");
    
    Vector comboLegs2 = new Vector();
    comboLegs2.add("leg1");
    comboLegs2.add("leg3");
    
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs1, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs2, "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractInequalityWithDifferentUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = new __UnderComp(); // assume __UnderComp is a class with a default constructor
    
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractNotEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentSecType() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "OPT", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}
}