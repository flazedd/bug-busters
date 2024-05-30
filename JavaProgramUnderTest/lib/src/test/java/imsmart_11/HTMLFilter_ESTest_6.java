package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_6 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("S5bW@*>?i]~a3(OLzP");
      assertEquals("S5bW@*&gt;?i]~a3(OLzP", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter("F98<~^");
      assertEquals("F98&lt;~^", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter("&gt;");
      assertEquals("&amp;gt;", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter(")-kT_{DYtL|\"WhJd");
      assertEquals(")-kT_{DYtL|&quot;WhJd", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HTMLFilter.filter((String) null);
      assertNull(string0);
  }

  @Test
  public void test5()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test6()  throws Throwable  {
      HTMLFilter hTMLFilter0 = new HTMLFilter();
  }
}
