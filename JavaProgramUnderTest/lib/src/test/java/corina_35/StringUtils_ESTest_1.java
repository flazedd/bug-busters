package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringUtils_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringUtils.substitute(",VpcWs .#XhTI&v}}J", ",VpcWs .#XhTI&v}}J", ",VpcWs .#XhTI&v}}J");
      assertEquals(",VpcWs .#XhTI&v}}J", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringUtils.leftPad("", 0);
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("0");
      assertArrayEquals(new int[] {0}, intArray0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("");
      assertEquals("", string0);
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
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.splitBy((String) null, 'E');
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
      StringUtils.leftPad("2y#4nmP2^wg", 6247);
      // Undeclared exception!
      StringUtils.leftPad("zMryP0o", 6247);
  }

  @Test
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.leftPad((String) null, (-400));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringUtils", e);
      }
  }

  @Test
  public void test09()  throws Throwable  {
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
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
      String string0 = StringUtils.substitute("", "yiFIK3<^$dsB5ZQ.(.f", "&quot;");
      assertEquals("", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      String string0 = StringUtils.escapeForXML(";i? >r~lt~'");
      assertEquals(";i? &gt;r~lt~&apos;", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("K#cU'i ");
      assertEquals("&#x007f;K#cU&apos;i ", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("&quot;");
      assertEquals("&amp;quot;", string0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("\"v6YrFc");
      assertEquals("&quot;v6YrFc", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      String string0 = StringUtils.escapeForXML("yiFIK3<^$dsB5ZQ.(.f");
      assertEquals("yiFIK3&lt;^$dsB5ZQ.(.f", string0);
  }

  @Test
  public void test17()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.extractInts("El/Mp{pcvpu3<nhYRo");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"El/Mp{pcvpu3<nhYRo\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test18()  throws Throwable  {
      int[] intArray0 = StringUtils.extractInts("");
      assertEquals(0, intArray0.length);
  }

  @Test
  public void test19()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitBy("^PpQ+7MY.U", '^');
      assertEquals(2, stringArray0.length);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = StringUtils.leftPad("El/Mp{pcvpu3<nhYRo", 33);
      assertEquals("               El/Mp{pcvpu3<nhYRo", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = StringUtils.leftPad("El/Mp{pcvpu3<nhYRo", 4);
      assertEquals("El/Mp{pcvpu3<nhYRo", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String[] stringArray0 = StringUtils.splitByLines("yiFIK3&lt;^$dsB5ZQ.(.f");
      assertEquals(1, stringArray0.length);
  }
}
