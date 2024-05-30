package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_6 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "&@w^5|?UD");
      bcWord0.getWord();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
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
      bcWord bcWord0 = new bcWord(".LmlE%_3 p~y*", ".LmlE%_3 p~y*");
      int int0 = bcWord0.getSyllables();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("q?9", "q?9");
      bcWord0.setEqualWord("", "");
      bcWord0.getRhymeKey(true);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("g#<h`Z.=>0", "g#<h`Z.=>0");
      bcWord0.setEqualWord("F!d;yq1:a!$T-(>]0L/", (String) null);
      bcWord0.getPhonemes();
      assertEquals("O", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "Qp+)");
      bcWord0.setEqualWord("u", "");
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("g#<h`Z.=>0", "g#<h`Z.=>0");
      String string0 = bcWord0.getMetricCode();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("O", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("emz%_3 ~y", "emz%_3 ~y");
      bcWord0.setEqualWord("emz%_3 ~y", (String) null);
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
      bcWord bcWord0 = new bcWord("zz` j+2DB2M", "zz` j+2DB2M");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("22", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("j+2DB2M", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("q?9", "q?9");
      bcWord0.setEqualWord("", "1");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals("1", string0);
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("}T51hu@Q0XBsuJ.", "}T51hu@Q0XBsuJ.");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("}T51hu@Q0XBsuJ.", string0);
      assertEquals("10", bcWord0.getMetricCode());
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("1", "1");
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("q?9", "q?9");
      bcWord0.setEqualWord("", "");
      boolean boolean0 = bcWord0.equalTo("q?9");
      assertTrue(boolean0);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("q?9", "q?9");
      boolean boolean0 = bcWord0.equalTo("");
      assertEquals(0, bcWord0.getSyllables());
      assertFalse(boolean0);
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("}T51hu@t0XBsuJ.", "}T51hu@t0XBsuJ.");
      boolean boolean0 = bcWord0.equalTo("}T51hu@t0XBsuJ.");
      assertEquals("10", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("g#<h`Z.=>0", "g#<h`Z.=>0");
      int int0 = bcWord0.getSyllables();
      assertEquals(1, int0);
      assertEquals("O", bcWord0.getMetricCode());
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("g#<h`Z.=>0", "g#<h`Z.=>0");
      bcWord0.getWord();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("O", bcWord0.getMetricCode());
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("k>2qxcU(ay", "/5pDY lF@jMSU?");
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord("q?9", "q?9");
      String string0 = bcWord0.getMetricCode();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", string0);
  }
}
