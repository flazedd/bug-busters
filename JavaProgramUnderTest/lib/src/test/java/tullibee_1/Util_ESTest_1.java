package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Collection;
import java.util.Vector;

public class Util_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Object> vector1 = new Vector<Object>();
      vector1.add((Object) vector0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("", "");
      assertEquals(0, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("O.ekT&8*,#i4D! A", "");
      assertEquals(16, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = Util.StringCompare("", "");
      assertEquals(0, int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = Util.StringCompare("%j", "com.ib.client.Util");
      assertEquals((-62), int0);
  }

  @Test
  public void test05()  throws Throwable  {
      String string0 = Util.NormalizeString("op<");
      assertEquals("op<", string0);
  }

  @Test
  public void test06()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Object> vector1 = new Vector<Object>();
      vector1.add((Object) vector0);
      vector0.add((Object) vector1);
      // Undeclared exception!
      try { 
        Util.VectorEqualsUnordered(vector1, vector0);
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test07()  throws Throwable  {
      Vector<Integer> vector0 = new Vector<Integer>();
      vector0.add((Integer) null);
      Vector<Object> vector1 = new Vector<Object>(vector0);
      // Undeclared exception!
      try { 
        Util.VectorEqualsUnordered(vector0, vector1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.ib.client.Util", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
      String string0 = Util.NormalizeString("");
      assertEquals("", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      String string0 = Util.DoubleMaxString(1.7976931348623157E308);
      assertEquals("", string0);
  }

  @Test
  public void test10()  throws Throwable  {
      String string0 = Util.DoubleMaxString((-662.5533533));
      assertEquals("-662.5533533", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      String string0 = Util.IntMaxString(Integer.MAX_VALUE);
      assertEquals("", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      String string0 = Util.IntMaxString(8);
      assertEquals("8", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Object object0 = new Object();
      vector0.add(object0);
      vector0.add(object0);
      Vector<Object> vector1 = new Vector<Object>();
      vector1.addAll((Collection<?>) vector0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Integer integer0 = 8;
      vector0.add((Object) integer0);
      Vector<Object> vector1 = new Vector<Object>();
      vector1.add((Object) null);
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Integer integer0 = 877;
      vector0.add((Object) integer0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, (Vector) null);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, (Vector) null);
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      boolean boolean0 = Util.VectorEqualsUnordered((Vector) null, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Util.NormalizeString((String) null);
      assertEquals("", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty("op<");
      assertFalse(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty("");
      assertTrue(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty((String) null);
      assertTrue(boolean0);
  }

  @Test
  public void test23()  throws Throwable  {
      int int0 = Util.StringCompare("`2n", "");
      assertEquals(3, int0);
  }

  @Test
  public void test24()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("3", "Tq?}6 X");
      assertEquals((-65), int0);
  }

  @Test
  public void test25()  throws Throwable  {
      Util util0 = new Util();
  }
}
