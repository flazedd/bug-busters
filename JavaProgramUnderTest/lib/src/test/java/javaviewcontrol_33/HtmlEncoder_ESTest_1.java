package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HtmlEncoder_ESTest_1 {

  @Test
  public void test0()  throws Throwable  {
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
  public void test1()  throws Throwable  {
      String string0 = HtmlEncoder.encode("c'a\"=vX[M)^ohbx>FQa");
      assertEquals("c'a&quot;=vX[M)^ohbx&gt;FQa", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HtmlEncoder.encode("%9HY?l8N&,i!<E");
      assertEquals("%9HY?l8N&amp;,i!&lt;E", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HtmlEncoder.encode("");
      assertEquals("", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      HtmlEncoder htmlEncoder0 = new HtmlEncoder();
  }
}
