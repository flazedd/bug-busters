package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "EazT");
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
      bcWord bcWord0 = new bcWord("6^=AX5U>A$_", "6^=AX5U>A$_");
      int int0 = bcWord0.getSyllables();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("_.1aYjBy", "I");
      bcWord0.setEqualWord("p1@<zHZ%Bu\"'-fQ", "");
      bcWord0.getRhymeKey(false);
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("K`T?)tu(P>74)O%", "");
      bcWord0.setEqualWord("", (String) null);
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord("_.1aYjBy", "I");
      bcWord0.setEqualWord("p1@<zHZ%Bu\"'-fQ", "");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("6^=AX5U>A$_", "6^=AX5U>A$_");
      String string0 = bcWord0.getMetricCode();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("$>%G-*>*ji@1", "$>%G-*>*ji@1");
      bcWord0.setEqualWord("bcry.bcWord", (String) null);
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
      bcWord bcWord0 = new bcWord("!$L]_\"2hm6ME>E(hz'A", "!$L]_\"2hm6ME>E(hz'A");
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
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("2", string0);
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.setEqualWord("~", "+vp#hzZREx-?BY0p5tS");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("+vp#hzZREx-?BY0p5tS", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("r&p{01j_>1vqOWJL=QPe", "r&p{01j_>1vqOWJL=QPe");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("011", bcWord0.getMetricCode());
      assertEquals("r&p{01j_>1vqOWJL=QPe", string0);
      assertEquals(3, bcWord0.getSyllables());
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("r&p{01j_>1vqOWJL=Pe", "r&p{01j_>1vqOWJL=Pe");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("r&p{01j_>1vqOWJL=Pe", string0);
      assertEquals("011", bcWord0.getMetricCode());
      assertEquals(3, bcWord0.getSyllables());
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("I", "+vp#hzZREx-?BY0p5tS");
      assertEquals("O", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("6^=AX5U>A$_", "6^=AX5U>A$_");
      bcWord0.setEqualWord("I", "/8iy0jI< m");
      boolean boolean0 = bcWord0.equalTo("6^=AX5U>A$_");
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
      assertTrue(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("r&p{01j_>1vqOWJL=Pe", "r&p{01j_>1vqOWJL=Pe");
      boolean boolean0 = bcWord0.equalTo("z(\"eg[,hm;[\"$i7y");
      assertFalse(boolean0);
      assertEquals("011", bcWord0.getMetricCode());
      assertEquals(3, bcWord0.getSyllables());
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("I", "!");
      boolean boolean0 = bcWord0.equalTo("I");
      assertTrue(boolean0);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("r&p{01j_>1vqOWJL=Pe", "r&p{01j_>1vqOWJL=Pe");
      int int0 = bcWord0.getSyllables();
      assertEquals(3, int0);
      assertEquals("011", bcWord0.getMetricCode());
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("r&p{01j_>1vqOWJL=Pe", "r&p{01j_>1vqOWJL=Pe");
      bcWord0.getWord();
      assertEquals(3, bcWord0.getSyllables());
      assertEquals("011", bcWord0.getMetricCode());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord("r&p{01j_>1vqOWJL=Pe", "r&p{01j_>1vqOWJL=Pe");
      bcWord0.getPhonemes();
      assertEquals(3, bcWord0.getSyllables());
      assertEquals("011", bcWord0.getMetricCode());
  }

  @Test
  public void test21()  throws Throwable  {
      bcWord bcWord0 = new bcWord("r&p{01j_>1vqOWJL=Pe", "r&p{01j_>1vqOWJL=Pe");
      String string0 = bcWord0.getMetricCode();
      assertEquals(3, bcWord0.getSyllables());
      assertEquals("011", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.setEqualWord("2", "+ K2qNd~Zj23&");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("Z", bcWord0.getMetricCode());
      assertEquals("K2qNd~Zj23&", string0);
      assertEquals(1, bcWord0.getSyllables());
  }
}
