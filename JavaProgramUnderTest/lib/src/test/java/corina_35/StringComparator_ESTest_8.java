package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringComparator_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = StringComparator.compare(" zC_D}!D", "8B");
      assertEquals((-95), int0);
  }

  @Test
  public void test01()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "+te:.9|Vz", (Object) "+te:.9|Vz");
      assertEquals(0, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "xO9n}a|>", (Object) "Me");
      assertEquals(1, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "bxMfn- H@NUn", (Object) "Me");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringComparator.compare("]e+f*7^U78D@e#P(|", (String) null);
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
        stringComparator0.compare((Object) "#'v@;@`c_izQmCc", (Object) null);
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
      int int0 = StringComparator.compare("", "corina.util.StringComparator");
      assertEquals((-1), int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = StringComparator.compare("corina.util.StringCmparator", "corina.util.StringCmparator");
      assertEquals(0, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = StringComparator.compare("H]%Ez?CX<04.9$'", " {Z='Yzx1@k;");
      assertEquals(1, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = StringComparator.compare(" 4Ugd", " {Z='Yzx1@k;");
      assertEquals(95, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = StringComparator.compare("71#:}UR", "");
      assertEquals(1, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        stringComparator0.compare((Object) "I6`<0h*", object0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // java.lang.Object cannot be cast to java.lang.String
         //
         //verifyException("corina.util.StringComparator", e);
      }
  }
}
