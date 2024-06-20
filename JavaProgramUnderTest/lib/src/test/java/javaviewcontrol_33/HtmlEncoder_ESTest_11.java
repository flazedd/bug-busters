package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HtmlEncoder_ESTest_11 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HtmlEncoder.encode("y2\"ZJ+!csD[ rBMUQ");
      assertEquals("y2&quot;ZJ+!csD[ rBMUQ", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      // Undeclared exception!
      try { 
        HtmlEncoder.encode((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.HtmlEncoder", e);
      }
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HtmlEncoder.encode("/dQj%Pe*2bj>5G>#TrB");
      assertEquals("/dQj%Pe*2bj&gt;5G&gt;#TrB", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HtmlEncoder.encode("k<Qrom");
      assertEquals("k&lt;Qrom", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HtmlEncoder.encode("&quot;");
      assertEquals("&amp;quot;", string0);
  }

  @Test
  public void test5()  throws Throwable  {
      String string0 = HtmlEncoder.encode("eD)vRUD PP|");
      assertEquals("eD)vRUD PP|", string0);
  }

  @Test
  public void test6()  throws Throwable  {
      String string0 = HtmlEncoder.encode("");
      assertEquals("", string0);
  }

  @Test
  public void test7()  throws Throwable  {
      HtmlEncoder htmlEncoder0 = new HtmlEncoder();
  }
}
