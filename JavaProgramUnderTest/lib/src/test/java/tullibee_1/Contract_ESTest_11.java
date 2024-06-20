package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Vector;
public class Contract_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_expiry = "BOND";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract((-481), "fL3n3atIYeyLjxf%q", "fL3n3atIYeyLjxf%q", "fL3n3atIYeyLjxf%q", 2525.56401839275, "fL3n3atIYeyLjxf%q", "fL3n3atIYeyLjxf%q", "", "fL3n3atIYeyLjxf%q", "", vector0, "", true, "com.ib.client.__UnderComp", "fL3n3atIYeyLjxf%q");
      Contract contract1 = (Contract)contract0.clone();
      assertEquals(2525.56401839275, contract1.m_strike, 0.01);
      
      contract1.m_strike = 1.0;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "RkR";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "o:5&yd:O.w%6", (String) null, "BcW1w{6Ur", (-1.0), "", "~Z iR:@|sdk@E!", "", "", "~Z iR:@|sdk@E!", contract0.m_comboLegs, "com.ib.client.Contract", false, "I.GE", "com.ib.client.__UnderComp");
      contract1.m_symbol = null;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals((-1.0), contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 0, "7Ew'6d", (String) null, "lP", "GQv{", "~}_-[c=e/[a\"oL", contract0.m_comboLegs, "com.ib.client.Util", true, (String) null, (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertTrue(contract1.m_includeExpired);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_symbol = "(s4#6-L}Rfy!3vt0";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, "|-qh9`y/@YQht*FWW&", "BOND", 733.43977992, "", "O7dk>kq9vp>QVgAEn{K", "{z#b3HUkY!8z8", "", "BOND", contract0.m_comboLegs, "", false, "wwcx/;MkA5O]V3zm", "com.ib.client.__UnderComp");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertEquals(733.43977992, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(53, "", "", "", 53, "", "BL/:;Zv", "BOND", "BOND", "", vector0, "", false, "", "");
      Contract contract1 = new Contract(0, "Z4_Mx(v;DZv-5", "", "Z4_Mx(v;DZv-5", 0.0, "ESO", "", "BOND", "", "", contract0.m_comboLegs, "", false, "3sit,Usz-<_n6", "");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(53, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test08()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Vector<Object>> vector0 = new Vector<Vector<Object>>();
      vector0.add((Vector<Object>) null);
      contract0.m_comboLegs = vector0;
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
      underComp0.m_delta = 601.5846943502;
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      assertFalse(contract1.equals((Object)contract0));
      
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      boolean boolean0 = contract1.equals(contract0);
      assertTrue(contract1.equals((Object)contract0));
      assertTrue(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Contract contract0 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      contract0.m_underComp = underComp0;
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      Vector<Object> vector0 = new Vector<Object>();
      contract0.m_comboLegs = vector0;
      vector0.add((Object) contract0);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_secId = "FiRk_<en~Uk6L";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secIdType = "fL3n3atIYeyLjxf%q";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_localSymbol = "'uA:V-@F^/-";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_multiplier = "Cd'm";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_right = "k45zZ7=mQ}";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertTrue(boolean0);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test21()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = (-481.0);
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(0, (String) null, "BOND", (String) null, 0, "lD", (String) null, (String) null, "lD", "lD", vector0, "BOND", false, "lD", (String) null);
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertTrue(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_currency = "q#ghP1ryZ=";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 1.0, (String) null, (String) null, "ZV", (String) null, (String) null, contract0.m_comboLegs, (String) null, false, "", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(1.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_symbol = "4eV";
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(boolean0);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, "ob[l", (String) null, (-3727.670772076), "A", "isqpqc|uii2N}[+2JQ", (String) null, (String) null, (String) null, contract0.m_comboLegs, "com.ib.client.Underomp", false, "lP", (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(contract1.m_includeExpired);
      assertEquals((-3727.670772076), contract1.m_strike, 0.01);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(682, "7J<$@", (String) null, "ob[l", 0, "[Mt-<", (String) null, "com.ib.client.Contract", "", (String) null, contract0.m_comboLegs, (String) null, true, "':lNPt`e_", "fL3n3atIYeyLjxf%q");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(682, contract1.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = new Object();
      boolean boolean0 = contract0.equals(object0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
  }

  @Test
  public void test29()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test30()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals(contract0);
      assertFalse(contract0.m_includeExpired);
      assertTrue(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test31()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, "ltXD2[{bw8)k@tX", 0.0, (String) null, (String) null, (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, "ltXD2[{bw8)k@tX", "ltXD2[{bw8)k@tX");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test32()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_primaryExch = "Z~bmt/z:bSe(yv8!]";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }
}
