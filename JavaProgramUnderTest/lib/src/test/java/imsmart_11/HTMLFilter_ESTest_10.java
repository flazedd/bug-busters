package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_10 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter("@_5_D\"gt#_>");
      assertEquals("@_5_D&quot;gt#_&gt;", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter((String) null);
      assertNull(string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter("sG1cH=!pB&b2\"res<-");
      assertEquals("sG1cH=!pB&amp;b2&quot;res&lt;-", string0);
      assertNotNull(string0);
  }

  @Test
  public void test4()  throws Throwable  {
      HTMLFilter hTMLFilter0 = new HTMLFilter();
  }
}
