package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Collection;
import java.util.Spliterator;
import java.util.Vector;
public class Util_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Object> vector1 = new Vector<Object>();
      vector1.add((Object) vector0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector1, vector0);
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("q,nZ{x34F", "");
      assertEquals(9, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("", ":");
      assertEquals((-1), int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = Util.StringCompare("mXQ\"18+RCl1STt*7", "mXQ\"18+RCl1STt*7");
      assertEquals(0, int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = Util.StringCompare("", "mXQ\"18+RCl1STt*7");
      assertEquals((-16), int0);
  }

  @Test
  public void test05()  throws Throwable  {
      String string0 = Util.NormalizeString("E?9R|G\"OCZpY]");
      assertEquals("E?9R|G\"OCZpY]", string0);
  }

  @Test
  public void test06()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Object> vector1 = new Vector<Object>();
      vector0.add((Object) vector1);
      vector1.add((Object) vector0);
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
      String string0 = Util.DoubleMaxString(1.0);
      assertEquals("1.0", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      String string0 = Util.IntMaxString(Integer.MAX_VALUE);
      assertEquals("", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      String string0 = Util.IntMaxString((-2202));
      assertEquals("-2202", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Integer integer0 = new Integer(1412);
      vector0.add((Object) integer0);
      Vector<Object> vector1 = new Vector<Object>(vector0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector1, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Spliterator<Object> spliterator0 = vector0.spliterator();
      Vector<Object> vector1 = new Vector<Object>();
      vector1.add((Object) "");
      vector1.add((Object) "");
      vector0.add((Object) "");
      vector0.add((Object) spliterator0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector1, vector0);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Object> vector1 = new Vector<Object>();
      vector1.add((Object) "");
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
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
      Vector<Integer> vector0 = new Vector<Integer>();
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
      boolean boolean0 = Util.StringIsEmpty("0.0");
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
      int int0 = Util.StringCompare("es;t", "-3784.0");
      assertEquals(56, int0);
  }

  @Test
  public void test24()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("", "");
      assertEquals(0, int0);
  }

  @Test
  public void test25()  throws Throwable  {
      Util util0 = new Util();
  }
}
