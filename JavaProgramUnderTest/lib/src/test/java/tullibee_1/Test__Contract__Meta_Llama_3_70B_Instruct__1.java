package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
import org.junit.jupiter.api.Test;
public class Test__Contract__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testContractEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(true, contract1.equals(contract2));
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
    
    assertEquals(true, contract1.equals(contract2));
}

@Test
public void testContractNotEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractEqualsDifferentSecType() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "OPT", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractEqualsDifferentComboLegs() {
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
public void testContractEqualsDifferentUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = new __UnderComp(); // assume __UnderComp has a default constructor
    
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractEqualsNull() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(null));
}

@Test
public void testContractEqualsDifferentCurrency() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "USD", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "EUR", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}









}