package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute("et7rVe`KCd", "et7rVe`KCd", "");
      assertEquals("", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 3068);
      String string1 = StringUtils.leftPad(string0, 4186);
      assertFalse(string1.equals((Object)string0));
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
      }
  }

  @Test
  public void test07()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 3835);
      StringUtils.splitBy(string0, '6');
      StringUtils.splitBy(string0, 'P');
      // Undeclared exception!
      StringUtils.splitBy(string0, '6');
  }

  @Test
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.splitBy((String) null, 'h');
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
        StringUtils.leftPad((String) null, 600);
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
      String string0 = StringUtils.substitute("", "etBv%0JluXH1N", (String) null);
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = StringUtils.substitute("&quot;", "", "&quot;");
      assertEquals("&quot;&quot;", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("V{gO_^Fh)jIrD|_e&'");
      assertEquals("V{gO_^Fh)jIrD|_&#x007f;e&amp;&apos;", string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("%0)t*L>&w{hs");
      assertEquals("%0)t*L&gt;&amp;w{hs", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("<\"b");
      assertEquals("&lt;&quot;b", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts("%0)t*L&gt;&amp;w{hs");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"%0)t*L&gt;&amp;w{hs\"
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
      String[] stringArray0 = StringUtils.splitBy("&O!s0bA(0fSx>v1U87", '0');
      assertEquals(3, stringArray0.length);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = StringUtils.leftPad("&quot;", 0);
      assertEquals("&quot;", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      StringUtils.leftPad("&quot;", 4673);
      StringUtils.leftPad("", 4673);
      // Undeclared exception!
      StringUtils.leftPad("A&gt;y]-zI/IYV", 1401);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitByLines("&quot;");
      assertEquals(1, stringArray0.length);
  }
}
