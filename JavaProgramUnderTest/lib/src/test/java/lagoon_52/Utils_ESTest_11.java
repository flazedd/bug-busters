package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL(")WP>");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/:OvrBT6%zyC");
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Utils.nChars(1087, ':');
      boolean boolean0 = Utils.absoluteURL(string0);
      assertTrue(boolean0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = Utils.nChars(0, 'X');
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
      Utils.nChars(5298, 's');
      // Undeclared exception!
      Utils.nChars(5298, 's');
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-2466), 'P');
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
      String string0 = Utils.nChars(4122, ' ');
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
      boolean boolean0 = Utils.pseudoAbsoluteURL("/-BObu~Q78");
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("TEIvKklAB");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("'KL:K8G^iY#o/O");
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = Utils.nChars(4085, '>');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePath("$:?@k9}!d");
      assertEquals("$$~$@k9}!d", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath("F- ?'ba~x7%F*AUO");
      assertEquals("F-- $'ba~~x7%F_AUO", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("1.|$/h5&6#D6(4");
      assertEquals("1.|$$-h5&6#D6(4", string0);
  }
}
