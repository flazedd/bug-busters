package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_6 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = Utils.nChars(4527, '(');
      boolean boolean0 = Utils.pseudoAbsoluteURL(string0);
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = Utils.nChars(0, 'S');
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
      Utils.nChars(5780, 'S');
      // Undeclared exception!
      Utils.nChars(5780, 'S');
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-4433), 'G');
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
      String string0 = Utils.nChars(6792, '\u001E');
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
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
      String string0 = Utils.nChars(4527, '(');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test12()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("/;#mbP");
      assertTrue(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("~~~~");
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/dKa<gV~:`|3;T ");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":VYNmy");
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("^1?a}CY`-+F;2:/\"");
      assertTrue(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePath("KfD$?");
      assertEquals("KfD$$$", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath(":.p_O#Q%_");
      assertEquals("~.p__O#Q%__", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("*qq6/fh0");
      assertEquals("_qq6-fh0", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("_$olq/;Ub=-4F{Q1");
      assertEquals("__$$olq-;Ub=--4F{Q1", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath("~~");
      assertEquals("~~~~", string0);
  }
}
