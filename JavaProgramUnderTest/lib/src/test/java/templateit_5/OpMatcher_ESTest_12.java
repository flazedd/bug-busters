package templateit_5;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class OpMatcher_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = OpMatcher.matchTemplateName("fG");
      assertTrue(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      __NamedStyle namedStyle0 = OpMatcher.matchStyle("");
      assertNull(namedStyle0);
  }

  @Test
  public void test02()  throws Throwable  {
      __NamedStyle namedStyle0 = OpMatcher.matchStyle((String) null);
      assertNull(namedStyle0);
  }

  @Test
  public void test03()  throws Throwable  {
      boolean boolean0 = OpMatcher.matchTemplateName("");
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      boolean boolean0 = OpMatcher.matchTemplateName((String) null);
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      String string0 = OpMatcher.matchTemplateParameter("}(?{+#4k>L`zb");
      assertNotNull(string0);
      assertEquals("4", string0);
  }

  @Test
  public void test06()  throws Throwable  {
      String string0 = OpMatcher.matchTemplateParameter("CRU/R5o4ADCSo#");
      assertNull(string0);
  }

  @Test
  public void test07()  throws Throwable  {
      String string0 = OpMatcher.matchTemplateParameter("E#adRXcf>&iw>,:#");
      assertEquals("adRX", string0);
      assertNotNull(string0);
  }

  @Test
  public void test08()  throws Throwable  {
      String string0 = OpMatcher.matchTemplateParameter("@tbegin");
      assertNull(string0);
  }

  @Test
  public void test09()  throws Throwable  {
      String string0 = OpMatcher.matchTemplateParameter((String) null);
      assertNull(string0);
  }

  @Test
  public void test10()  throws Throwable  {
      boolean boolean0 = OpMatcher.matchTemplateEnd("w^&1E*|L|byM<-n)5");
      assertFalse(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      boolean boolean0 = OpMatcher.matchTemplateEnd("@template_end");
      assertTrue(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      boolean boolean0 = OpMatcher.matchTemplateEnd("@tend");
      assertTrue(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      // Undeclared exception!
      try { 
        OpMatcher.matchTemplateEnd((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.templateit.OpMatcher", e);
      }
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = OpMatcher.matchTemplateBegin("");
      assertNull(stringArray0);
  }

  @Test
  public void test15()  throws Throwable  {
      String[] stringArray0 = OpMatcher.matchTemplateBegin("@template_begin");
      assertNull(stringArray0);
  }

  @Test
  public void test16()  throws Throwable  {
      String[] stringArray0 = OpMatcher.matchTemplateBegin("@tbegin");
      assertNull(stringArray0);
  }

  @Test
  public void test17()  throws Throwable  {
      String[] stringArray0 = OpMatcher.matchTemplateBegin((String) null);
      assertNull(stringArray0);
  }

  @Test
  public void test18()  throws Throwable  {
      OpMatcher opMatcher0 = new OpMatcher();
  }
}
