package imsmart_11;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class HTMLFilter_ESTest_8 {

  @Test
  public void test0()  throws Throwable  {
      String string0 = HTMLFilter.filter("");
      assertEquals("", string0);
  }

  @Test
  public void test1()  throws Throwable  {
      String string0 = HTMLFilter.filter("jWN>1 \"4b?d%6oQb");
      assertEquals("jWN&gt;1 &quot;4b?d%6oQb", string0);
  }

  @Test
  public void test2()  throws Throwable  {
      String string0 = HTMLFilter.filter("OK7zNK\"~zc6&x;Yt");
      assertEquals("OK7zNK&quot;~zc6&amp;x;Yt", string0);
  }

  @Test
  public void test3()  throws Throwable  {
      String string0 = HTMLFilter.filter((String) null);
      assertNull(string0);
  }

  @Test
  public void test4()  throws Throwable  {
      String string0 = HTMLFilter.filter("<X|N{f=RIjI=YG7");
      assertEquals("&lt;X|N{f=RIjI=YG7", string0);
      assertNotNull(string0);
  }

  @Test
  public void test5()  throws Throwable  {
      HTMLFilter hTMLFilter0 = new HTMLFilter();
  }
}
