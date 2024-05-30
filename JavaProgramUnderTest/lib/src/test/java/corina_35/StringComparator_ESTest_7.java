package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringComparator_ESTest_7 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = StringComparator.compare("", " JZvVB+={$;");
      assertEquals(95, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = StringComparator.compare("#T[j>EEa,Ct", "NQlDG}ov");
      assertEquals((-1), int0);
  }

  @Test
  public void test02()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "", (Object) "");
      assertEquals(0, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "", (Object) "NQlDG}ov");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      // Undeclared exception!
      try { 
        stringComparator0.compare((Object) null, (Object) "tu@+/^]p;CI{PdA[clU");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.StringComparator", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
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
  public void test07()  throws Throwable  {
      int int0 = StringComparator.compare("Y%-h]Xe,\"gTn_edm", "E@((");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = StringComparator.compare("", "corina.util.StringComparator");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = StringComparator.compare(" JZvVB+={$;", "");
      assertEquals((-95), int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = StringComparator.compare(";:%", "");
      assertEquals(1, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = StringComparator.compare("corina.util.StringComparator", "corina.util.StringComparator");
      assertEquals(0, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "E@((", (Object) "<|tYqJNd");
      assertEquals(1, int0);
  }
}
