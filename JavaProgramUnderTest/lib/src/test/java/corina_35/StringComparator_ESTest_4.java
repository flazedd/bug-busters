package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringComparator_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "J[z-=m>JYfl[QZv", (Object) "J[z-=m>JYfl[QZv");
      assertEquals(0, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "B.U", (Object) "iin|JFsuI^mv<D>o");
      assertEquals((-1), int0);
  }

  @Test
  public void test02()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringComparator.compare((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringComparator", e);
      }
  }

  @Test
  public void test03()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      // Undeclared exception!
      try { 
        stringComparator0.compare((Object) null, (Object) null);
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
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        stringComparator0.compare(object0, object0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // java.lang.Object cannot be cast to java.lang.String
         //
         //verifyException("corina.util.StringComparator", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = StringComparator.compare(" TI{Q)", "-R;IZ)/-G");
      assertEquals((-13), int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = StringComparator.compare("", "d\"N/P\u0002!nF|@");
      assertEquals((-1), int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = StringComparator.compare("w]?", "eb");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = StringComparator.compare(" TI{Q)", "");
      assertEquals(1, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = StringComparator.compare(" T{Q)", " T{Q)");
      assertEquals(0, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "-R;IZ)/-G", (Object) " >5y'6OI[=EOyt`");
      assertEquals(13, int0);
  }
}
