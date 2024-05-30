package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_7 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute(").7z2'D9As#HSK", ").7z2'D9As#HSK", ").&#x007f;7z2&apos;D9As#HSK");
      assertEquals(").&#x007f;7z2&apos;D9As#HSK", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("Qq|+Mwc&{F7", 13);
      assertEquals("  Qq|+Mwc&{F7", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 0);
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("0");
      assertArrayEquals(new int[] {0}, intArray0);
  }

  @Test
  public void test04()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("");
      assertEquals("", string0);
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.substitute((String) null, (String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringUtils", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.splitByLines((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringUtils", e);
      }
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.splitBy((String) null, 'm');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringUtils", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
      StringUtils.leftPad("]RyG@-", 5061);
      // Undeclared exception!
      StringUtils.leftPad("]RyG@-", 5061);
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, (-269));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringUtils", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts((String) null);
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
        StringUtils.escapeForXML((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringUtils", e);
      }
  }

  @Test
  public void test12()  throws Throwable  {
      String string0 = StringUtils.substitute("&apos;", "z>1`&[y(W/4YHNuaI", "");
      assertEquals("&apos;", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = StringUtils.substitute("", "", "");
      assertEquals("", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("z>1`&[y(W/4YHNuaI");
      assertEquals("z&gt;1`&amp;[y(W/4YHNuaI", string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("`L0*0&!X8W<d(u&jH.");
      assertEquals("`L0*0&amp;!X8W&lt;d(u&amp;jH.", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.escapeForXML(").7z2'D9As#HSK");
      assertEquals(").&#x007f;7z2&apos;D9As#HSK", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("^hI~5tkDBg \"p4");
      assertEquals("^hI~5tkDBg &quot;p4", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts("                                                                                                                                                                                                                                                                                                                                                                                                                                                                               2&K");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"2&K\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test19()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("");
      assertArrayEquals(new int[] {}, intArray0);
  }

  @Test
  public void test20()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy("corina.util.StringUtils", 'n');
      assertEquals(3, stringArray0.length);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = StringUtils.leftPad("", (-796));
      assertEquals("", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitByLines("");
      assertEquals(1, stringArray0.length);
  }
}
