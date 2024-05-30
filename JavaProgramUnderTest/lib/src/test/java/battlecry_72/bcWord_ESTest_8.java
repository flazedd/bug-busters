package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "HcmL1A=");
      bcWord0.getWord();
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test01()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.getWord();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test02()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      int int0 = bcWord0.getSyllables();
      assertEquals(0, int0);
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("HcmL1A=", "HcmL1A=");
      bcWord0.setEqualWord("a]j_)~", "");
      bcWord0.getRhymeKey(false);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("XR", "XR");
      bcWord0.setEqualWord("", (String) null);
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "]Jm]<xp)aBb')D=5U7:");
      bcWord0.setEqualWord("$a[N vt'>Yor/^n>Gy<", "");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      String string0 = bcWord0.getMetricCode();
      assertEquals("", string0);
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("j", "j");
      bcWord0.setEqualWord((String) null, (String) null);
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
      bcWord bcWord0 = new bcWord("", "");
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
      bcWord bcWord0 = new bcWord("HcmL1A=", "HcmL1A=");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("HcmL1A=", string0);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("-w y-Cz0=AFj&", "-w y-Cz0=AFj&");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("O", bcWord0.getMetricCode());
      assertEquals("y-Cz0=AFj&", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("S&Ej1)KyX?]#8!BK~2", "S&Ej1)KyX?]#8!BK~2");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("12", bcWord0.getMetricCode());
      assertEquals("S&Ej1)KyX?]#8!BK~2", string0);
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2o4iU8Xd6\"Wk3!Bk", "2o4iU8Xd6\"Wk3!Bk");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("2o4iU8Xd6\"Wk3!Bk", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("S&Ej1)KyX?]#8!BK~2", "S&Ej1)KyX?]#8!BK~2");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("S&Ej1)KyX?]#8!BK~2", string0);
      assertEquals("12", bcWord0.getMetricCode());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("[]>d0pQYEje:qU~!]Kh", "[]>d0pQYEje:qU~!]Kh");
      bcWord0.setEqualWord("", "[]>d0pQYEje:qU~!]Kh");
      boolean boolean0 = bcWord0.equalTo("[]>d0pQYEje:qU~!]Kh");
      assertEquals(1, bcWord0.getSyllables());
      assertTrue(boolean0);
      assertEquals("O", bcWord0.getMetricCode());
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("HcmL1A=", "HcmL1A=");
      boolean boolean0 = bcWord0.equalTo(";");
      assertEquals(1, bcWord0.getSyllables());
      assertFalse(boolean0);
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2o4iU8Xd6\"Wk3!Bk", "2o4iU8Xd6\"Wk3!Bk");
      boolean boolean0 = bcWord0.equalTo("2o4iU8Xd6\"Wk3!Bk");
      assertTrue(boolean0);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("HcmL1A=", "HcmL1A=");
      int int0 = bcWord0.getSyllables();
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, int0);
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("HcmL1A=", "HcmL1A=");
      bcWord0.getWord();
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord("[]>d0pQYEje:qU~!]Kh", "[]>d0pQYEje:qU~!]Kh");
      bcWord0.getPhonemes();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("O", bcWord0.getMetricCode());
  }

  @Test
  public void test21()  throws Throwable  {
      bcWord bcWord0 = new bcWord("[]>d0pQYEje:qU~!]Kh", "[]>d0pQYEje:qU~!]Kh");
      String string0 = bcWord0.getMetricCode();
      assertEquals("O", string0);
      assertEquals(1, bcWord0.getSyllables());
  }
}
