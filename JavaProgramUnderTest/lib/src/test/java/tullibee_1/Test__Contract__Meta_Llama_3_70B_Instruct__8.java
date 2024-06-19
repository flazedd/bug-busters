package tullibee_1;
import java.util.Vector;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Contract__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testContractEquals() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    Contract contract2 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractNotEquals() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    Contract contract2 = new Contract(2, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentSymbol() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    Contract contract2 = new Contract(1, "XYZ", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentSecType() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    Contract contract2 = new Contract(1, "ABC", "OPT", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentComboLegs() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    Vector comboLegs = new Vector();
    comboLegs.add("leg1");
    Contract contract2 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", comboLegs, "NYSE", false, "", "");
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractNotEqualsDifferentUnderComp() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    __UnderComp underComp = new __UnderComp(); // assuming __UnderComp has a default constructor
    Contract contract2 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    contract2.m_underComp = underComp;
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractEqualsNull() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    assertEquals(false, contract1.equals(null));
}
@Test
public void testContractNotEqualsDifferentExchange() {
    Contract contract1 = new Contract(1, "ABC", "STK", "", 0, "", "", "NYSE", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    Contract contract2 = new Contract(1, "ABC", "STK", "", 0, "", "", "NASDAQ", "USD", "ABC", new Vector(), "NYSE", false, "", "");
    assertEquals(false, contract1.equals(contract2));
}
}