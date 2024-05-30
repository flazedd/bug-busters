package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("hs;Ff");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":j`o#H.A`b>V<mx");
      assertTrue(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Utils.nChars(0, 'q');
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
      Utils.nChars(6530, '`');
      // Undeclared exception!
      Utils.nChars(6530, 'o');
  }

  @Test
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-2355), '9');
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
      String string0 = Utils.encodePath("|R~+GU&2");
      assertEquals("|R~~+GU&2", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("/");
      assertTrue(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = Utils.nChars(1715, ',');
      boolean boolean0 = Utils.pseudoAbsoluteURL(string0);
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/#(9(D:?Hv>=[");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = Utils.nChars(4012, '2');
      boolean boolean0 = Utils.absoluteURL(string0);
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("Y:b/c0oXmYi[ 4hpsm");
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = Utils.encodePathAsIdentifier("}XP|a#{0 ");
      assertEquals("_125_XP_124_a_35__123_0_32_", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.nChars(4012, '2');
      String string1 = Utils.encodePathAsIdentifier(string0);
      String string2 = Utils.encodePathAsIdentifier(string1);
      // Undeclared exception!
      Utils.encodePathAsIdentifier(string2);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath("Y:b/c0oXmYi[ 4hpsm");
      assertEquals("Y~b-c0oXmYi[ 4hpsm", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("W%g@?ex\"Z->Rl4#.");
      assertEquals("W%g@$ex\"Z-->Rl4#.", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("`Ydi*Jv");
      assertEquals("`Ydi_Jv", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath("Z8$I:6tT0kmg?@lX");
      assertEquals("Z8$$I~6tT0kmg$@lX", string0);
  }

  @Test
  public void test24()  throws Throwable  {
      String string0 = Utils.encodePath("5fG,zyci3_");
      assertEquals("5fG,zyci3__", string0);
  }
}
