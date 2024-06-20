package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringComparator_ESTest_10 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = StringComparator.compare("", "-D<|XB|an9");
      assertEquals(82, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = StringComparator.compare("67JhMpm0OeK%<^{=sr", ");@IyZZj|R Ct");
      assertEquals(1, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "\"F`)b1iN=wr}19;", (Object) "\"F`)b1iN=wr}19;");
      assertEquals(0, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "", (Object) "?7x.\"pM");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
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
  public void test06()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      // Undeclared exception!
      try { 
        stringComparator0.compare((Object) stringComparator0, (Object) "}`)yf%kM]/v");
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // corina.util.StringComparator cannot be cast to java.lang.String
         //
         //verifyException("corina.util.StringComparator", e);
      }
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = StringComparator.compare("Sz:|)O", "");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = StringComparator.compare("", "}`)yf%kM]/v");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = StringComparator.compare("-z`- CVx[\"1thI", "m/fg%_+Xp_{@~:");
      assertEquals((-82), int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = StringComparator.compare("m/fg%_+Xp_{@~:", ");@IyZZj|R Ct");
      assertEquals((-1), int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = StringComparator.compare("4xr", "4xr");
      assertEquals(0, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      StringComparator stringComparator0 = new StringComparator();
      int int0 = stringComparator0.compare((Object) "4xr", (Object) "");
      assertEquals(1, int0);
  }
}
