package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_9 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter("oFvj@0EJF>");
      assertNotNull(string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter("ek6KzY7+BXC{r/;<G");
      assertEquals("ek6KzY7+BXC{r/;&lt;G", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter("bRuDv*Be[x\"F");
      assertEquals("bRuDv*Be[x&quot;F", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HTMLFilter.filter((String) null);
      assertNull(string0);
  }

  @Test
  public void test5()  throws Throwable  {
      String string0 = HTMLFilter.filter("&lt;");
      assertEquals("&amp;lt;", string0);
      assertNotNull(string0);
  }

  @Test
  public void test6()  throws Throwable  {
      HTMLFilter hTMLFilter0 = new HTMLFilter();
  }
}
