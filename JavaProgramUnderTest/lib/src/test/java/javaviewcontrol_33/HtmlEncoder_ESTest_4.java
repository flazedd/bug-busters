package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HtmlEncoder_ESTest_4 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HtmlEncoder.encode("^_PkF|F> +Q9&g95^");
      assertEquals("^_PkF|F&gt; +Q9&amp;g95^", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HtmlEncoder.encode("");
      assertEquals("", string0);
  }

  @Test
  public void test2()  throws Throwable  {
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
  public void test3()  throws Throwable  {
      String string0 = HtmlEncoder.encode("p3P\"FC(?d<w|Kk");
      assertEquals("p3P&quot;FC(?d&lt;w|Kk", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      HtmlEncoder htmlEncoder0 = new HtmlEncoder();
  }
}
