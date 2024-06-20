package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_10 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("'%Bwj 3LWG.q");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":9L(6@dV*;D|");
      assertTrue(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Utils.nChars(0, 'D');
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = Utils.encodePath("");
      assertEquals("", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.pseudoAbsoluteURL((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      Utils.nChars('\uFFFD', '\uFFFD');
  }

  @Test
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-3558), 'D');
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test
  public void test07()  throws Throwable  {
      String string0 = Utils.encodePathAsIdentifier("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
      String string1 = Utils.encodePathAsIdentifier(string0);
      Utils.encodePathAsIdentifier(string1);
      // Undeclared exception!
      Utils.encodePathAsIdentifier(string0);
  }

  @Test
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier("");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test10()  throws Throwable  {
      String string0 = Utils.nChars(5541, 'K');
      String string1 = Utils.encodePath(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePath((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.absoluteURL((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test13()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("/");
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("D");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/:Go$.Q[UKV5)mP7g");
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("lSrxPSI4A:|i/25");
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("yKfjb-;W$zz");
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePath("_45_R");
      assertEquals("__45__R", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath("yKfjb;W?zz");
      assertEquals("yKfjb;W$zz", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("w)R~^,UVEm#@3]@:)(");
      assertEquals("w)R~~^,UVEm#@3]@~)(", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("0=<w-1']u");
      assertEquals("0=<w--1']u", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath(")2y*ak\r oD4");
      assertEquals(")2y_ak\r oD4", string0);
  }

  @Test
  public void test24()  throws Throwable  {
      String string0 = Utils.encodePath("hCU6D=08b$\" 8/) A");
      assertEquals("hCU6D=08b$$\" 8-) A", string0);
  }
}
