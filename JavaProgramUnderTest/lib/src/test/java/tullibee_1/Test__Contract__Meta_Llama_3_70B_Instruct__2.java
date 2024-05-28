package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Contract__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testContractEquals() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    
    assertEquals(true, contract1.equals(contract2));
}

@Test
public void testContractClone() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = null;
    try {
        contract2 = (Contract) contract1.clone();
    } catch (CloneNotSupportedException e) {
        assert false;
    }
    
    assertEquals(true, contract1.equals(contract2));
}

@Test
public void testContractNotEquals() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractEqualsWithDifferentComboLegs() {
    Vector comboLegs1 = new Vector();
    comboLegs1.addElement("leg1");
    Vector comboLegs2 = new Vector();
    comboLegs2.addElement("leg2");
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs1, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs2, "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractEqualsWithDifferentSecId() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId1");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId2");
    
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractEqualsWithNull() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = null;
    
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractEqualsWithDifferentPrimaryExch() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch1", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch2", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractEqualsWithDifferentLocalSymbol() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol1", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol2", comboLegs, "primaryExch", false, "secIdType", "secId");
    
    assertEquals(false, contract1.equals(contract2));
}

}