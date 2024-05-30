package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Contract_ESTest_6 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0, contract0.m_conId);
      
      contract0.m_strike = (-1.0);
      contract0.m_conId = (-1);
      Contract contract1 = new Contract((-1), (String) null, (String) null, "a0}~:", (-1), "", "a0}~:", "", (String) null, "", contract0.m_comboLegs, "", false, "~)TL$kN%M", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertEquals(0.0, contract1.m_strike, 0.01);
      
      contract1.m_strike = 975.63635;
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "com.ib.client.__UnderComp";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_primaryExch = "@LPE";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "}<{TooCy", (String) null, (String) null, 520.40944, "BOND", (String) null, "'pr", "", "", contract0.m_comboLegs, "", false, "", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(520.40944, contract1.m_strike, 0.01);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "!";
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(contract0.equals((Object)contract1));
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(610, (String) null, "", (String) null, 0, "BOND", (String) null, "BOND", (String) null, (String) null, contract0.m_comboLegs, "{", false, (String) null, "[$W)Qy-;^5sd~9");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(610, contract1.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add((Object) null);
      Contract contract0 = new Contract((-1), "MP", "MP", "MP", (-1), "MP", "MP", "MP", (String) null, (String) null, vector0, ".f", true, (String) null, "MP");
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
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      underComp1.m_price = 3698.0;
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test10()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = (Contract)contract0.clone();
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      boolean boolean0 = contract1.equals(contract0);
      assertTrue(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
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
      
      vector0.add((Object) contract0);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_secIdType = "]q5{K|hC-D>f(G(9";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_multiplier = "BOND";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_right = "KX ww";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_expiry = "0U )Y";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertEquals(0.0, contract1.m_strike, 0.01);
      
      contract1.m_strike = 936.918107442912;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "BOND";
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertTrue(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_currency = "hd&@F*}pkA7";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_primaryExch = "com.ib.client.Contract";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_exchange = "KXww";
      boolean boolean0 = object0.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "kXynKElCn4Y7", (String) null, (String) null, 1.0, "0U )Y", (String) null, "BOND", (String) null, "com.ib.client.__UnderComp", contract0.m_comboLegs, (String) null, true, "0U )Y", "BOND");
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(1.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_secType = "KXww";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(91, "yP*=n$]1iR5YIoKJ", "yP*=n$]1iR5YIoKJ", "I7aPn5Kz*0+b", (-878.8177774828196), "}1L-8n!BC", (String) null, "kJS2)=]", "cJcG!xw:F", "}1L-8n!BC", vector0, "),#]+3P8", false, "%", "}1L-8n!BC");
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(91, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals((-878.8177774828196), contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract0.m_underComp);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertTrue(boolean0);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
  }
}
