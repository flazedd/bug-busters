package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringComparator_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = StringComparator.compare(" l_ql}uPB:E5Wz?", "-9wbo0cAFDY0jLi.P");
      assertEquals((-13), int0);
  }

  @Test
  public void test01()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) ".yQ5'#>", (Object) ".yQ5'#>");
      assertEquals(0, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringComparator.compare("-x~6SBOK~WO", (String) null);
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
        stringComparator0.compare((Object) "", object0);
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
      int int0 = StringComparator.compare("1.lp`6", ".yQ5'#>");
      assertEquals(1, int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = StringComparator.compare("corina.util.StringComparator", "");
      assertEquals(1, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = StringComparator.compare("", "5u<l(a");
      assertEquals((-1), int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = StringComparator.compare("-x~6SBOK~WO", " E");
      assertEquals(95, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "-x~6SBOK~WO", (Object) "");
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = StringComparator.compare("-x~6SBOK~WO", "-x~6SBOK~WO");
      assertEquals(0, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "-x~6SBOK~WO", (Object) "74{Eo_");
      assertEquals((-1), int0);
  }
}
