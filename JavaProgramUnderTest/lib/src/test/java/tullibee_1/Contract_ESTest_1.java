package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Contract_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = 1853.104411;
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_currency = ":2";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, "", 0.0, "com.ib.client.Contract", (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, "com.ib.client.Contract", true, (String) null, "x6\"");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, "", (String) null, 1.0, "\"m:+A", (String) null, "UhKg=cG-R?", (String) null, "c:z,", contract0.m_comboLegs, "com.ib.client.Util", true, "i|cb}2?xFlU8", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(1.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0, contract0.m_conId);
      
      contract0.m_secType = "m`QiOa4aW|2kP*";
      contract0.m_conId = (-4133);
      Contract contract1 = new Contract((-4133), "8%(( kSQ|W<c)*1V", "KKH /|)m[?Q(FQn0", "yCQrIxN#npwrOC", (-4133), "m`QiOa4aW|2kP*", "yCQrIxN#npwrOC", "\"D!", (String) null, (String) null, contract0.m_comboLegs, "m`QiOa4aW|2kP*", false, "yCQrIxN#npwrOC", (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0, contract0.m_conId);
      
      contract0.m_conId = Integer.MAX_VALUE;
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Contract> vector0 = new Vector<Contract>();
      contract0.m_comboLegs = vector0;
      vector0.add((Contract) null);
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
  public void test07()  throws Throwable  {
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
  public void test08()  throws Throwable  {
      __UnderComp underComp0 = new __UnderComp();
      Contract contract0 = new Contract();
      __UnderComp underComp1 = new __UnderComp();
      contract0.m_underComp = underComp1;
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      underComp0.m_price = (-3094.280393605728);
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test09()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test10()  throws Throwable  {
      __UnderComp underComp0 = new __UnderComp();
      Contract contract0 = new Contract();
      __UnderComp underComp1 = new __UnderComp();
      contract0.m_underComp = underComp1;
      Contract contract1 = (Contract)contract0.clone();
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test11()  throws Throwable  {
      __UnderComp underComp0 = new __UnderComp();
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add(object0);
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_comboLegs = vector0;
      Object object1 = contract0.clone();
      boolean boolean0 = object0.equals(object1);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secIdType = ">PQA";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_localSymbol = "bEy=v";
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_multiplier = "x!x8%W";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_right = ">0PQA";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "BOND";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = (-1315.0);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "BOND";
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertTrue(boolean0);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_currency = ":2";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_primaryExch = "com.ib.client.__UnderComp";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_exchange = "BOND";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_symbol = "-?hfTO;;T4b>n";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "$qk";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract1.equals((Object)contract0));
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(4, "X7CO:]6", (String) null, (String) null, (-2584.068352692716), (String) null, "jS,PmQrzat5", "N-)O(t,r]zdp#Rl-", (String) null, (String) null, contract0.m_comboLegs, (String) null, true, (String) null, "BOND");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(4, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals((-2584.068352692716), contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test26()  throws Throwable  {
      __UnderComp underComp0 = new __UnderComp();
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(underComp0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertTrue(boolean0);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
  }
}
