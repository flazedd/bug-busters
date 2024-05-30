package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_7 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "");
      bcWord0.getWord();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test01()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.getWord();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test02()  throws Throwable  {
      bcWord bcWord0 = new bcWord("{=I.", "");
      int int0 = bcWord0.getSyllables();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("W", "INSZZ{(TC2x");
      bcWord0.setEqualWord("ObQfJe1", "");
      bcWord0.getRhymeKey(true);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("iE$1]gq#dP$", "O/<;H");
      bcWord0.setEqualWord("", (String) null);
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("{=I.", "");
      String string0 = bcWord0.getMetricCode();
      assertEquals("", string0);
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("iE$1]gq#dP$", "O/<;H");
      bcWord0.setEqualWord("", (String) null);
      // Undeclared exception!
      try { 
        bcWord0.getRhymeKey(true);
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
      bcWord bcWord0 = new bcWord("?sM3.ty'jyO=*\"Q", "?sM3.ty'jyO=*\"Q");
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
      bcWord bcWord0 = new bcWord("%Q pDWh2Wj]@ux", "%Q pDWh2Wj]@ux");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("pDWh2Wj]@ux", string0);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("u\"1o&Ym2v/OBLV&qY!", "u\"1o&Ym2v/OBLV&qY!");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("12", bcWord0.getMetricCode());
      assertEquals("u\"1o&Ym2v/OBLV&qY!", string0);
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("`#1b", "`#1b");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals("`#1b", string0);
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("I", "0");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("0", string0);
      assertEquals("O", bcWord0.getMetricCode());
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("80[dF5VD_W6)i2%{", "80[dF5VD_W6)i2%{");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("02", bcWord0.getMetricCode());
      assertEquals("80[dF5VD_W6)i2%{", string0);
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("4", "");
      bcWord0.setEqualWord("", "4");
      boolean boolean0 = bcWord0.equalTo("4");
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
      assertTrue(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("`#1b", "`#1b");
      boolean boolean0 = bcWord0.equalTo("0");
      assertFalse(boolean0);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("`#1b", "`#1b");
      int int0 = bcWord0.getSyllables();
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, int0);
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("`#1b", "`#1b");
      bcWord0.getWord();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("m00Jg3h=", "9z]VH");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord("`#1b", "`#1b");
      String string0 = bcWord0.getMetricCode();
      assertEquals("I", string0);
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test21()  throws Throwable  {
      bcWord bcWord0 = new bcWord("`#1b", "`#1b");
      bcWord0.setEqualWord("", "`#1b");
      boolean boolean0 = bcWord0.equalTo("");
      assertTrue(boolean0);
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }
}
