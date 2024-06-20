package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringComparator_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = StringComparator.compare("-(8bm87aR!*<Gh\"0nj^", "Eoqb");
      assertEquals((-82), int0);
  }

  @Test
  public void test01()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "hqs^-E-(0+xyS.", (Object) ":");
      assertEquals(1, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) " Id<0ygod>.bX", (Object) "|009$B2");
      assertEquals((-1), int0);
  }

  @Test
  public void test03()  throws Throwable  {
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
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        stringComparator0.compare(object0, (Object) ":");
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
      int int0 = StringComparator.compare("hqs^-E-(0+xyS.", "hqs^-E-(0+xyS.");
      assertEquals(0, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = StringComparator.compare("", "Eoqb");
      assertEquals((-1), int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = StringComparator.compare("Eoqb", "-(8bm87aR!*<Gh\"0nj^");
      assertEquals(82, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = StringComparator.compare("hqs^-E-(0+xyS.", "bG+(kN");
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = StringComparator.compare("Eoqb", "");
      assertEquals(1, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "hqs^-E-(0+xyS.", (Object) "hqs^-E-(0+xyS.");
      assertEquals(0, int0);
  }
}
