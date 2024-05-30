package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Contract_ESTest_3 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "Yebza5]";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 2343.0, (String) null, (String) null, (String) null, (String) null, "com.ib.client.__UnderComp", contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(2343.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, "PQtV/LP*]0e", 0.0, (String) null, "vj's;^v", (String) null, "PQtV/LP*]0e", "Yebza5]", contract0.m_comboLegs, (String) null, true, "fSHP,PYc![QYg1]K1_", "W");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract0.m_conId);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_exchange = "2J$RW4ATM)e,Fv\",hi";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.equals((Object)contract0));
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_symbol = "BOND";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(0, "com.ib.client.Contract", "com.ib.client.Contract", "com.ib.client.Contract", 0, "com.ib.client.Contract", "com.ib.client.Contract", "", "", "", vector0, "A%i![z &|", true, "", (String) null);
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertTrue(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0, contract0.m_conId);
      
      contract0.m_conId = 1828;
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add((Object) null);
      Contract contract0 = new Contract(1229, "AJ2B", "AJ2B", "AJ2B", 1229, "AJ2B", "AJ2B", "AJ2B", "AJ2B", "AJ2B", vector0, "AJ2B", true, "AJ2B", "AJ2B");
      Object object0 = contract0.clone();
      // Undeclared exception!
      try { 
        contract0.equals(object0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.ib.client.Util", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_comboLegs = null;
      // Undeclared exception!
      try { 
        contract0.clone();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.ib.client.Contract", e);
      }
  }

  @Test
  public void test09()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
      __UnderComp underComp1 = new __UnderComp();
      underComp1.m_price = (-1.0);
      contract0.m_underComp = underComp1;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test10()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
      __UnderComp underComp1 = new __UnderComp();
      contract0.m_underComp = underComp1;
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertTrue(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(1229, "AJ2B", "AJ2B", "AJ2B", 1229, "AJ2B", "AJ2B", "AJ2B", "AJ2B", "AJ2B", vector0, "AJ2B", false, "AJ2B", "AJ2B");
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      vector0.add((Object) contract0);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_secId = "4K~Nc";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secIdType = "BOND";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0, (String) null, (String) null, (String) null, (String) null, "comib.clint.__UnderComp", contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_multiplier = "aa9ST^U;f9Ov6is0q";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_right = "^O6D";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "Yebza5]";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertEquals(0.0, contract1.m_strike, 0.01);
      
      contract1.m_strike = (-883.1404605852);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(0, "BOND", "BOND", "BOND", 0, "BOND", "BOND", "BOND", "BOND", "BOND", vector0, "BOND", true, "BOND", "BOND");
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
      assertTrue(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, "PQtV/LP*]0e", 0.0, (String) null, "vj's;^v", (String) null, "PQtV/LP*]0e", "Yebza5]", contract0.m_comboLegs, (String) null, true, "fSHP,PYc![QYg1]K1_", "W");
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0, (String) null, (String) null, (String) null, (String) null, "Yz(:c^ZW$p=", vector0, "~_ue.vb", false, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, "*", 0, (String) null, "com.ib.client.Contract", "BOND", "|p7)_I^ym", "com.ib.client.__UnderComp", contract0.m_comboLegs, (String) null, false, "PQtV/LP*]0e", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test24()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(0, "com.ib.client.Contract", "com.ib.client.Contract", "com.ib.client.Contract", 0, "com.ib.client.Contract", "com.ib.client.Contract", "", "", "", vector0, "A%i![z &|", true, "", (String) null);
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(723, (String) null, "com.ib.client.Util", "BOND", 0.0, (String) null, "?/} lx", "D", (String) null, "6lW )^3]IVCGkG,C,", contract0.m_comboLegs, (String) null, false, "A|WvYmL1a", "BOND");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(723, contract1.m_conId);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = new Object();
      boolean boolean0 = contract0.equals(object0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertTrue(boolean0);
  }

  @Test
  public void test29()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_symbol = "BOND";
      boolean boolean0 = object0.equals(contract0);
      assertFalse(boolean0);
  }
}
