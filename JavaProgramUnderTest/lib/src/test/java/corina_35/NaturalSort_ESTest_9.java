package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NaturalSort_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("<(%+", "]NemQ{]qBN:ny%L`Lg(");
      assertEquals((-1), int0);
  }

  @Test
  public void test01()  throws Throwable  {
      // Undeclared exception!
      try { 
        NaturalSort.compareIgnoreCase((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.NaturalSort", e);
      }
  }

  @Test
  public void test02()  throws Throwable  {
      // Undeclared exception!
      try { 
        NaturalSort.compare((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("corina.util.NaturalSort", e);
      }
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = NaturalSort.compare("", "mGd %*He]<A~$?3$x");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("6jS9>?", "");
      assertEquals(1, int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("WJ?;+rR v!tiw!\"jE", "WJ?;+rR v!tiw!\"jE");
      assertEquals(0, int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("ZJ ", "ZJ ");
      assertEquals(0, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("3Isb@i", "0m:y0");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compare("0m:y0", "3Isb@i");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = NaturalSort.compare("019|Y!+<Gy", "0");
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("4%Z:dl'09", "4%Z:dl'09");
      assertEquals(0, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = NaturalSort.compare("29", "4ZQ:dl'w.");
      assertEquals(1, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      int int0 = NaturalSort.compare("8)23xn>Je8)", "29");
      assertEquals((-1), int0);
  }

  @Test
  public void test13()  throws Throwable  {
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        naturalSort_NaturalComparator0.compare(object0, "6yU>E.c8q");
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // java.lang.Object cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$NaturalComparator", e);
      }
  }

  @Test
  public void test14()  throws Throwable  {
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        naturalSort_CINaturalComparator0.compare(object0, object0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // java.lang.Object cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$CINaturalComparator", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      int int0 = NaturalSort.compare("*|l4x3aV0t$qP!O0:29", "*|l4x3aV0t$qP!O0:29");
      assertEquals(0, int0);
  }
}
