package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_4 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter("Ov,<Ng'q>K|:D");
      assertEquals("Ov,&lt;Ng'q&gt;K|:D", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter("@?#&wjo9Qht52K:Z");
      assertEquals("@?#&amp;wjo9Qht52K:Z", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter("@.B%$?uMlk'.4W\"");
      assertEquals("@.B%$?uMlk'.4W&quot;", string0);
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
