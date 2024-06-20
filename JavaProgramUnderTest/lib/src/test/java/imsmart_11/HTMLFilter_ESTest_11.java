package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_11 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter(".&S>n(u &");
      assertEquals(".&amp;S&gt;n(u &amp;", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter("7B?bbON/\"YT+");
      assertEquals("7B?bbON/&quot;YT+", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter((String) null);
      assertNull(string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HTMLFilter.filter("7<5O#k-BU");
      assertNotNull(string0);
      assertEquals("7&lt;5O#k-BU", string0);
  }

  @Test
  public void test5()  throws Throwable  {
      HTMLFilter hTMLFilter0 = new HTMLFilter();
  }
}
