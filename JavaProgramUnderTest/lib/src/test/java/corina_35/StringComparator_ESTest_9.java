package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringComparator_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = StringComparator.compare("y{8wC5}BI<>kS3gJR+", "-]=gKA`ELvo'H>");
      assertEquals(82, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = StringComparator.compare("D", "y");
      assertEquals((-1), int0);
  }

  @Test
  public void test02()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "", (Object) "pwS9(]7]l@m3}");
      assertEquals((-1), int0);
  }

  @Test
  public void test03()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringComparator.compare("", (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringComparator", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      // Undeclared exception!
      try { 
        stringComparator0.compare((Object) "]Ci2*@;G*XshVX RW", (Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringComparator", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      // Undeclared exception!
      try { 
        stringComparator0.compare((Object) stringComparator0, (Object) stringComparator0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // corina.util.StringComparator cannot be cast to java.lang.String
         //
         //verifyException("corina.util.StringComparator", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = StringComparator.compare("E<y`_YYj=JB5Hkj(3", "E<y`_YYj=JB5Hkj(3");
      assertEquals(0, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = StringComparator.compare("corina.util.StringComparator", "");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = StringComparator.compare("", "T'$}3bJG0>Z16Wx4c");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = StringComparator.compare("-]=gKA`ELvo'H>", "y{8wC5}BI<>kS3gJR+");
      assertEquals((-82), int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = StringComparator.compare("bN", "> m");
      assertEquals(1, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "T'$}3bJG0>Z16Wx4c", (Object) "");
      assertEquals(1, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "eKN0k", (Object) "eKN0k");
      assertEquals(0, int0);
  }
}
