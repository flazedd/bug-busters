package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute("KOnQp", "KOnQp", "KOnQp");
      assertEquals("KOnQp", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("7o0,g,G\"0?EyCZP", 31);
      assertEquals("               7o0,g,G\"0?EyCZP", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = StringUtils.substitute("", "nY{7>;4:#h$", "");
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 0);
      assertEquals("", string0);
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
        StringUtils.splitBy((String) null, 'r');
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
      StringUtils.leftPad("", 4396);
      StringUtils.leftPad("", 4396);
      // Undeclared exception!
      StringUtils.leftPad("", 4396);
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, (-1));
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
        StringUtils.extractInts("G");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"G\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test11()  throws Throwable  {
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
  public void test12()  throws Throwable  {
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
  public void test13()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("nY{7>;4:#h$");
      assertEquals("nY{7&gt;;4:#h$", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = StringUtils.escapeForXML(";8J-tzX-ea;']");
      assertEquals(";8J-tzX-ea;&apos;]", string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("um,42VN&#x007f;&lt;D");
      assertEquals("um,42VN&amp;#x007f;&amp;lt;D", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("7o0,g,G\"0?EyCZP");
      assertEquals("7o0,g,G&quot;0?Ey&#x007f;CZP", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("um,42VN<D");
      assertEquals("um,42VN&#x007f;&lt;D", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("0");
      assertArrayEquals(new int[] {0}, intArray0);
  }

  @Test
  public void test19()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("");
      assertEquals(0, intArray0.length);
  }

  @Test
  public void test20()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy(">H0iT+NTe", '0');
      assertEquals(2, stringArray0.length);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = StringUtils.leftPad("&apos;", 1);
      assertEquals("&apos;", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitByLines("&apos;");
      assertEquals(1, stringArray0.length);
  }
}
