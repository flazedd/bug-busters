package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_2 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter("MqrD|x>roN0e");
      assertEquals("MqrD|x&gt;roN0e", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter("3P7<HaX%~");
      assertEquals("3P7&lt;HaX%~", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter("&quot;");
      assertEquals("&amp;quot;", string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HTMLFilter.filter("\"H%");
      assertEquals("&quot;H%", string0);
  }

  @Test
  public void test5()  throws Throwable  {
      String string0 = HTMLFilter.filter((String) null);
      assertNull(string0);
  }

  @Test
  public void test6()  throws Throwable  {
      HTMLFilter hTMLFilter0 = new HTMLFilter();
  }
}
