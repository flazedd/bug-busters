package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("M");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/Mk*{:Bh7N");
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":ni");
      assertTrue(boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = Utils.nChars(0, ',');
      assertEquals("", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      String string0 = Utils.encodePath("");
      assertEquals("", string0);
  }

  @Test
  public void test05()  throws Throwable  {
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
  public void test06()  throws Throwable  {
      Utils.nChars(7560, '/');
      // Undeclared exception!
      Utils.nChars(7560, '3');
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-1), '`');
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
      String string0 = Utils.nChars(3407, '.');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePathAsIdentifier(string1);
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier("");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePath((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
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
      String string0 = Utils.nChars(2508, ')');
      boolean boolean0 = Utils.pseudoAbsoluteURL(string0);
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("I`:mJ/#e4'`*S7T0e9t");
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = Utils.encodePath("~i");
      assertEquals("~~i", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.nChars(3407, '.');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath("w/Mk*{:Bh7N");
      assertEquals("w-Mk_{~Bh7N", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath(";X>hZ(T5/C/<-");
      assertEquals(";X>hZ(T5-C-<--", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("Z#?K|He/,7O*FD@}R*G");
      assertEquals("Z#$K|He-,7O_FD@}R_G", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath("$$");
      assertEquals("$$$$", string0);
  }
}
