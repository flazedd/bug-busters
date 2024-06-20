package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "0");
      bcWord0.getWord();
      assertEquals("O", bcWord0.getMetricCode());
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
      bcWord bcWord0 = new bcWord("VV^61A\"#C`I", "VV^61A\"#C`I");
      int int0 = bcWord0.getSyllables();
      assertEquals(1, int0);
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("O", ">TDM\")m'5K|UO#4pq+");
      bcWord0.setEqualWord("l,]", "");
      bcWord0.getRhymeKey(true);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("m6Fd5jFp", "");
      bcWord0.setEqualWord("wl,?l&`YE3s", (String) null);
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord("O", ">TDM\")m'5K|UO#4pq+");
      bcWord0.setEqualWord("l,]", "");
      bcWord0.getPhonemes();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("VV^61A\"#C`I", "VV^61A\"#C`I");
      String string0 = bcWord0.getMetricCode();
      assertEquals("I", string0);
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("z#zZ)) 5;3K6G}lq#", "z#zZ)) 5;3K6G}lq#");
      bcWord0.setEqualWord("z#zZ)) 5;3K6G}lq#", (String) null);
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
      bcWord bcWord0 = new bcWord("m6Fd5jFp", "");
      bcWord0.setEqualWord((String) null, "7");
      // Undeclared exception!
      try { 
        bcWord0.equalTo("E");
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
      bcWord bcWord0 = new bcWord("m6Fd5jFp", "");
      bcWord0.setEqualWord("f", "0");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("0", string0);
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("Go3Z; j7wqm1u4", "Go3Z; j7wqm1u4");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("j7wqm1u4", string0);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("]~m28x*z", "]~m28x*z");
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("I|xv5]E2 2", "I|xv5]E2 2");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("2", string0);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("22", bcWord0.getMetricCode());
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("0Lq%s1GZBM3;{U9QylH", "0Lq%s1GZBM3;{U9QylH");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("0Lq%s1GZBM3;{U9QylH", string0);
      assertEquals("01", bcWord0.getMetricCode());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      bcWord0.setEqualWord("I", "m?Hf9");
      boolean boolean0 = bcWord0.equalTo("");
      assertTrue(boolean0);
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("Go3Z; j7wqm1u4", "Go3Z; j7wqm1u4");
      boolean boolean0 = bcWord0.equalTo("");
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("Go3Z; j7wqm1u4", "Go3Z; j7wqm1u4");
      boolean boolean0 = bcWord0.equalTo("Go3Z; j7wqm1u4");
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("I", bcWord0.getMetricCode());
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("m6Fd5jFp", "");
      int int0 = bcWord0.getSyllables();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, int0);
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("Go3Z; j7wqm1u4", "Go3Z; j7wqm1u4");
      bcWord0.getWord();
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord("t1V=!#qN1", "t1V=!#qN1");
      bcWord0.getPhonemes();
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("11", bcWord0.getMetricCode());
  }

  @Test
  public void test21()  throws Throwable  {
      bcWord bcWord0 = new bcWord("m6Fd5jFp", "");
      String string0 = bcWord0.getMetricCode();
      assertEquals("", string0);
      assertEquals(0, bcWord0.getSyllables());
  }
}
