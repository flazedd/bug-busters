package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "S41Uo&NkX]");
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
      bcWord bcWord0 = new bcWord("g#R5!;-J!EUh|V", "");
      int int0 = bcWord0.getSyllables();
      assertEquals(0, int0);
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("g#R5!;-J!EUh|V", "");
      bcWord0.getRhymeKey(false);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("g#R5!;-J!EUh|V", "");
      bcWord0.setEqualWord("g#R5!;-J!EUh|V", (String) null);
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.setEqualWord("0", ".u{iP4'rd9j_^}O");
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("g#R5!;-J!EUh|V", "");
      String string0 = bcWord0.getMetricCode();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("!=m2", "!=m2");
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
  public void test08()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
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
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.setEqualWord("2", "{FDdxUr[ -qvj6:1&7|");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("-qvj6:1&7|", string0);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("bcry.bcWord", "bcry.bcWord");
      bcWord0.setEqualWord("", ";P5u&(N0e|V5_U");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals(";P5u&(N0e|V5_U", string0);
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("k%SIZ{=Id262Unn", "k%SIZ{=Id262Unn");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("22", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("k%SIZ{=Id262Unn", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("k%SIZ{=Id262Unn", "k%SIZ{=Id262Unn");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("22", bcWord0.getMetricCode());
      assertEquals("k%SIZ{=Id262Unn", string0);
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("2", string0);
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("gp0_vrA", "gp0_vrA");
      assertEquals("O", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("bcry.bcWord", "bcry.bcWord");
      bcWord0.setEqualWord("I", "");
      boolean boolean0 = bcWord0.equalTo("bcry.bcWord");
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      boolean boolean0 = bcWord0.equalTo("{FDdxUr[ -qvj6:1&7|");
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("k%SIZ{=Id262Unn", "k%SIZ{=Id262Unn");
      boolean boolean0 = bcWord0.equalTo("k%SIZ{=Id262Unn");
      assertTrue(boolean0);
      assertEquals("22", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      int int0 = bcWord0.getSyllables();
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(1, int0);
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
      bcWord bcWord0 = new bcWord("g#R5!;-J!EUh|V", "");
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test22()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      String string0 = bcWord0.getMetricCode();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", string0);
  }
}
