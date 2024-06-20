package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "F ");
      bcWord0.getWord();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test01()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "4<P@Al5f+Q6|");
      bcWord0.getWord();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test02()  throws Throwable  {
      bcWord bcWord0 = new bcWord("0-3fgo0vboqp+B", "<up");
      int int0 = bcWord0.getSyllables();
      assertEquals(0, int0);
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.setEqualWord("J[k|.y|&!>)", "");
      bcWord0.getRhymeKey(true);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "c':SI>f3GPCtn>");
      bcWord0.setEqualWord((String) null, (String) null);
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      String string0 = bcWord0.getMetricCode();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.setEqualWord("U.a}0", (String) null);
      // Undeclared exception!
      try { 
        bcWord0.getRhymeKey(false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("bcry.bcWord", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
      bcWord bcWord0 = new bcWord("s>vD2MI'.fbpDkto", "s>vD2MI'.fbpDkto");
      // Undeclared exception!
      try { 
        bcWord0.equalTo((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("bcry.bcWord", e);
      }
  }

  @Test
  public void test09()  throws Throwable  {
      bcWord bcWord0 = null;
      try {
        bcWord0 = new bcWord((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("bcry.bcWord", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      bcWord bcWord0 = new bcWord("Z", "qU+N3j^L3/}U~,2Ik/");
      bcWord0.setEqualWord("qU+N3j^L3/}U~,2Ik/", "C7g* 0IVZqk6W");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("0IVZqk6W", string0);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("v@+eNs'Nmu)^asBu", "1");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals("1", string0);
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("m`", "0-3fgo0vboqp+B");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("00", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("0-3fgo0vboqp+B", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("2", string0);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("OX0g\"D,!c[#4mj8m)IkX", "OX0g\"D,!c[#4mj8m)IkX");
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("O", bcWord0.getMetricCode());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("m`", "0-3fgo0vboqp+B");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("00", bcWord0.getMetricCode());
      assertEquals("0-3fgo0vboqp+B", string0);
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.setEqualWord("-v(%_f0TOE8f)~d&", "-v(%_f0TOE8f)~d&");
      boolean boolean0 = bcWord0.equalTo("");
      assertTrue(boolean0);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      boolean boolean0 = bcWord0.equalTo("");
      assertFalse(boolean0);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("w", "n-Dt{&Y~>Tj]C");
      bcWord0.setEqualWord("n-Dt{&Y~>Tj]C", "F ");
      boolean boolean0 = bcWord0.equalTo("n-Dt{&Y~>Tj]C");
      assertEquals("", bcWord0.getMetricCode());
      assertTrue(boolean0);
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      int int0 = bcWord0.getSyllables();
      assertEquals(1, int0);
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.getWord();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test21()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.getPhonemes();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test22()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      String string0 = bcWord0.getMetricCode();
      assertEquals("Z", string0);
      assertEquals(1, bcWord0.getSyllables());
  }
}
