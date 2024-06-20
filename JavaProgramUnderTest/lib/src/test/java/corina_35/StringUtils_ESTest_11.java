package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute("/", "/", "/");
      assertEquals("/", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("$}3FXjyT&amp;w&lt;6.jxt+[k", 34);
      assertEquals("        $}3FXjyT&amp;w&lt;6.jxt+[k", string0);
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
      }
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.splitBy((String) null, 'i');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test08()  throws Throwable  {
      StringUtils.leftPad("", 4699);
      StringUtils.leftPad("&gt;", 4699);
      // Undeclared exception!
      StringUtils.leftPad("&gt;", 1865);
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, 12);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
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
      String string0 = StringUtils.substitute("", "gN_g:BL0_383Hx]", "");
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("wB@F+{P(<`H");
      assertEquals("wB&#x007f;@F+{P(&lt;`H", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("'h6.iS R");
      assertEquals("&apos;h6.iS R", string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("&apos;h6.iS R");
      assertEquals("&amp;apos;h6.iS R", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("s,-m>u\";U)NUH");
      assertEquals("s,-m&gt;u&quot;;U)NUH", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts("2E1s8MH3^n=e`_}K");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"2E1s8MH3^n=e`_}K\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test18()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("");
      assertArrayEquals(new int[] {}, intArray0);
  }

  @Test
  public void test19()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy("wB&#x007f;@F+{P(&lt;`H", '0');
      assertEquals(3, stringArray0.length);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = StringUtils.leftPad("TJPR%4~-7aC", (-1627));
      assertEquals("TJPR%4~-7aC", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = StringUtils.leftPad("yW-4'", 4283);
      StringUtils.splitBy(string0, 'y');
      StringUtils.splitByLines(string0);
      // Undeclared exception!
      StringUtils.splitBy(string0, 'y');
  }
}
