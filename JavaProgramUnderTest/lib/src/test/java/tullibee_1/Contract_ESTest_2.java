package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Contract_ESTest_2 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_expiry = "S_`W`R(L{3rMf7K";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = (-21.17554394531026);
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "BOND";
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract0.equals((Object)contract1));
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract1 = new Contract(0, (String) null, (String) null, "f7Z-w4yb5['}Zi(", 0.0, (String) null, "kG", "com.ib.client.Util", (String) null, "com.ib.client.Util", vector0, "com.ib.client.Util", false, (String) null, "");
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test04()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(0, "?,kG}@N9y= C9@iqHB", (String) null, "", 0.0, (String) null, (String) null, (String) null, "", "", vector0, "KVzznq^dT", true, "com.ib.client.__UnderComp", "?,kG}@N9y= C9@iqHB");
      Contract contract1 = new Contract(0, "FyzDUAgM5:b7`<1", "l)HQwxQ", (String) null, 0.0, "", "{T`UiS", (String) null, "", "0)W>j#3#", contract0.m_comboLegs, "BOND", true, "Z4s`|xoC}ONv", "");
      contract1.m_secType = "";
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "L";
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(contract0.equals((Object)contract1));
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test06()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(0, "?,kG}@N9y= C9@iqHB", (String) null, "", 0.0, (String) null, (String) null, (String) null, "", "", vector0, "KVzznq^dT", true, "com.ib.client.__UnderComp", "?,kG}@N9y= C9@iqHB");
      Contract contract1 = new Contract((-483), "", "zMVS8XuDNI", "", 0.0, "upSKot!9aroaSx", "", "i??J4}\"UoVK:(W}+M@", "", (String) null, contract0.m_comboLegs, "", true, "", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals((-483), contract1.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      vector0.setSize(2492);
      Contract contract0 = new Contract(2492, "}:\"mH-$#Hte", "com.ib.client.Util", "com.ib.client.Util", 2492, "}:\"mH-$#Hte", "}:\"mH-$#Hte", "}:\"mH-$#Hte", "}:\"mH-$#Hte", "com.ib.client.Util", vector0, "}:\"mH-$#Hte", true, "}:\"mH-$#Hte", "}:\"mH-$#Hte");
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
      underComp0.m_delta = (-1385.14154);
      __UnderComp underComp1 = new __UnderComp();
      contract0.m_underComp = underComp1;
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test10()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      __UnderComp underComp1 = new __UnderComp();
      contract0.m_underComp = underComp1;
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0, contract1.m_conId);
      assertTrue(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      contract0.m_comboLegs = vector0;
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      vector0.add(object0);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_secId = "KT#k";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_secIdType = "";
      contract0.m_secIdType = "BOND";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_localSymbol = "com.ib.client.Contract";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_multiplier = "ove";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_right = "ncnh9p";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "X_FYE *=Ni^{Z@e*";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = 451.105899430782;
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "BOND";
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(contract1.m_includeExpired);
      assertTrue(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_currency = "AgXSi";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, "", (String) null, 0, (String) null, (String) null, ":qD[?dr1z=2 ?", "com.ib.client.Contract", (String) null, contract0.m_comboLegs, (String) null, true, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_symbol = "AgqSi";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "MHM?";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.equals((Object)contract0));
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(520, (String) null, (String) null, (String) null, 0.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(520, contract1.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      boolean boolean0 = contract0.equals(vector0);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertTrue(boolean0);
  }

  @Test
  public void test29()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0.0, (String) null, "%^", (String) null, "AgXSi", "com.ib.client.Contract", contract0.m_comboLegs, "com.ib.client.Contract", false, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
  }
}
