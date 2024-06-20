package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("--");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/l_A:Qx=[E9i\\-?I");
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Utils.nChars(0, 'F');
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
      Utils.nChars('\uFFF9', '\uFFF9');
  }

  @Test
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-2995), 'E');
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
      boolean boolean0 = Utils.pseudoAbsoluteURL("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
      assertTrue(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      String string0 = Utils.nChars(3144, ';');
      boolean boolean0 = Utils.pseudoAbsoluteURL(string0);
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("?N/7H:\"4%2t");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":R1u:K");
      assertTrue(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = Utils.nChars(3144, ';');
      boolean boolean0 = Utils.absoluteURL(string0);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("+TDHVl#7lYw*h):r/");
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = Utils.nChars(3144, ';');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePathAsIdentifier(string1);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePath("~~");
      assertEquals("~~~~", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.nChars(3144, ';');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("+TDHVl#7lYw*h):r/");
      assertEquals("+TDHVl#7lYw_h)~r-", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("--");
      assertEquals("----", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath("<|A%C$Q'4S?p4Of");
      assertEquals("<|A%C$$Q'4S$p4Of", string0);
  }
}
