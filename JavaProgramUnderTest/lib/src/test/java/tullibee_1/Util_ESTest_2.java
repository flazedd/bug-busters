package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.Collection;
import java.util.Vector;

public class Util_ESTest_2 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("", "");
      assertEquals(0, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase((String) null, "0");
      assertEquals((-1), int0);
  }

  @Test
  public void test02()  throws Throwable  {
      int int0 = Util.StringCompare("com.ib.client.Util", (String) null);
      assertEquals(18, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = Util.StringCompare("\"m10zz8%vpQl", "0");
      assertEquals((-14), int0);
  }

  @Test
  public void test04()  throws Throwable  {
      String string0 = Util.NormalizeString("1");
      assertEquals("1", string0);
  }

  @Test
  public void test05()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Object> vector1 = new Vector<Object>();
      vector0.add((Object) vector1);
      vector1.add((Object) vector0);
      // Undeclared exception!
      try { 
        Util.VectorEqualsUnordered(vector0, vector1);
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test06()  throws Throwable  {
      String string0 = Util.NormalizeString((String) null);
      assertEquals("", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      String string0 = Util.DoubleMaxString(1.7976931348623157E308);
      assertEquals("", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      String string0 = Util.DoubleMaxString(0.0);
      assertEquals("0.0", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      String string0 = Util.IntMaxString(Integer.MAX_VALUE);
      assertEquals("", string0);
  }

  @Test
  public void test10()  throws Throwable  {
      String string0 = Util.IntMaxString((-1265));
      assertEquals("-1265", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      Integer integer0 = new Integer((-989));
      Vector<Integer> vector0 = new Vector<Integer>();
      vector0.add(integer0);
      vector0.add((Integer) null);
      Vector<Integer> vector1 = new Vector<Integer>();
      vector1.addAll((Collection<? extends Integer>) vector0);
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
  public void test12()  throws Throwable  {
      Integer integer0 = new Integer((-989));
      Vector<Integer> vector0 = new Vector<Integer>();
      Integer integer1 = new Integer(1);
      Vector<Object> vector1 = new Vector<Object>();
      vector1.add((Object) integer0);
      vector0.addElement(integer1);
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Integer integer0 = new Integer((-989));
      Vector<Integer> vector0 = new Vector<Integer>();
      vector0.add(integer0);
      Vector<Integer> vector1 = new Vector<Integer>();
      vector1.addAll((Collection<? extends Integer>) vector0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Integer integer0 = new Integer((-989));
      Vector<Integer> vector0 = new Vector<Integer>();
      vector0.add(integer0);
      Vector<Object> vector1 = new Vector<Object>();
      boolean boolean0 = Util.VectorEqualsUnordered(vector1, vector0);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Vector<Integer> vector0 = new Vector<Integer>();
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, (Vector) null);
      assertTrue(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      boolean boolean0 = Util.VectorEqualsUnordered((Vector) null, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty("0.0");
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty("");
      assertTrue(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty((String) null);
      assertTrue(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      int int0 = Util.StringCompare("T", "T");
      assertEquals(0, int0);
  }

  @Test
  public void test22()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("-550", (String) null);
      assertEquals(4, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      Util util0 = new Util();
      Vector<Object> vector0 = new Vector<Object>();
      vector0.add((Object) util0);
      Vector<Object> vector1 = new Vector<Object>();
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
      assertFalse(boolean0);
  }
}
