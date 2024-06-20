package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class bcWord_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      bcWord bcWord0 = new bcWord("oI.6OJ8`;]$c}kd|", "TL1[k,clz=2[C%k4");
      bcWord0.setEqualWord("oI.6OJ8`;]$c}kd|", "Z");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("12", bcWord0.getMetricCode());
      assertEquals("Z", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "");
      bcWord0.getWord();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", bcWord0.getMetricCode());
  }

  @Test
  public void test02()  throws Throwable  {
      bcWord bcWord0 = new bcWord("oI.6OJ8`;]$c}kd|", "TL1[k,clz=2[C%k4");
      bcWord0.getWord();
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("12", bcWord0.getMetricCode());
  }

  @Test
  public void test03()  throws Throwable  {
      bcWord bcWord0 = new bcWord("7tKr[G3DW", "7tKr[G3DW");
      int int0 = bcWord0.getSyllables();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, int0);
  }

  @Test
  public void test04()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.setEqualWord("", "");
      bcWord0.getRhymeKey(false);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test05()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "bcry.bcWord");
      bcWord0.setEqualWord("bcry.bcWord", (String) null);
      bcWord0.getPhonemes();
      assertEquals("", bcWord0.getMetricCode());
      assertEquals(0, bcWord0.getSyllables());
  }

  @Test
  public void test06()  throws Throwable  {
      bcWord bcWord0 = new bcWord("2", "2");
      bcWord0.setEqualWord("", "");
      bcWord0.getPhonemes();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test07()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "");
      String string0 = bcWord0.getMetricCode();
      assertEquals(0, bcWord0.getSyllables());
      assertEquals("", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      bcWord bcWord0 = new bcWord("d5=e*;60r6-D{I<r", "d5=e*;60r6-D{I<r");
      bcWord0.setEqualWord("d5=e*;60r6-D{I<r", (String) null);
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
  public void test09()  throws Throwable  {
      bcWord bcWord0 = new bcWord((String) null, "bcry.bcWord");
      // Undeclared exception!
      try { 
        bcWord0.equalTo("W3,C}DqjLp");
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
  public void test11()  throws Throwable  {
      bcWord bcWord0 = new bcWord("D:X!p!r&[]tA113Q_@", "D:X!p!r&[]tA113Q_@");
      String string0 = bcWord0.getRhymeKey(false);
      assertEquals("11", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("D:X!p!r&[]tA113Q_@", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "nhT03=H:~72i");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("nhT03=H:~72i", string0);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("02", bcWord0.getMetricCode());
  }

  @Test
  public void test13()  throws Throwable  {
      bcWord bcWord0 = new bcWord("bh+m~mBLh,if[7%xJ*q", "nEu <}NJVj2.p");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals("<}NJVj2.p", string0);
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test14()  throws Throwable  {
      bcWord bcWord0 = new bcWord("16TIXn&^c[YHz;nA.F", "16TIXn&^c[YHz;nA.F");
      bcWord0.setEqualWord("s;{[.", "s;{[.");
      boolean boolean0 = bcWord0.equalTo("16TIXn&^c[YHz;nA.F");
      assertTrue(boolean0);
      assertEquals("I", bcWord0.getMetricCode());
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test15()  throws Throwable  {
      bcWord bcWord0 = new bcWord("bh+m~mBLh,if[7%xJ*q", "nEu <}NJVj2.p");
      boolean boolean0 = bcWord0.equalTo("nEu <}NJVj2.p");
      assertEquals("Z", bcWord0.getMetricCode());
      assertFalse(boolean0);
      assertEquals(1, bcWord0.getSyllables());
  }

  @Test
  public void test16()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "nhT03=H:~72i");
      boolean boolean0 = bcWord0.equalTo("");
      assertTrue(boolean0);
      assertEquals("02", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test17()  throws Throwable  {
      bcWord bcWord0 = new bcWord("bh+m~mBLh,if[7%xJ*q", "nEu <}NJVj2.p");
      int int0 = bcWord0.getSyllables();
      assertEquals(1, int0);
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test18()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "nhT03=H:~72i");
      bcWord0.getWord();
      assertEquals("02", bcWord0.getMetricCode());
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test19()  throws Throwable  {
      bcWord bcWord0 = new bcWord("bh+m~mBLh,if[7%xJ*q", "nEu <}NJVj2.p");
      bcWord0.getPhonemes();
      assertEquals(1, bcWord0.getSyllables());
      assertEquals("Z", bcWord0.getMetricCode());
  }

  @Test
  public void test20()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "nhT03=H:~72i");
      String string0 = bcWord0.getMetricCode();
      assertEquals("02", string0);
      assertEquals(2, bcWord0.getSyllables());
  }

  @Test
  public void test21()  throws Throwable  {
      bcWord bcWord0 = new bcWord("", "nhT03=H:~72i");
      bcWord0.setEqualWord("", "-%bb0}C");
      String string0 = bcWord0.getRhymeKey(true);
      assertEquals(2, bcWord0.getSyllables());
      assertEquals("02", bcWord0.getMetricCode());
      assertEquals("-%bb0}C", string0);
  }
}
