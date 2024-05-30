package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringComparator_ESTest_6 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = StringComparator.compare("-e_^{|br^hKUVQT?\t", " m&@xQ");
      assertEquals(13, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = StringComparator.compare("kW", "RX]");
      assertEquals((-1), int0);
  }

  @Test
  public void test02()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "", (Object) "^i(ktekDZqDIn~_M");
      assertEquals((-1), int0);
  }

  @Test
  public void test03()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringComparator.compare((String) null, "");
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
        stringComparator0.compare((Object) null, (Object) "");
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
  public void test06()  throws Throwable  {
      int int0 = StringComparator.compare("x,]8K,i%aCY9=$L1/*", "x,]8K,i%aCY9=$L1/*");
      assertEquals(0, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = StringComparator.compare("kW", "");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = StringComparator.compare("", "(*");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = StringComparator.compare(" m&@xQ", "-e_^{|br^hKUVQT?\t");
      assertEquals((-13), int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = StringComparator.compare("RFq#/QZ0`d8", " m&@xQ");
      assertEquals(1, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "kW", (Object) "");
      assertEquals(1, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "a|<", (Object) "a|<");
      assertEquals(0, int0);
  }
}
