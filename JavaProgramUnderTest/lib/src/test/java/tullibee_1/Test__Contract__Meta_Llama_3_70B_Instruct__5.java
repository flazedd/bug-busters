package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__Contract__Meta_Llama_3_70B_Instruct__5 {
@Test
public void testContractEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractNotEquals() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(2, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentSecType() {
    Contract contract1 = new Contract(1, "symbol", "STK", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "OPT", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentComboLegs() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Vector comboLegs = new Vector();
    comboLegs.add("leg1");
    comboLegs.add("leg2");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", comboLegs, "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentUnderComp() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    contract1.m_underComp = new __UnderComp();
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsNull() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(null));
}
@Test
public void testContractEqualsDifferentLocalSymbol() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol1", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol2", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsDifferentCurrency() {
    Contract contract1 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency1", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract contract2 = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency2", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    assertEquals(false, contract1.equals(contract2));
}
}