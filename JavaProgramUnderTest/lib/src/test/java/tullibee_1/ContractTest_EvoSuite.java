package tullibee_1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class ContractTest_EvoSuite {
    @Test
    public void test0()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = (Contract)contract0.clone();
        assertTrue(contract1.equals(contract0));

        contract0.m_localSymbol = "O?bHS";
        boolean boolean0 = contract0.equals((Object) contract1);
        assertEquals(false, boolean0);
    }

    @Test
    public void test1()  throws Throwable  {
        Contract contract0 = new Contract();
        boolean boolean0 = contract0.equals((Object) null);
        assertEquals(false, contract0.m_includeExpired);
        assertEquals(0, contract0.m_conId);
        assertEquals(0.0, contract0.m_strike, 0.01D);
        assertEquals(false, boolean0);
    }

    @Test
    public void test2()  throws Throwable  {
        Contract contract0 = new Contract();
        Object object0 = new Object();
        boolean boolean0 = contract0.equals(object0);
        assertEquals(false, boolean0);
        assertEquals(false, contract0.m_includeExpired);
        assertEquals(0.0, contract0.m_strike, 0.01D);
        assertEquals(0, contract0.m_conId);
    }

    @Test
    public void test3()  throws Throwable  {
        Contract contract0 = new Contract();
        Vector<Object> vector0 = new Vector<Object>();
        Contract contract1 = new Contract((-516), "BOND", "BOND", "BOND", (double) (-516), "BOND", "BOND", "BOND", "BOND", (String) null, (Vector) vector0, "BOND", false, "BOND", "BOND");
        Contract contract2 = (Contract)contract0.clone();
        boolean boolean0 = contract1.equals((Object) contract2);
        assertEquals(false, boolean0);
        assertEquals((-516), contract1.m_conId);
        assertEquals(false, contract1.m_includeExpired);
        assertTrue(contract2.equals(contract0));
    }

    @Test
    public void test4()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = new Contract((-1), "jOND", "jOND", "jOND", (double) (-1), "jOND", "jOND", "jOND", "jOND", "jOND", (Vector) contract0.m_comboLegs, (String) null, false, (String) null, "jOND");
        Contract contract2 = new Contract((-1), "jOND", (String) null, (String) null, (-1.0), "jOND", "jOND", "jOND", (String) null, (String) null, (Vector) contract0.m_comboLegs, "jOND", false, (String) null, (String) null);
        contract1.equals((Object) contract2);
        assertEquals(0.0, contract0.m_strike, 0.01D);
        assertEquals((-1), contract1.m_conId);
        assertEquals(false, contract0.m_includeExpired);
        assertEquals((-1.0), contract1.m_strike, 0.01D);
        assertEquals(0, contract0.m_conId);
        assertEquals(false, contract1.m_includeExpired);
    }

    @Test
    public void test5()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = (Contract)contract0.clone();
        assertTrue(contract0.equals(contract1));
        assertNotNull(contract1);

        contract0.m_symbol = "ON";
        boolean boolean0 = contract0.equals((Object) contract1);
        assertFalse(contract0.equals(contract1));
        assertEquals(false, boolean0);
    }

    @Test
    public void test6()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = (Contract)contract0.clone();
        Contract contract2 = new Contract(0, (String) null, (String) null, "0FUX>AV|C `", (double) 0, (String) null, (String) null, "0FUX>AV|C `", "0FUX>AV|C `", (String) null, (Vector) contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
        boolean boolean0 = contract2.equals((Object) contract1);
        assertEquals(0.0, contract1.m_strike, 0.01D);
        assertEquals(false, boolean0);
        assertEquals(false, contract2.m_includeExpired);
        assertEquals(0, contract2.m_conId);
        assertTrue(contract1.equals(contract0));
    }

    @Test
    public void test7()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = (Contract)contract0.clone();
        assertNotNull(contract1);
        assertTrue(contract1.equals(contract0));

        contract0.m_primaryExch = "E";
        boolean boolean0 = contract0.equals((Object) contract1);
        assertFalse(contract0.equals(contract1));
        assertEquals(false, boolean0);
    }

    @Test
    public void test8()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0.0, (String) null, ":&<jC9.<3Z~@eStW", (String) null, (String) null, (String) null, (Vector) contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
        contract0.m_currency = ":&<jC9.<3Z~@eStW";
        Contract contract2 = (Contract)contract1.clone();
        assertNotNull(contract2);

        boolean boolean0 = contract0.equals((Object) contract2);
        assertTrue(contract1.equals(contract2));
        assertEquals(0, contract0.m_conId);
        assertFalse(contract0.equals(contract1));
        assertEquals(0.0, contract1.m_strike, 0.01D);
        assertEquals(false, boolean0);
    }

    @Test
    public void test9()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = (Contract)contract0.clone();
        assertNotNull(contract1);
        assertTrue(contract0.equals(contract1));

        contract0.m_strike = (-698.9376271409143);
        boolean boolean0 = contract0.equals((Object) contract1);
        assertEquals(false, boolean0);
    }

    @Test
    public void test10()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = new Contract();
        assertTrue(contract1.equals(contract0));

        contract1.m_expiry = "BOND";
        Contract contract2 = (Contract)contract0.clone();
        boolean boolean0 = contract1.equals((Object) contract2);
        assertEquals(false, boolean0);
    }

    @Test
    public void test11()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = (Contract)contract0.clone();
        assertTrue(contract1.equals(contract0));

        contract0.m_right = "0FUX>AV|C `";
        boolean boolean0 = contract0.equals((Object) contract1);
        assertEquals(false, boolean0);
    }

    @Test
    public void test12()  throws Throwable  {
        Contract contract0 = new Contract();
        Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0.0, (String) null, ":&<jC9.<3Z~@eStW", (String) null, (String) null, (String) null, (Vector) contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
        boolean boolean0 = contract0.equals((Object) contract1);
        assertEquals(0, contract1.m_conId);
        assertEquals(false, contract1.m_includeExpired);
        assertEquals(false, boolean0);
    }

