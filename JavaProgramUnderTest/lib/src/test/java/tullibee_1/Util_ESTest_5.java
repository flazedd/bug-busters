package tullibee_1;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Collection;
import java.util.Vector;
public class Util_ESTest_5 {

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
      int int0 = Util.StringCompare((String) null, "");
      assertEquals(0, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = Util.StringCompare("t@H[7[/o5", "com.ib.client.Util");
      assertEquals(17, int0);
  }

  @Test
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
      Vector<Object> vector0 = new Vector<Object>();
      vector0.setSize(1772);
      Vector<Object> vector1 = new Vector<Object>(vector0);
      // Undeclared exception!
      try { 
        Util.VectorEqualsUnordered(vector1, vector0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.ib.client.Util", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      String string0 = Util.NormalizeString((String) null);
      assertEquals("", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      String string0 = Util.NormalizeString("M_yV5my%[ouK ~}}");
      assertEquals("M_yV5my%[ouK ~}}", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      String string0 = Util.DoubleMaxString(1.7976931348623157E308);
      assertEquals("", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      String string0 = Util.DoubleMaxString(Integer.MAX_VALUE);
      assertEquals("2.147483647E9", string0);
  }

  @Test
  public void test10()  throws Throwable  {
      String string0 = Util.IntMaxString(Integer.MAX_VALUE);
      assertEquals("", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      String string0 = Util.IntMaxString(1127);
      assertEquals("1127", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      Vector<Integer> vector0 = new Vector<Integer>();
      Integer integer0 = new Integer(1043);
      vector0.addElement(integer0);
      Vector<Object> vector1 = new Vector<Object>();
      vector0.add(integer0);
      vector1.add((Object) integer0);
      Object object0 = new Object();
      vector1.add(object0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      Vector<Integer> vector0 = new Vector<Integer>();
      Integer integer0 = new Integer(1043);
      vector0.addElement(integer0);
      Vector<Object> vector1 = new Vector<Object>();
      vector1.add((Object) integer0);
      boolean boolean0 = Util.VectorEqualsUnordered(vector1, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      Vector<Integer> vector0 = new Vector<Integer>();
      Integer integer0 = new Integer((-1));
      vector0.add(integer0);
      Vector<Object> vector1 = new Vector<Object>();
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
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
      Vector<Integer> vector0 = new Vector<Integer>();
      boolean boolean0 = Util.VectorEqualsUnordered((Vector) null, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      Vector<Integer> vector0 = new Vector<Integer>();
      boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector0);
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("t@H[7[/o5", (String) null);
      assertEquals(10, int0);
  }

  @Test
  public void test19()  throws Throwable  {
      boolean boolean0 = Util.StringIsEmpty("ve2");
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
      int int0 = Util.StringCompare("", "7DhgV`<#Te6");
      assertEquals((-11), int0);
  }

  @Test
  public void test23()  throws Throwable  {
      int int0 = Util.StringCompareIgnCase("0.0", "O#p6;q$^dx.&C");
      assertEquals((-63), int0);
  }

  @Test
  public void test24()  throws Throwable  {
      Util util0 = new Util();
  }
}
