package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_12 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter(">|Vycim#u)B");
      assertEquals("&gt;|Vycim#u)B", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter("=a<\"");
      assertEquals("=a&lt;&quot;", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter((String) null);
      assertNull(string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HTMLFilter.filter("&quot;");
      assertEquals("&amp;quot;", string0);
      assertNotNull(string0);
  }

  @Test
  public void test5()  throws Throwable  {
      HTMLFilter hTMLFilter0 = new HTMLFilter();
  }
}
