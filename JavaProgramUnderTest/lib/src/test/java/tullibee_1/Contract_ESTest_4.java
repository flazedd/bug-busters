package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Vector;

public class Contract_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_expiry = "4";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test01()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0.0, contract0.m_strike, 0.01);
      
      contract0.m_strike = (-5157.7505);
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_currency = "YV(*qP8sM']L,p";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.equals((Object)contract0));
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0, contract0.m_conId);
      
      contract0.m_conId = 1428;
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract1 = new Contract(1428, "", "", "tpT^YZMYEX*|", 0.0, "", (String) null, "", "", "wFwhb\"w", vector0, "tpT^YZMYEX*|", false, (String) null, "");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, "", (String) null, 3595.90212035, (String) null, "b:0RR:Ei%!", "hIes7WjUiivD7Usg", (String) null, (String) null, contract0.m_comboLegs, (String) null, false, (String) null, "'l \"eTCzm6");
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(contract0.m_includeExpired);
      assertEquals(3595.90212035, contract1.m_strike, 0.01);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "com.ib.client.Contract", (String) null, (String) null, 0.0, (String) null, "}'#zZKx`8<Y*M7N}|P", (String) null, "5Zn!1", (String) null, contract0.m_comboLegs, (String) null, false, "nd)GOoq?q9|}7mnv", "mDx8");
      boolean boolean0 = contract1.equals(contract0);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
  }

  @Test
  public void test06()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract1 = new Contract(0, "", "-c xx-I V*vrci6gt", "-c xx-I V*vrci6gt", (-5157.7505), "", (String) null, "UY,GQ23A5|f*DMc", "", "Wo", vector0, (String) null, true, "Wo", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertTrue(contract1.m_includeExpired);
      assertEquals((-5157.7505), contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test07()  throws Throwable  {
      Contract contract0 = new Contract();
      assertEquals(0, contract0.m_conId);
      
      contract0.m_conId = (-761);
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(22, "BONF", "BONF", "BONF", 22, "BONF", "BONF", "BONF", "BONF", "BONF", vector0, "BONF", true, "BONF", "BONF");
      vector0.setSize(22);
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
      Contract contract0 = new Contract(0, (String) null, "(anDxW\"", (String) null, 0.0, "\".7/", "P", "(anDxW\"", "\".7/", "(anDxW\"", (Vector) null, "P", false, "\".7/", "a )!zH^4iz1:");
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
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      __UnderComp underComp1 = new __UnderComp();
      underComp0.m_conId = Integer.MAX_VALUE;
      contract1.m_underComp = underComp1;
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      __UnderComp underComp0 = new __UnderComp();
      __UnderComp underComp1 = new __UnderComp();
      contract1.m_underComp = underComp1;
      contract0.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertTrue(boolean0);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test12()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      __UnderComp underComp0 = new __UnderComp();
      contract1.m_underComp = underComp0;
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(0, "BONF", "BONF", "BONF", 0, "BONF", "BONF", "BONF", "BONF", "BONF", vector0, "BONF", false, "BONF", "BONF");
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      vector0.add((Object) "BONF");
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secId = "com.ib.client.__UnderComp";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
  }

  @Test
  public void test15()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_secIdType = "*K3/O)P";
      Contract contract1 = new Contract();
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(boolean0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test16()  throws Throwable  {
      Contract contract0 = new Contract();
      contract0.m_localSymbol = "}_QSG^x,uyc_,LUMi";
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_localSymbol = "";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_multiplier = "(;An;";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_right = "9FN@IEp2z4?";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_expiry = "AwQgWk";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract();
      assertEquals(0.0, contract1.m_strike, 0.01);
      
      contract1.m_strike = (-59.5769493);
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract0 = new Contract(553, "BOND", "BOND", "BOND", 553, "BOND", "BOND", "BOND", "BOND", "BOND", vector0, "BOND", false, "BOND", "BOND");
      Contract contract1 = (Contract)contract0.clone();
      boolean boolean0 = contract0.equals(contract1);
      assertTrue(boolean0);
      assertEquals(553, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(553.0, contract1.m_strike, 0.01);
  }

  @Test
  public void test22()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, (String) null, (String) null, (String) null, 1689.73, (String) null, "wv>=AfuB9wU", (String) null, "9FN@IEp2z4?", (String) null, contract0.m_comboLegs, (String) null, false, (String) null, "wv>=AfuB9wU");
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract1.m_conId);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(1689.73, contract1.m_strike, 0.01);
  }

  @Test
  public void test23()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = contract0.clone();
      assertTrue(object0.equals((Object)contract0));
      
      contract0.m_primaryExch = "0Si&K$ap";
      boolean boolean0 = contract0.equals(object0);
      assertFalse(object0.equals((Object)contract0));
      assertFalse(boolean0);
  }

  @Test
  public void test24()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract(0, "(c{7(", (String) null, (String) null, 0, (String) null, "(c{7(", (String) null, (String) null, (String) null, contract0.m_comboLegs, (String) null, false, "bqc^rlqA=y3@2)", (String) null);
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertEquals(0, contract1.m_conId);
      assertFalse(boolean0);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test25()  throws Throwable  {
      Contract contract0 = new Contract();
      Vector<Object> vector0 = new Vector<Object>();
      Contract contract1 = new Contract(0, "com.ib.client.__UnderComp", "T", "", (-4850.274), "!p6P`?[Zms:l8(ey?", "C;)PD\"O90Ho", (String) null, (String) null, "", vector0, (String) null, false, "BOND", (String) null);
      boolean boolean0 = contract1.equals(contract0);
      assertEquals(0, contract1.m_conId);
      assertFalse(contract1.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0, contract0.m_conId);
      assertFalse(boolean0);
      assertEquals((-4850.274), contract1.m_strike, 0.01);
  }

  @Test
  public void test26()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = new Contract((-1838), "lOgq", "[SzHaI43@m>-+*Jn", "lOgq", 0.0, "BOND", "(oB>#v0BEO9F$iK", "lOgq", "|x9k-xt$}`<rj}_\"YL", "ItVq}~)do&X|oib@-", contract0.m_comboLegs, (String) null, false, "BOND", "lOgq");
      boolean boolean0 = contract0.equals(contract1);
      assertEquals(0.0, contract1.m_strike, 0.01);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals((-1838), contract1.m_conId);
      assertFalse(boolean0);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract1.m_includeExpired);
  }

  @Test
  public void test27()  throws Throwable  {
      Contract contract0 = new Contract();
      Object object0 = new Object();
      boolean boolean0 = contract0.equals(object0);
      assertEquals(0, contract0.m_conId);
      assertFalse(contract0.m_includeExpired);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(boolean0);
  }

  @Test
  public void test28()  throws Throwable  {
      Contract contract0 = new Contract();
      boolean boolean0 = contract0.equals((Object) null);
      assertEquals(0.0, contract0.m_strike, 0.01);
      assertFalse(contract0.m_includeExpired);
      assertFalse(boolean0);
      assertEquals(0, contract0.m_conId);
  }

  @Test
  public void test29()  throws Throwable  {
      Vector<Contract> vector0 = new Vector<Contract>();
      Contract contract0 = new Contract(1461, ".|S3", ".|S3", ".|S3", 1962.48393382207, ".|S3", ".|S3", "V8#sTT<W?~:AU[T8V-", ".|S3", ".|S3", vector0, "V8#sTT<W?~:AU[T8V-", false, "V8#sTT<W?~:AU[T8V-", ".|S3");
      boolean boolean0 = contract0.equals(contract0);
      assertEquals(1962.48393382207, contract0.m_strike, 0.01);
      assertEquals(1461, contract0.m_conId);
      assertTrue(boolean0);
      assertFalse(contract0.m_includeExpired);
  }

  @Test
  public void test30()  throws Throwable  {
      Contract contract0 = new Contract();
      Contract contract1 = (Contract)contract0.clone();
      assertTrue(contract1.equals((Object)contract0));
      
      contract1.m_exchange = "d:G{Q''[nhU";
      boolean boolean0 = contract0.equals(contract1);
      assertFalse(contract1.equals((Object)contract0));
      assertFalse(boolean0);
  }
}
