package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Contract_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "0?-;BD^>qi]lVzm5>K";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = 3211.338;
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, "", (String) null, 0.0, (String) null, (String) null, (String) null, "BOND", "", contract0.m_comboLegs, (String) null, false, "/pf#", "8=CeSxlkKGV");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0, "?MKwzY0lRY|>#ZdFz", ")EN,zMc&u')", "com.ib.client.Util", "BOND", "com.[b.client.__UnderComp", contract0.m_comboLegs, (String) null, true, "com.ib.client.Util", (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract((-3787), (String) null, (String) null, (String) null, (-3787), "BOND", "0t'xWa", "=?", (String) null, "bEi_*{;@O{B=[s[V/HQ", contract0.m_comboLegs, "tc/F7", false, "]P]QHKV{O7X", (String) null);
      Contract contract2 = new Contract((-3787), "bEi_*{;@O{B=[s[V/HQ", (String) null, "com.ib.client.__UnderComp", 1097.39653724195, "LwLY<=42F$*As", "]P]QHKV{O7X", "=?", "", "|TO}G~,:3TsuFyE2rj", contract0.m_comboLegs, "BOND", false, (String) null, "Kns*]1$/c-(@^");
      boolean boolean0 = contract1.equals(contract2);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals((-3787), contract2.m_conId);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(1097.39653724195, contract2.m_strike, 0.01);
      assertFalse(contract2.m_includeExpired);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "com.ib.client.__UnderComp";
      Contract contract1 = new Contract(0, (String) null, "Oe8b[>", (String) null, 0.0, "YV", "BOND", "AC34N", (String) null, "com.ib.client.__UnderComp", contract0.m_comboLegs, "mq,nHQ| e*O)", true, (String) null, (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(contract0.m_includeExpired);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0, contract0.m_conId);
      
      contract0.m_conId = 176;
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add((Object) null);
      Contract contract0 = new Contract((-9), "IVJG", "IVJG", "IVJG", (-9), "IVJG", "IVJG", "IVJG", "IVJG", "IVJG", vector0, "IVJG", true, "IVJG", "IVJG");
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
      Contract contract1 = new Contract();
      underComp0.m_conId = (-17);
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test10()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      assertFalse(contract1.equals((Object)contract0));
      
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(contract1.equals((Object)contract0));
      assertTrue(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_underComp = null;
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test13()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract((-6), "3+;4/0P)5-", "3+;4/0P)5-", "3+;4/0P)5-", (-6), "3+;4/0P)5-", "3+;4/0P)5-", "3+;4/0P)5-", "3+;4/0P)5-", "3+;4/0P)5-", vector0, "3+;4/0P)5-", true, "3+;4/0P)5-", "3+;4/0P)5-");
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      vector0.add(object0);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_secIdType = "o?j56)v4=Odl]4~Z";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_localSymbol = "com.ib.client.Util";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_multiplier = "Q&Sk5J;";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_right = "BOND";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_expiry = "482DSgZj";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = (-1015.4487601);
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
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "IOr&jt~|d$,\"8";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.equals((Object)contract0));
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_primaryExch = "BOCkkKUz^I%7i";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0, (String) null, (String) null, "?MKwzY0lRY|>#ZdFz", (String) null, "BOND", contract0.m_comboLegs, "BOND", true, "f?o{", "BOND");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "=?";
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0, "?MKwzY0lRY|>#ZdFz", ")EN,zMc&u')", "com.ib.client.Util", "BOND", "com.[b.client.__UnderComp", contract0.m_comboLegs, (String) null, true, "com.ib.client.Util", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract((-1975), "com.ib.client.Contract", "", (String) null, 0.0, (String) null, "Vc,", "", (String) null, "BOND", contract0.m_comboLegs, "-r`l-", false, "", "*kv*\u0002:of[1a0$bl");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertEquals((-1975), contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract0.m_underComp);
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
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test28()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(2581, "", "vrxb7", "Vl]_<Dga", 2581, "BOND", "BOND", "", ")rp+Z", ")rp+Z", vector0, "", false, "com.ib.client.__UnderComp", ")rp+Z");
      boolean boolean0 = contract0.equals(contract0);
      assertTrue(boolean0);
      assertEquals(2581.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(2581, contract0.m_conId);
  }

  @Test
  public void test29()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_symbol = "com.ib.client.__UnderComp";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }
}
