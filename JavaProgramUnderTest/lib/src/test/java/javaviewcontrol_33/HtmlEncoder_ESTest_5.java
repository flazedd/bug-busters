package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HtmlEncoder_ESTest_5 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HtmlEncoder.encode("VHD:>%Yf{!");
      assertEquals("VHD:&gt;%Yf{!", string0);
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
      String string0 = HtmlEncoder.encode("\"&<>");
      assertEquals("&quot;&amp;&lt;&gt;", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HtmlEncoder.encode("e~fr~:hfq/-fu5f{ !`");
      assertEquals("e~fr~:hfq/-fu5f{ !`", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HtmlEncoder.encode("");
      assertEquals("", string0);
  }

  @Test
  public void test5()  throws Throwable  {
      HtmlEncoder htmlEncoder0 = new HtmlEncoder();
  }
}
