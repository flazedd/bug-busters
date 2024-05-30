package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_3 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("--");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = Utils.nChars(0, 't');
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Utils.encodePath("");
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.pseudoAbsoluteURL((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      // Undeclared exception!
      Utils.nChars('\uFFFD', '\uFFFD');
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-1), '4');
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier("");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePath((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.absoluteURL((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("/C*@c");
      assertTrue(boolean0);
  }

  @Test
  public void test11()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("F0+)6_iXhu9`f~hP");
      assertFalse(boolean0);
  }

  @Test
  public void test12()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test13()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/RvO:NtUSLIS");
      assertFalse(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":9;.j??g");
      assertTrue(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      String string0 = Utils.nChars(3041, '>');
      boolean boolean0 = Utils.absoluteURL(string0);
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":.?/g");
      assertTrue(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      String string0 = Utils.encodePathAsIdentifier("F0+)6_iXhu9`f~hP");
      assertEquals("F0_43__41_6_iXhu9_96_f_126_hP", string0);
  }

  @Test
  public void test18()  throws Throwable  {
      String string0 = Utils.nChars(3041, '>');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePath("WA_eji;?V");
      assertEquals("WA__eji;$V", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath("D!<N:+ f7A=wb]lr`");
      assertEquals("D!<N~+ f7A=wb]lr`", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("U  {TqY~F--/e");
      assertEquals("U  {TqY~~F-----e", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("S.dCg*[O69y");
      assertEquals("S.dCg_[O69y", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath("I9N$f8%7\"1&");
      assertEquals("I9N$$f8%7\"1&", string0);
  }
}
