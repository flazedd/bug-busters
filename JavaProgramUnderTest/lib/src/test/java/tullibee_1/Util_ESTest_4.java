package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Collection;
import java.util.Vector;
public class Util_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      Vector<Integer> vector0 = new Vector<Integer>();
      Integer integer0 = new Integer(2740);
      vector0.add(integer0);
      boolean boolean0 = Util.VectorEqualsUnordered((Vector) null, vector0);
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("0.0", "0.0");
      assertEquals(0, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("aR-e)", ",9a=wM");
      assertEquals(53, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = Util.StringCompare("kn+|/YwhD", "kn+|/YwhD");
      assertEquals(0, int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = Util.StringCompare("/u 6HzL*X", "[RK~CaydFZ@");
      assertEquals((-44), int0);
  }

  @Test
  public void test05()  throws Throwable  {
      String string0 = Util.NormalizeString("sn*g=QP");
      assertEquals("sn*g=QP", string0);
  }

  @Test
  public void test06()  throws Throwable  {
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
      String string0 = Util.NormalizeString((String) null);
      assertEquals("", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      String string0 = Util.DoubleMaxString(1.7976931348623157E308);
      assertEquals("", string0);
  }

  @Test
  public void test10()  throws Throwable  {
      String string0 = Util.DoubleMaxString((-658.30646749));
      assertEquals("-658.30646749", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      String string0 = Util.IntMaxString(Integer.MAX_VALUE);
      assertEquals("", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      String string0 = Util.IntMaxString((-3574));
      assertEquals("-3574", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      Integer integer0 = new Integer((-2751));
      Vector<Integer> vector0 = new Vector<Integer>();
      vector0.add(integer0);
      Vector<Object> vector1 = new Vector<Object>(239);
      vector0.add(integer0);
      vector1.addAll((Collection<?>) vector0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector1, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Integer> vector1 = new Vector<Integer>();
      Integer integer0 = new Integer(357);
      vector1.add(integer0);
      Integer integer1 = new Integer(1544);
      vector0.add((Object) integer1);
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      Vector<Integer> vector1 = new Vector<Integer>();
      Integer integer0 = new Integer(357);
      vector1.add(integer0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector1, vector0);
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
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase((String) null, "`Dhe=sjcg");
      assertEquals((-9), int0);
  }

  @Test
  public void test19()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty("p?6%");
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty("");
      assertTrue(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty((String) null);
      assertTrue(boolean0);
  }

  @Test
  public void test22()  throws Throwable  {
      int int0 = Util.StringCompare("sn*g=QP", "nF5<j1");
      assertEquals(5, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      Util util0 = new Util();
  }
}
