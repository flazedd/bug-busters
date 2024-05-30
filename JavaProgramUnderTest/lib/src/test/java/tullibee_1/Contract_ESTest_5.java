package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Contract_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "q[a";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertEquals(0.0, contract1.m_strike, 0.01);
      
      contract1.m_strike = (-1.0);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_currency = "z*=Py$iVyip6P";
      boolean boolean0 = object0.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_primaryExch = "";
      contract0.m_primaryExch = "Fq]mjLBKtse04D";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_exchange = "rVUP'!@FA,n]3!;";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_symbol = "\"2|HVkt|ae!(TX9@M~r";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_secType = "%n";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(1, "com.ib.client.Contract", "", "", 0.0, "BOND", (String) null, "", "Ei&}OIrbGs6ip+Qx^Q", "", contract0.m_comboLegs, "wLS [[^lH%} 1S ", true, "", (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(1, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test08()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      vector0.setSize(1274);
      Contract contract0 = new Contract(1274, (String) null, (String) null, (String) null, 1274, (String) null, (String) null, (String) null, (String) null, (String) null, vector0, (String) null, true, (String) null, (String) null);
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
  public void test09()  throws Throwable  {
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
  public void test10()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      contract0.m_underComp = underComp0;
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      __UnderComp underComp1 = new __UnderComp();
      underComp1.m_price = 109.754438297;
      contract0.m_underComp = underComp1;
      boolean boolean0 = object0.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_underComp = contract0.m_underComp;
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      contract0.m_underComp = underComp0;
      Contract contract1 = (Contract)contract0.clone();
      __UnderComp underComp1 = new __UnderComp();
      contract0.m_underComp = underComp1;
      boolean boolean0 = contract1.equals(contract0);
      assertTrue(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_underComp = contract0.m_underComp;
      contract0.m_underComp = contract0.m_underComp;
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      boolean boolean0 = object0.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(Integer.MAX_VALUE, (String) null, (String) null, (String) null, Integer.MAX_VALUE, (String) null, (String) null, (String) null, (String) null, (String) null, vector0, (String) null, true, (String) null, (String) null);
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      vector0.add((Contract) object0);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_secId = "nSxzx3'5Pb~";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secIdType = "[ROK";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_localSymbol = "[rvB%5$A&>|n7-?";
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_multiplier = "BOND";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_right = "n^";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_expiry = "com.ib.client.Util";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = (-1.0);
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(2147483637, (String) null, "BOND", (String) null, 2147483637, (String) null, (String) null, (String) null, (String) null, "BOND", vector0, (String) null, true, (String) null, (String) null);
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(boolean0);
      assertEquals(2147483637, contract1.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertEquals(2.147483637E9, contract1.m_strike, 0.01);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "t";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "", (String) null, "com.ib.client.__UnderComp", 0, "BOND", (String) null, "", "UMrVyZ", (String) null, contract0.m_comboLegs, "BOND", true, "-)*9+E", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0, contract0.m_conId);
      
      contract0.m_conId = (-1);
      Contract contract1 = new Contract((-1), "erX8e|mT/a)tT~S", "9xTZ(.kKVc}@}7", "com.ib.client.__UnderComp", (-1), "<$[&d", (String) null, "+X6f6c7Uk&dB]CWW", (String) null, "G=Y/Y]o5cF", contract0.m_comboLegs, "", true, (String) null, "com.ib.client.__UnderComp");
      contract0.m_secType = "9xTZ(.kKVc}@}7";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract1 = new Contract(0, ")$W. ,%gh$V", "NWPkwT Vm3wR1r`(Q", (String) null, 0.0, (String) null, "z@h5{", (String) null, "^q#b~3]<n'kALd8", "(pOs,3%W3Q/Wc|fL", vector0, (String) null, false, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(1, "com.ib.client.Contract", "", "", 0.0, "BOND", (String) null, "", "Ei&}OIrbGs6ip+Qx^Q", "", contract0.m_comboLegs, "wLS [[^lH%} 1S ", true, "", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(1, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Contract> vector0 = new Vector<Contract>();
      boolean boolean0 = contract0.equals(vector0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
  }

  @Test
  public void test29()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test30()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertTrue(boolean0);
  }

  @Test
  public void test31()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_exchange = "";
      contract0.m_exchange = "BOND";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }
}
