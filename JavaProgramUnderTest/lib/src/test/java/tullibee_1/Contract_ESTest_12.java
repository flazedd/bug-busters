package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Contract_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "}spv:+Io";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 526.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, true, "8Y|/NX+LQ3J\u0002", "JN.;0d:huQZe");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(526.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "'d\u0006z";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, "zPPJ.\"s$B:n|4", 0, (String) null, (String) null, (String) null, "BOND", "z^o", contract0.m_comboLegs, "'d\u0006z", true, "aE", "aE");
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, "", "d?FRn#weo =Fq", 0.0, "=L(6Ky 4\u0007", "=L(6Ky 4\u0007", "bXP64.<LyL(cI", (String) null, (String) null, (Vector) null, "p/94*B:", false, (String) null, "`Zn");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "=1A", (String) null, (String) null, 0.0, (String) null, (String) null, (String) null, (String) null, "", contract0.m_comboLegs, (String) null, false, "`<H~QayN7K", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract1 = new Contract(0, (String) null, "z^o", (String) null, 2870.5065111168, "", (String) null, ".=of$i", (String) null, (String) null, vector0, "b)21=7;1@S^", false, "", (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(2870.5065111168, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract((-946), "BOND", "GM0n:n|", "Dl]7VY~`z6", (-1137.9411780732596), "N", "BOND", "`y`b6HMbc", "", "Dl]7VY~`z6", vector0, "", true, "BOND", "");
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertEquals((-1137.9411780732596), contract0.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertEquals((-946), contract0.m_conId);
      assertTrue(contract0.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>(3758, (-1709));
      contract0.m_comboLegs = vector0;
      vector0.add((Object) null);
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
      Contract contract0 = new Contract(0, (String) null, (String) null, (String) null, 0, "com.ib.client.Contract", (String) null, (String) null, (String) null, (String) null, (Vector) null, "}=:pIooj!h8n", false, (String) null, "8Y|/NX+LQ3J\u0002");
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
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_underComp = null;
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      underComp1.m_delta = (-178.5896421);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      contract1.m_underComp = null;
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertTrue(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      boolean boolean0 = object0.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      contract0.m_comboLegs = vector0;
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      Object object1 = new Object();
      vector0.add(object1);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secIdType = "FLQM";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_localSymbol = "'dl6";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_multiplier = "NLQ6";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_right = "o7.=z";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_expiry = "C}QTM";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = 1764.7960160337;
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "BOND";
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertTrue(boolean0);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_currency = "rhgffHqjq##\"G^w%T";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0, "com.ib.client.Contract", (String) null, (String) null, (String) null, (String) null, (Vector) null, "}=:pIooj!h8n", false, (String) null, "8Y|/NX+LQ3J\u0002");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_exchange = "com.ib.client.__UnderComp";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test25()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(0, "^Y", "", "^Y", 0.0, "(h!(i'O:}", "1C(}9", "^Y", "", "^Y", vector0, "", true, "1C(}9", "");
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertTrue(contract0.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, "BOND", "BOND", 0.0, "E'*DkSN$.AEHU!&\"(", "8H$i0<#4|%]Z}mH", "E'*DkSN$.AEHU!&\"(", (String) null, (String) null, contract0.m_comboLegs, "0(.{&[128t ", true, (String) null, "f-i't]<i'4MrB@px.");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertTrue(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test29()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Contract> vector0 = new Vector<Contract>();
      boolean boolean0 = contract0.equals(vector0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test30()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract((-1554), "j=vi.l6XjZ<^x", (String) null, "-qc", 0.0, "Wd", (String) null, "IU2D,c6Pu$VvX/pcz", (String) null, (String) null, contract0.m_comboLegs, "WdV", true, "CZo%]K", "Fw<YP#o");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals((-1554), contract1.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertTrue(contract1.m_includeExpired);
  }
}
