package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "V tM[t<<4v$[");
      bcWord0.getWord();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
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
      bcWord bcWord0 = new bcWord(".,7g)^0p/}X@^@", ".,7g)^0p/}X@^@");
      int int0 = bcWord0.getSyllables();
      assertEquals(1, int0);
      assertEquals("O", bcWord0.getMetricCode());
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.setEqualWord("", (String) null);
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.setEqualWord("FViogmyA", "!B?");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      String string0 = bcWord0.getMetricCode();
      assertEquals("", string0);
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("|", "|");
      bcWord0.setEqualWord((String) null, (String) null);
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
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("#G0]!E61ZMVa", "#G0]!E61ZMVa");
      bcWord0.setEqualWord((String) null, "rtChT-){2");
      // Undeclared exception!
      try { 
        bcWord0.equalTo("");
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
  public void test09()  throws Throwable  {
      bcWord bcWord0 = new bcWord("x1EgAx7c=", "x1EgAx7c=");
      bcWord0.setEqualWord("@o4IGE4Z`bcDkIRh*N", "q%LM_ U_q:udx#rG0]");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals("U_q:udx#rG0]", string0);
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test10()  throws Throwable  {
      bcWord bcWord0 = new bcWord("<t~O6~r2}p2mt]`hx", "<t~O6~r2}p2mt]`hx");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("<t~O6~r2}p2mt]`hx", string0);
      assertEquals("22", bcWord0.getMetricCode());
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("|WSa^21pn26G,)0]!", "|WSa^21pn26G,)0]!");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("2120", bcWord0.getMetricCode());
      assertEquals(4, bcWord0.getSyllables());
      assertEquals("|WSa^21pn26G,)0]!", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "");
      bcWord0.getRhymeKey(true);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("FV3sB4+X^]7;", "2");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("2", string0);
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("53$d1BH#+X3l(U#5", "53$d1BH#+X3l(U#5");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("53$d1BH#+X3l(U#5", string0);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.setEqualWord("FViogmyA", "!B?");
      boolean boolean0 = bcWord0.equalTo("");
      assertTrue(boolean0);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("|WSa^21pn26G,)0]!", "|WSa^21pn26G,)0]!");
      boolean boolean0 = bcWord0.equalTo("n");
      assertFalse(boolean0);
      assertEquals(4, bcWord0.getSyllables());
      assertEquals("2120", bcWord0.getMetricCode());
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "");
      boolean boolean0 = bcWord0.equalTo("2");
      assertTrue(boolean0);
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      int int0 = bcWord0.getSyllables();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, int0);
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord(".,7g)^0p/}X@^@", ".,7g)^0p/}X@^@");
      bcWord0.getWord();
      assertEquals("O", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test21()  throws Throwable  {
      bcWord bcWord0 = new bcWord("|WSa^21pn26G,)0]!", "|WSa^21pn26G,)0]!");
      String string0 = bcWord0.getMetricCode();
      assertEquals(4, bcWord0.getSyllables());
      assertEquals("2120", string0);
  }
}
