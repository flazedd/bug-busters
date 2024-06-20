package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute("9t#0o C@", "9t#0o C@", ")0r[dh");
      assertEquals(")0r[dh", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("F A7{zD;kfbJ>ZA`hN", 34);
      assertEquals("               F A7{zD;kfbJ>ZA`hN", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 0);
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("0");
      assertEquals(1, intArray0.length);
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
        StringUtils.splitBy((String) null, 'Z');
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
      StringUtils.leftPad("`+B,KZ])tQ&H#", 5416);
      // Undeclared exception!
      StringUtils.leftPad("`+B,KZ])tQ&H#", 5416);
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, 1244);
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
      String string0 = StringUtils.substitute("", "p$oy=,x", "p$oy=,x");
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("F A7{zD;kfbJ>ZA`hN");
      assertEquals("F A7{zD;&#x007f;kfbJ&gt;ZA`hN", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("j&f mNu<#'");
      assertEquals("j&amp;f mNu&lt;#&apos;", string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("Eklk7q0[\"K4{<");
      assertEquals("Eklk7q0[&quot;K&#x007f;4{&lt;", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts("|i=I+z'");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"|i=I+z'\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test17()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("");
      assertArrayEquals(new int[] {}, intArray0);
  }

  @Test
  public void test18()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy("quM({`", '(');
      assertEquals(2, stringArray0.length);
  }

  @Test
  public void test19()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy("QF)da", '-');
      assertEquals(1, stringArray0.length);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = StringUtils.leftPad("|i=I+z'", 1);
      assertEquals("|i=I+z'", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitByLines("");
      assertEquals(1, stringArray0.length);
  }
}
