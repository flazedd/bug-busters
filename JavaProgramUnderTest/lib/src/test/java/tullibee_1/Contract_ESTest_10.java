package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Contract_ESTest_10 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "", (String) null, "com.ib.client.Contract", 0, (String) null, (String) null, "", (String) null, (String) null, contract0.m_comboLegs, (String) null, true, (String) null, "");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract0.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = 2292.197;
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "ni}l;d:d";
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract0.equals((Object)contract1));
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_primaryExch = "$FUgMG";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "", (String) null, "", (-1.0), (String) null, "Ud{Lh@G:7p8y", "-'I1/8", (String) null, "!6(phbIJ{b</PO_Gte", contract0.m_comboLegs, (String) null, false, "", "B[CJ #W#xy%w!Q");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals((-1.0), contract1.m_strike, 0.01);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_symbol = "#&f]#/lv{!JGg";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "-U<YiN", "BOND", "[[26XT5wzO", 0.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, true, (String) null, "d*@ZYrA9we+1A+\"");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test07()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(1, "", "BOND", "~HP+2&e", 3648.2900069, "", (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, ";GMH", false, (String) null, "\".-P2>Kz%';V/");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(1, contract1.m_conId);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertEquals(3648.2900069, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test08()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add((Object) null);
      Contract contract0 = new Contract((-2176), "com.ib.client.__UnderComp", (String) null, "com.ib.client.__UnderComp", (-2176), "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", vector0, (String) null, false, "com.ib.client.__UnderComp", "com.ib.client.__UnderComp");
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
      Contract contract1 = new Contract(0, (String) null, ";LMH", (String) null, 0.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      Contract contract2 = (Contract)contract1.clone();
      assertTrue(contract2.equals((Object)contract1));
      
      __UnderComp underComp0 = new __UnderComp();
      contract2.m_underComp = underComp0;
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      underComp0.m_delta = (-2668.7909577567766);
      boolean boolean0 = contract1.equals(contract2);
      assertFalse(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, ";LMH", (String) null, 0.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      Contract contract2 = (Contract)contract1.clone();
      __UnderComp underComp0 = new __UnderComp();
      contract2.m_underComp = underComp0;
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      boolean boolean0 = contract1.equals(contract2);
      assertEquals(0.0, contract2.m_strike, 0.01);
      assertTrue(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract2.m_conId);
      assertFalse(contract2.equals((Object)contract0));
      assertFalse(contract2.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.equals((Object)contract1));
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, ";LMH", (String) null, 0.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      Object object0 = contract1.clone();
      assertTrue(object0.equals((Object)contract1));
      
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract1.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Vector<Object>> vector0 = new Vector<Vector<Object>>();
      contract0.m_comboLegs = vector0;
      Vector<Object> vector1 = new Vector<Object>();
      vector0.add(vector1);
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_secId = "NS-f]@/DU58<OPS{oi";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract((-226), "$PDD", "$PDD", "$PDD", 1.0, "$PDD", "com.ib.client.Contract", "$PDD", "com.ib.client.Contract", "QrT>:hU>jL/I2", vector0, "e-|0*P!Oir}lKe'z!s", false, "QrT>:hU>jL/I2", "$PDD");
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_secIdType = null;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_multiplier = "Yw]BKt_xOs'B[85AC 1";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_right = "K2Ylz\"f/o$j%paU";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_expiry = "";
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_expiry = "y']>kes5&/mQgYK";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = (-4299.0);
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secType = "BOND";
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertTrue(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, "^JHjS@", (-218.0), (String) null, (String) null, "", "PD", (String) null, contract0.m_comboLegs, (String) null, false, "^JHjS@", "5w'Q,2r=l}z");
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertEquals((-218.0), contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_primaryExch = "C";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_exchange = "F8GrK_C3Q(<PcB3BI_";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "&JX5'd&EVmYke\"?", "", "s", 1.0, "", "ly;x}{i,<&XLr", (String) null, "", "", contract0.m_comboLegs, (String) null, true, "K-@Y.9S_+l", "");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertEquals(0, contract1.m_conId);
      assertEquals(1.0, contract1.m_strike, 0.01);
      assertTrue(contract1.m_includeExpired);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(1, "", "BOND", "~HP+2&e", 3648.2900069, "", (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, ";GMH", true, (String) null, "\".-P2>Kz%';V/");
      boolean boolean0 = contract1.equals(contract0);
      assertTrue(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(1, contract1.m_conId);
      assertEquals(3648.2900069, contract1.m_strike, 0.01);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals("BOND");
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test28()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(1525, "ly;x}{i,<&XLr", "ly;x}{i,<&XLr", "ly;x}{i,<&XLr", (-2274.861106413098), "ly;x}{i,<&XLr", "ly;x}{i,<&XLr", "CTqY@m5/~!3", "", "", vector0, "CTqY@m5/~!3", true, "~", "");
      boolean boolean0 = contract0.equals((Object) null);
      assertTrue(contract0.m_includeExpired);
      assertEquals(1525, contract0.m_conId);
      assertEquals((-2274.861106413098), contract0.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test29()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertTrue(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test30()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, ";LMH", (String) null, 0.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.equals((Object)contract1));
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
  }
}
