package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_2 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL(".");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = Utils.nChars(0, '\\');
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Utils.encodePath("");
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
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
  public void test04()  throws Throwable  {
      Utils.nChars(5290, '9');
      // Undeclared exception!
      Utils.nChars(5290, '~');
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-1), '\"');
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      String string0 = Utils.nChars(2661, ']');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePathAsIdentifier(string1);
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier("");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test09()  throws Throwable  {
      String string0 = Utils.nChars(3325, '[');
      String string1 = Utils.encodePath(string0);
      String string2 = Utils.encodePath(string0);
      Utils.encodePath(string1);
      // Undeclared exception!
      Utils.encodePath(string2);
  }

  @Test
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
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
  public void test12()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("/$QGY(a|DO1CrVxT^rc");
      assertTrue(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("C]lcT:O2/{,!a");
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/}'+{6q#R|zY:");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":N<ye-M(O{");
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("--");
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("C]lcT:O2/{,!a");
      assertTrue(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePath("4U 1fi85NvC,S'~F_");
      assertEquals("4U 1fi85NvC,S'~~F__", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath("1?Nmf");
      assertEquals("1$Nmf", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("q*h-\"B2edlD");
      assertEquals("q_h--\"B2edlD", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("$$");
      assertEquals("$$$$", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath("C]lcT:O2/{,!a");
      assertEquals("C]lcT~O2-{,!a", string0);
  }
}