//    @Test
//    public void test13()  throws Throwable  {
//        Contract contract0 = new Contract();
//        contract0.m_secIdType = "BOND";
//        Contract contract1 = new Contract();
//        Contract contract2 = (Contract)contract1.clone();
//        boolean boolean0 = contract0.equals((Object) contract2);
//        assertNotSame(contract1, contract2);
//        assertEquals(false, boolean0);
//        assertEquals(0.0, contract1.m_strike, 0.01D);
//        assertTrue(contract1.equals(contract2));
//    }
//
//    @Test
//    public void test14()  throws Throwable  {
//        Contract contract0 = new Contract();
//        contract0.m_secId = "'L";
//        Contract contract1 = new Contract();
//        contract0.equals((Object) contract1);
//        assertEquals(false, contract0.m_includeExpired);
//        assertEquals(0.0, contract0.m_strike, 0.01D);
//        assertEquals(false, contract1.m_includeExpired);
//    }
//
//    @Test
//    public void test15()  throws Throwable  {
//        Vector<Object> vector0 = new Vector<Object>();
//        Contract contract0 = new Contract((-516), "BOND", "BOND", "BOND", (double) (-516), "BOND", "BOND", "BOND", "BOND", (String) null, (Vector) vector0, "BOND", false, "BOND", "BOND");
//        Contract contract1 = (Contract)contract0.clone();
//        assertTrue(contract0.equals(contract1));
//
//        vector0.add((Object) contract1);
//        boolean boolean0 = contract0.equals((Object) contract1);
//        assertEquals(false, boolean0);
//    }
//
//    @Test
//    public void test16()  throws Throwable  {
//        Contract contract0 = new Contract();
//        Contract contract1 = new Contract();
//        assertTrue(contract1.equals(contract0));
//
//        UnderComp underComp0 = new UnderComp();
//        contract1.m_underComp = (UnderComp) underComp0;
//        boolean boolean0 = contract1.equals((Object) contract0);
//        assertEquals(false, boolean0);
//    }
//
//    @Test
//    public void test17()  throws Throwable  {
//        Contract contract0 = new Contract();
//        Contract contract1 = new Contract();
//        UnderComp underComp0 = new UnderComp();
//        contract0.m_underComp = (UnderComp) underComp0;
//        assertFalse(contract0.equals(contract1));
//
//        UnderComp underComp1 = new UnderComp();
//        contract1.m_underComp = (UnderComp) underComp1;
//        boolean boolean0 = contract1.equals((Object) contract0);
//        assertTrue(contract0.equals(contract1));
//        assertEquals(true, boolean0);
//    }
}
