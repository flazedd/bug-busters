package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HtmlEncoder_ESTest_6 {

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
      String string0 = HtmlEncoder.encode("mSv,w}Z>-'rOp~vt@]|");
      assertEquals("mSv,w}Z&gt;-'rOp~vt@]|", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HtmlEncoder.encode("&gt;");
      assertEquals("&amp;gt;", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HtmlEncoder.encode("lmQSM{4/\"Xv");
      assertEquals("lmQSM{4/&quot;Xv", string0);
  }

  @Test
  public void test5()  throws Throwable  {
      String string0 = HtmlEncoder.encode("Ni$U<?WFj*Wcc!mSC");
      assertEquals("Ni$U&lt;?WFj*Wcc!mSC", string0);
  }

  @Test
  public void test6()  throws Throwable  {
      HtmlEncoder htmlEncoder0 = new HtmlEncoder();
  }
}
