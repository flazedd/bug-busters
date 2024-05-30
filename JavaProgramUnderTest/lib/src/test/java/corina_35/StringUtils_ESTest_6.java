package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_6 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute("Ta!2", "Ta!2", "Ta!2");
      assertEquals("Ta!2", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("uW4D-$>z&", 10);
      assertEquals(" uW4D-$>z&", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 0);
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("");
      assertEquals(0, intArray0.length);
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
        StringUtils.splitBy((String) null, 'g');
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
      StringUtils.leftPad("V{` ^Yxdh`;", 5708);
      // Undeclared exception!
      StringUtils.leftPad("V{` ^Yxdh`;", 5708);
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, 71);
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
        StringUtils.extractInts("J");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"J\"
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
      String string0 = StringUtils.substitute("", "7NCaPAXs; ", "");
      assertEquals("", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("|AK1bs\"wyDFgE>u?");
      assertEquals("|AK1bs&quot;wyDFgE&gt;u?", string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML(")<3vv]}K");
      assertEquals(")&lt;3vv]}K", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("|Y#)h2h&2jd,]ik");
      assertEquals("|&#x007f;Y#)h2h&amp;2&#x007f;jd,]ik", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("|g@a+p'\"Ps+PnEXE|");
      assertNotNull(string0);
  }

  @Test
  public void test18()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("0");
      assertEquals(1, intArray0.length);
  }

  @Test
  public void test19()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy("DO/Oa(7gW$N}R=6V", '=');
      assertEquals(2, stringArray0.length);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = StringUtils.leftPad("7NCaPAXs; ", (-2779));
      assertEquals("7NCaPAXs; ", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitByLines("FpV{zS[Mf");
      assertEquals(1, stringArray0.length);
  }
}
