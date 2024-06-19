package tullibee_1;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__Contract__Meta_Llama_3_70B_Instruct__7 {
@Test
public void testContractEquality() {
    Contract contract1 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", new Vector(), "NYSE", false, "ISIN", "US1234567890");
    Contract contract2 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", new Vector(), "NYSE", false, "ISIN", "US1234567890");
    
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractInequality() {
    Contract contract1 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", new Vector(), "NYSE", false, "ISIN", "US1234567890");
    Contract contract2 = new Contract(2, "DEF", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "DEF123", new Vector(), "NYSE", false, "ISIN", "US9876543210");
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractComboLegsEquality() {
    Vector comboLegs1 = new Vector();
    comboLegs1.addElement("Leg1");
    comboLegs1.addElement("Leg2");
    
    Vector comboLegs2 = new Vector();
    comboLegs2.addElement("Leg1");
    comboLegs2.addElement("Leg2");
    
    Contract contract1 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", comboLegs1, "NYSE", false, "ISIN", "US1234567890");
    Contract contract2 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", comboLegs2, "NYSE", false, "ISIN", "US1234567890");
    
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractClone() {
    Contract contract1 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", new Vector(), "NYSE", false, "ISIN", "US1234567890");
    
    try {
        Contract contract2 = (Contract)contract1.clone();
        assertEquals(true, contract1.equals(contract2));
    } catch (CloneNotSupportedException e) {
        fail("CloneNotSupportedException should not be thrown");
    }
}
@Test
public void testContractInequalityWithNull() {
    Contract contract1 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", new Vector(), "NYSE", false, "ISIN", "US1234567890");
    Contract contract2 = null;
    
    assertEquals(false, contract1.equals(contract2));
}
@Test
public void testContractInequalityWithDifferentClass() {
    Contract contract1 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", new Vector(), "NYSE", false, "ISIN", "US1234567890");
    Object obj = new Object();
    
    assertEquals(false, contract1.equals(obj));
}
@Test
public void testContractEqualityWithSameUnderComp() {
    Contract contract1 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", new Vector(), "NYSE", false, "ISIN", "US1234567890");
    Contract contract2 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", new Vector(), "NYSE", false, "ISIN", "US1234567890");
    
    // assume __UnderComp has an equals method
    __UnderComp underComp = new __UnderComp();
    
    contract1.m_underComp = underComp;
    contract2.m_underComp = underComp;
    
    assertEquals(true, contract1.equals(contract2));
}
@Test
public void testContractComboLegsInequality() {
    Vector comboLegs1 = new Vector();
    comboLegs1.addElement("Leg1");
    comboLegs1.addElement("Leg2");
    
    Vector comboLegs2 = new Vector();
    comboLegs2.addElement("Leg1");
    comboLegs2.addElement("Leg3");
    
    Contract contract1 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", comboLegs1, "NYSE", false, "ISIN", "US1234567890");
    Contract contract2 = new Contract(1, "ABC", "STK", "20221231", 100.0, "CALL", "1", "NYSE", "USD", "ABC123", comboLegs2, "NYSE", false, "ISIN", "US1234567890");
    
    assertEquals(false, contract1.equals(contract2));
}
}