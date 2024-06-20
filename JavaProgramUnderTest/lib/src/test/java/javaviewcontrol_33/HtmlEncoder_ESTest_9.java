package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HtmlEncoder_ESTest_9 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HtmlEncoder.encode("");
      assertEquals("", string0);
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
      String string0 = HtmlEncoder.encode("-d>(M4R:&{6>00Q");
      assertEquals("-d&gt;(M4R:&amp;{6&gt;00Q", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HtmlEncoder.encode("'&lt;xPtNPA5^?es!");
      assertEquals("'&amp;lt;xPtNPA5^?es!", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HtmlEncoder.encode("q/c!dr=\"*,1k!");
      assertEquals("q/c!dr=&quot;*,1k!", string0);
  }

  @Test
  public void test5()  throws Throwable  {
      String string0 = HtmlEncoder.encode("'<xPtNPA5^?es!");
      assertEquals("'&lt;xPtNPA5^?es!", string0);
  }

  @Test
  public void test6()  throws Throwable  {
      HtmlEncoder htmlEncoder0 = new HtmlEncoder();
  }
}
