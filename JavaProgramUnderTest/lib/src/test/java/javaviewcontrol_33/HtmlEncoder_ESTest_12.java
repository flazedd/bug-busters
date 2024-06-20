package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HtmlEncoder_ESTest_12 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HtmlEncoder.encode("Z\u0007s=\"nVp");
      assertEquals("Z\u0007s=&quot;nVp", string0);
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
      String string0 = HtmlEncoder.encode("e,w>K;*f3a'%NWO07JD");
      assertEquals("e,w&gt;K;*f3a'%NWO07JD", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HtmlEncoder.encode("|X<S$=Xrh");
      assertEquals("|X&lt;S$=Xrh", string0);
  }

  @Test
  public void test5()  throws Throwable  {
      String string0 = HtmlEncoder.encode("&amp;");
      assertEquals("&amp;amp;", string0);
  }

  @Test
  public void test6()  throws Throwable  {
      HtmlEncoder htmlEncoder0 = new HtmlEncoder();
  }
}
