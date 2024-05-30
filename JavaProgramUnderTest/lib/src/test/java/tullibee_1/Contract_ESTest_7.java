package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Contract_ESTest_7 {

  @Test
  public void test00()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract((-1883), (String) null, "ai,xi", "", (-1883), "ai,xi", "ai,xi", "", "", "XL4jO", vector0, "ai,xi", true, "com.ib.client.__UnderComp", "");
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "XL4jO";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = 2240.7787144485865;
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "Vr6_n),H6@l=? )<i";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0.0, "", (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, "/-R8|z|Pkj", false, "com.ib.client.Contract", "ftTtNy>Z_3of");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test04()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(0, (String) null, (String) null, "", (-2177.89388479), "", " 6%D%5ov_++SAB", "|,Q9m{vW)wo:JH", "u;45*P.u:!aR 1Ur", (String) null, vector0, (String) null, true, "", "");
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals((-2177.89388479), contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertTrue(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_secType = "{v#*J8/`6K%>RIl2E";
      boolean boolean0 = object0.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(1332, (String) null, (String) null, (String) null, 1332, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(1332.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(1332, contract1.m_conId);
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add((Object) null);
      Contract contract0 = new Contract((-1883), (String) null, "BOND", "", (-1883), "BOND", "BOND", "", "", "XL4jO", vector0, ")+]K4.4B\"6:Q", true, "com.ib.client.__UnderComp", "");
      Object object0 = contract0.clone();
      // Undeclared exception!
      try { 
        object0.equals(contract0);
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
      underComp0.m_price = 1411.79095218;
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
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
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add((Object) contract0);
      contract0.m_comboLegs = vector0;
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secId = "BOND";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_secIdType = "6ai,3Voi";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_localSymbol = "*9u-y:*W{E>)L3'";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_multiplier = "aiZD";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_right = "ysx^mpH";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract((-1883), (String) null, "ai,xi", "ai,xi", (-1883), "ai,xi", "ai,xi", "ai,xi", "ai,xi", "XL4jO", vector0, ")+]K4.4B\"6:Q", true, "com.ib.client.__UnderComp", "");
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "2v:-_gB&szIZ6f";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 322.0, ")i,Sxi", "n(Q%87ry=s", (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract0.m_conId);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(322.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>(0);
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0.0, (String) null, "=hli{", (String) null, "BOND", (String) null, vector0, (String) null, false, (String) null, "com.ib.client.Util");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_primaryExch = "com.ib.client.Util";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_exchange = "&Y_v,6z";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "YhFc}*Ftf";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract1 = new Contract((-3332), (String) null, ".;rn=&wQ$-!JvPGL", "com.ib.client.Contract", 1874.4347881707, "", (String) null, "", "hkslL7~*e&,&iM", ".;rn=&wQ$-!JvPGL", vector0, (String) null, true, ".;rn=&wQ$-!JvPGL", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals((-3332), contract1.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(1874.4347881707, contract1.m_strike, 0.01);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(")i,Sxi");
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertTrue(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test29()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test30()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_symbol = "b";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }
}
