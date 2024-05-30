package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_7 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter("=KJl6atdoAn>");
      assertEquals("=KJl6atdoAn&gt;", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter("c-Jyf4&<H");
      assertEquals("c-Jyf4&amp;&lt;H", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter("ptj*=\"KJtMWLK2Bn[b0");
      assertEquals("ptj*=&quot;KJtMWLK2Bn[b0", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HTMLFilter.filter((String) null);
      assertNull(string0);
  }

  @Test
  public void test5()  throws Throwable  {
      HTMLFilter hTMLFilter0 = new HTMLFilter();
  }
}
