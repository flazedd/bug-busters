package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NaturalSort_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
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
  public void test01()  throws Throwable  {
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
  public void test02()  throws Throwable  {
      int int0 = NaturalSort.compare("", "}");
      assertEquals((-1), int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("6?2Hs>~", "");
      assertEquals(1, int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = NaturalSort.compare("u ", "u ");
      assertEquals(0, int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("6?2Hs>~", "0V#^0aBR\"");
      assertEquals(1, int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compare("0", "7-");
      assertEquals((-1), int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compare("0", "0");
      assertEquals(0, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("0", "06W^ aBR\"");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = NaturalSort.compare("7-", "96:0E+K(&O~Tzz");
      assertEquals((-1), int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("/7 6 nQs5", "/7 6 nQs5");
      assertEquals(0, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        naturalSort_NaturalComparator0.compare(naturalSort_CINaturalComparator0, object0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // corina.util.NaturalSort$CINaturalComparator cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$NaturalComparator", e);
      }
  }

  @Test
  public void test12()  throws Throwable  {
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        naturalSort_CINaturalComparator0.compare("", object0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // java.lang.Object cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$CINaturalComparator", e);
      }
  }

  @Test
  public void test13()  throws Throwable  {
      int int0 = NaturalSort.compare("96:0E+K(&O~Tzz", "6?2Hs>~");
      assertEquals(1, int0);
  }
}
