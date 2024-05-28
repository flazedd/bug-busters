package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Contract__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testContractEquality() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(true, contract1.equals(contract2));
}

@Test
public void testContractInequality() {
    Vector comboLegs1 = new Vector();
    comboLegs1.add("leg1");
    Vector comboLegs2 = new Vector();
    comboLegs2.add("leg2");
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs1, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs2, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractInequalityDifferentConId() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractInequalityDifferentSecType() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "STOCK", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "OPTION", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractInequalityDifferentExpiry() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "2022-01-01", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "2023-01-01", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractInequalityDifferentRight() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "CALL", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "PUT", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}

@Test
public void testContractCloning() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = null;
    try {
        contract2 = (Contract)contract1.clone();
    } catch (CloneNotSupportedException e) {
        fail("CloneNotSupportedException should not be thrown");
    }
    assertEquals(true, contract1.equals(contract2));
}

@Test
public void testContractInequalityDifferentCurrency() {
    Vector comboLegs = new Vector();
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "USD", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 10.0, "right", "multiplier", "exchange", "EUR", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}

}