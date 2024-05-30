package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute("&gt;", "&gt;", "&gt;");
      assertEquals("&gt;", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("0g>B:j(~sz&hm_U6!8M", 37);
      assertEquals("                  0g>B:j(~sz&hm_U6!8M", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 0);
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = StringUtils.substitute("", "&#x", "&#x");
      assertEquals("", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("3");
      assertArrayEquals(new int[] {3}, intArray0);
  }

  @Test
  public void test05()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("");
      assertEquals("", string0);
  }

  @Test
  public void test06()  throws Throwable  {
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
  public void test07()  throws Throwable  {
      String string0 = StringUtils.leftPad("corina.util.StringUtils", 5996);
      StringUtils.splitBy(string0, '\"');
      // Undeclared exception!
      StringUtils.splitByLines(string0);
  }

  @Test
  public void test08()  throws Throwable  {
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
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.splitBy((String) null, '#');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test10()  throws Throwable  {
      StringUtils.leftPad("m.RFe<1{7az`Brh/o", 3640);
      StringUtils.leftPad("m.RFe<1{7az`Brh/o", 3640);
      // Undeclared exception!
      StringUtils.leftPad("m.RFe<1{7az`Brh/o", 3640);
  }

  @Test
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, 34);
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
        StringUtils.extractInts((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 5072);
      String string1 = StringUtils.escapeForXML(string0);
      // Undeclared exception!
      StringUtils.escapeForXML(string1);
  }

  @Test
  public void test14()  throws Throwable  {
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
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("r>oiy]YorboAKr~KE2");
      assertEquals("r&gt;oiy]YorboAKr~KE2", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.escapeForXML(".BM#tnM<");
      assertEquals(".BM#tnM&lt;", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("+U3qx&93");
      assertEquals("+U3qx&amp;93", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("?hMes'\"Z,6o");
      assertEquals("?hMes&apos;&quot;&#x007f;Z,6o", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts("[HrZ@UmW,N~=P3UcVB");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"[HrZ@UmW,N~=P3UcVB\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test20()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("");
      assertArrayEquals(new int[] {}, intArray0);
  }

  @Test
  public void test21()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy("?hMes'\"Z,6o", '');
      assertEquals(2, stringArray0.length);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = StringUtils.leftPad("", (-1759));
      assertEquals("", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitByLines("/T$");
      assertEquals(1, stringArray0.length);
  }
}
