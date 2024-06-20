package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_10 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "gAXTGyyq?");
      bcWord0.getWord();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test01()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "1");
      bcWord0.getWord();
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test02()  throws Throwable  {
      bcWord bcWord0 = new bcWord("(r8KEZ\"2aITub<", "(r8KEZ\"2aITub<");
      int int0 = bcWord0.getSyllables();
      assertEquals(1, int0);
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("M{gSX{~</mS3'p!", "");
      bcWord0.getRhymeKey(true);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "1");
      bcWord0.setEqualWord("1", (String) null);
      bcWord0.getPhonemes();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord("\\ZYjRob7uz3T", "\\ZYjRob7uz3T");
      bcWord0.setEqualWord("", "");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("fZ#<;rH!=2 e;\"Za", "fZ#<;rH!=2 e;\"Za");
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
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("f{^h/230Q73p", "f{^h/230Q73p");
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
      bcWord bcWord0 = new bcWord(":DSs2#", ":DSs2#");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(":DSs2#", string0);
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test10()  throws Throwable  {
      bcWord bcWord0 = new bcWord("fZ#< (;r!=!\u0013 ;\"Za", "fZ#< (;r!=!\u0013 ;\"Za");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("fZ#< (;r!=!\u0013 ;\"Za", string0);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord(":DSs2#", "i");
      bcWord0.setEqualWord("If!rnzk-?q(", "! \"R[#|1Zk1[r");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("\"R[#|1Zk1[r", string0);
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("f{^h/230Q73p", "f{^h/230Q73p");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("20", bcWord0.getMetricCode());
      assertEquals("f{^h/230Q73p", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("i", ":DSs2#");
      String string0 = bcWord0.getMetricCode();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("={X^hUDa0Q73p", "={X^hUDa0Q73p");
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("O", bcWord0.getMetricCode());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("f{^h/230Q73p", "f{^h/230Q73p");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("20", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("f{^h/230Q73p", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "1");
      bcWord0.setEqualWord("]?!GM|aRw N4D?J?tL", "]?!GM|aRw N4D?J?tL");
      boolean boolean0 = bcWord0.equalTo("");
      assertTrue(boolean0);
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord(":DSs2#", "i");
      boolean boolean0 = bcWord0.equalTo("&\r#f)h'4^GBY$1");
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("\\ZYjRob7uz3T", "\\ZYjRob7uz3T");
      boolean boolean0 = bcWord0.equalTo("\\ZYjRob7uz3T");
      assertEquals(0, bcWord0.getSyllables());
      assertTrue(boolean0);
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("\\ZYjRob7uz3T", "\\ZYjRob7uz3T");
      int int0 = bcWord0.getSyllables();
      assertEquals(0, int0);
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord(":DSs2#", "i");
      bcWord0.getWord();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test21()  throws Throwable  {
      bcWord bcWord0 = new bcWord(":DSs2#", "i");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test22()  throws Throwable  {
      bcWord bcWord0 = new bcWord(":DSs2#", "i");
      String string0 = bcWord0.getMetricCode();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", string0);
  }
}
