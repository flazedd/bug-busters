package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Contract_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(1, "", "3h", "", 0.0, "", ";", "", (String) null, "`F", vector0, "", false, "BOND", "BOND");
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "`F";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(0, "", "", "", (-2191.230201), "$l$OTJO);+&4Z-]", "$l$OTJO);+&4Z-]", "", "", (String) null, vector0, "", false, "", "");
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals((-2191.230201), contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test02()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(1, "", "3h", "", 0.0, "", ";", "", (String) null, "`F", vector0, "", false, "BOND", "BOND");
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_currency = "BfN3EM";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract();
      contract0.m_primaryExch = "`?3E?u#gPl*7";
      vector0.add(contract0);
      Contract contract1 = new Contract();
      boolean boolean0 = vector0.remove((Object) contract1);
      assertEquals(1, vector0.size());
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_exchange = "WBv~N*|B,";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test05()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Contract> vector1 = new Vector<Contract>();
      Contract contract0 = new Contract(0, "", "", "", (-2191.230201), "$l$OTJO);+&4Z-]", "$l$OTJO);+&4Z-]", "", "", (String) null, vector0, "", false, "", "");
      Contract contract1 = new Contract(0, "QK-L[uVN28S", "", (String) null, 1.0, "$l$OTJO);+&4Z-]", "", "", "", (String) null, vector1, "$l$OTJO);+&4Z-]", false, "", "");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(1.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test06()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(0, "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", 0, "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", "com.ib.client.__UnderComp", vector0, "com.ib.client.__UnderComp", true, "", "BOND");
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract((-1), "", "", "", 0.0, "tRV7Bts*O]94) <_O|", "", "", (String) null, (String) null, vector0, "BOND", false, (String) null, "");
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals((-1), contract0.m_conId);
  }

  @Test
  public void test08()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add((Object) null);
      Contract contract0 = new Contract(67, (String) null, (String) null, (String) null, 483.28780987039, (String) null, (String) null, "#Zk&WmG", (String) null, (String) null, vector0, (String) null, false, "com.ib.client.Contract", (String) null);
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
      boolean boolean0 = contract0.equals(contract0);
      assertTrue(boolean0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      contract0.m_underComp = underComp0;
      underComp1.m_conId = (-225);
      Contract contract2 = (Contract)contract1.clone();
      boolean boolean0 = contract0.equals(contract2);
      assertFalse(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      __UnderComp underComp0 = new __UnderComp();
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertTrue(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
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
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
      Object object0 = contract1.clone();
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Contract> vector0 = new Vector<Contract>();
      contract0.m_comboLegs = vector0;
      vector0.add(contract0);
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secId = "d";
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
      contract0.m_secIdType = "%'GjW+";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_localSymbol = "i= \"k9NR";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test19()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(1, "", "3h", "", 0.0, "", ";", "3h", (String) null, "`F", vector0, "3h", false, (String) null, (String) null);
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_multiplier = "qbM5)v[q<{^]|1*5";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0.0, "BOND", (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, "BOND");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_expiry = "rQ&pK:pC<*5F";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.equals((Object)contract0));
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = 23.0;
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(18, (String) null, "BOND", "BOND", 0.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, (String) null);
      Contract contract2 = (Contract)contract1.clone();
      boolean boolean0 = contract1.equals(contract2);
      assertEquals(18, contract2.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertTrue(boolean0);
      assertFalse(contract2.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract2.m_strike, 0.01);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract2.equals((Object)contract0));
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_primaryExch = "Z[/WF&7C%'OtR{";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.equals((Object)contract0));
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, (-671.5491435341986), "", (String) null, "6j|dbKUDz.N_9i", "\"BvZoeIKN?&[M4", "com.ib.client.Contract", contract0.m_comboLegs, "Vq$i`!f}O", false, "BOND", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertEquals((-671.5491435341986), contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_symbol = "40g7ZZu9f";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract1 = new Contract(0, (String) null, "p[N", "5c #a", 0.0, "com.ib.client.__UnderComp", (String) null, "J_H`Q", "d,f:B9Go)rN,\\", (String) null, vector0, (String) null, false, "%JjO\"I-r60", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals("VdVu");
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test29()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(1, "", "3h", "", 0.0, "", ";", "3h", (String) null, "`F", vector0, "3h", false, (String) null, (String) null);
      boolean boolean0 = contract0.equals((Object) null);
      assertEquals(1, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test30()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract1 = new Contract(67, (String) null, (String) null, (String) null, 483.28780987039, (String) null, (String) null, "#Zk&WmG", (String) null, (String) null, vector0, (String) null, false, "com.ib.client.Contract", (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(67, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertFalse(contract0.m_includeExpired);
      assertEquals(483.28780987039, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test31()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_currency = "VdVu";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }
}
