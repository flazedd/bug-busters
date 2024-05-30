package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("!t&Uzou>slm0l|");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = Utils.nChars(0, '9');
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
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
  public void test03()  throws Throwable  {
      Utils.nChars(5440, 'Y');
      // Undeclared exception!
      Utils.nChars(5440, 'Y');
  }

  @Test
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-2162), 'h');
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier("");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test06()  throws Throwable  {
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
  public void test07()  throws Throwable  {
      String string0 = Utils.nChars(2618, '@');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test08()  throws Throwable  {
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
  public void test09()  throws Throwable  {
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
  public void test10()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("///////////////////////////////");
      assertTrue(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("[hnQ");
      assertFalse(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/:/1x._cHZe4\"6(cI*");
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":|()G5.");
      assertTrue(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("__49__0bcgYN");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("P$_r=Z7$:\u0002/Ly}{jVF");
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = Utils.encodePathAsIdentifier("yjBy!KI%(<Y(i!]XE~");
      assertEquals("yjBy_33_KI_37__40__60_Y_40_i_33__93_XE_126_", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = Utils.encodePath("_");
      assertEquals("__", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePath("j8yj^?i#Q#OO/]^-0");
      assertEquals("j8yj^$i#Q#OO-]^--0", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath(":|()G5.");
      assertEquals("~|()G5.", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("EL~JgpLvZ&;%w*(h]");
      assertEquals("EL~~JgpLvZ&;%w_(h]", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("j8yj^$i#Q#OO-]^--0");
      assertEquals("j8yj^$$i#Q#OO--]^----0", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath("");
      assertEquals("", string0);
  }
}
