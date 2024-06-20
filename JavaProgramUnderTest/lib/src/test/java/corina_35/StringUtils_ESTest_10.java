package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_10 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute("&#x", "&#x", "");
      assertEquals("", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("Y4|}o9kg5", 15);
      assertEquals("      Y4|}o9kg5", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 0);
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = StringUtils.leftPad("", (-840));
      assertEquals("", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("4");
      assertArrayEquals(new int[] {4}, intArray0);
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
      String string0 = StringUtils.leftPad("", 5189);
      StringUtils.splitBy(string0, 'i');
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
      String string0 = StringUtils.leftPad("", 5202);
      StringUtils.splitBy(string0, 'i');
      // Undeclared exception!
      StringUtils.splitBy(string0, 'i');
  }

  @Test
  public void test10()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.splitBy((String) null, 'q');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test11()  throws Throwable  {
      StringUtils.leftPad("GD`%v+iO'b%qF ?", 5300);
      // Undeclared exception!
      StringUtils.leftPad("GD`%v+iO'b%qF ?", 5300);
  }

  @Test
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, 872);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test13()  throws Throwable  {
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
  public void test14()  throws Throwable  {
      String string0 = StringUtils.leftPad(">>sKSshm/Ap9Bsr?b", 6325);
      String string1 = StringUtils.escapeForXML(string0);
      // Undeclared exception!
      StringUtils.escapeForXML(string1);
  }

  @Test
  public void test15()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.escapeForXML((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.substitute("", "IZqp*M", "");
      assertEquals("", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = StringUtils.substitute("ey<b}m>e=^F%! Q", "", "Nj}M<M~57sp6#<q;j");
      assertEquals("Nj}M<M~57sp6#<q;jey<b}m>e=^F%! Q", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("T1VErbu'");
      assertEquals("T1VErbu&apos;", string0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = StringUtils.escapeForXML(".<<cRtP&54`bJI>");
      assertEquals(".&lt;&lt;cRtP&amp;54`bJI&gt;", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("g={\".:%4F2@=j#");
      assertEquals("g={&quot;.:%4F2@=j#", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts("Nj}M<M~57sp6#<q;j");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"Nj}M<M~57sp6#<q;j\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test22()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("");
      assertArrayEquals(new int[] {}, intArray0);
  }

  @Test
  public void test23()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy("/6Jo(qM#6cI8IP%e(", 'M');
      assertEquals(2, stringArray0.length);
  }

  @Test
  public void test24()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitByLines("");
      assertEquals(1, stringArray0.length);
  }
}
