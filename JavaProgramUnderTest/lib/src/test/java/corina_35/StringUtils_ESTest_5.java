package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute("jh|\"*l`b`G[vpYzN`", "jh|\"*l`b`G[vpYzN`", "%w6+'y/arwZ+C/sOi");
      assertEquals("%w6+'y/arwZ+C/sOi", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("&apos;Iw=$h31?%h", 21);
      assertEquals("     &apos;Iw=$h31?%h", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = StringUtils.leftPad("(`8oc ", (-3215));
      assertEquals("(`8oc ", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("0");
      assertEquals(1, intArray0.length);
  }

  @Test
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 4313);
      StringUtils.splitBy(string0, 't');
      StringUtils.splitByLines(string0);
      // Undeclared exception!
      StringUtils.splitByLines(string0);
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
        StringUtils.splitBy((String) null, 'r');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test08()  throws Throwable  {
      StringUtils.leftPad("&#x", 5080);
      // Undeclared exception!
      StringUtils.leftPad("&quot;", 5080);
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, 260);
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
      String string0 = StringUtils.substitute("", "                                                                                                                                                                                                                                                                                                                                                                                                                                                                       E\".(oK", "");
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("                                             o>-D:0zadThp|6ORk");
      assertEquals("                                             o&gt;-D:0zadThp|6ORk", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("6{of=BPf{z}aHW<");
      assertEquals("6{of=BPf{&#x007f;z}aHW&lt;", string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("%w6+'y/arwZ+C/sOi");
      assertEquals("%&#x007f;w6+&apos;y/arwZ+C/sOi", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("                                             o&gt;-D:0zadThp|6ORk");
      assertEquals("                                             o&amp;gt;-D:0zadThp|6ORk", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("E\".(oK");
      assertEquals("E&quot;.(oK", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("");
      assertEquals("", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts("corina.util.StringUtils");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"corina.util.StringUtils\"
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
      String[] stringArray0 = StringUtils.splitBy("e'p|uk]*nF+Zo", 'k');
      assertEquals(2, stringArray0.length);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 0);
      assertEquals("", string0);
  }
}
