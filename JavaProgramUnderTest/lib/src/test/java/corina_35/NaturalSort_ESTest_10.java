package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NaturalSort_ESTest_10 {

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
      int int0 = NaturalSort.compare("1Ub,nu{}:5PWt+e\"", "$Cj%uewlrMo\niydT|D");
      assertEquals(1, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("s\"' KCA7 F ", "s\"' KCA7 F ");
      assertEquals(0, int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("807%!JO", "0>Q~");
      assertEquals(1, int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("07]t!aPJw", "1");
      assertEquals((-1), int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compare("zd=FQG+l0", "zd=FQG+l0");
      assertEquals(0, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compare("41", "7z5?w");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compare("7z5jw", "26My2 kw");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      int int0 = naturalSort_NaturalComparator0.compare("D}}6WT[`-Q^TE10YJm", "D}}6WT[`-Q^TE10YJm");
      assertEquals(0, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      // Undeclared exception!
      try { 
        naturalSort_CINaturalComparator0.compare(naturalSort_NaturalComparator0, naturalSort_NaturalComparator0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // corina.util.NaturalSort$NaturalComparator cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$CINaturalComparator", e);
      }
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = NaturalSort.compare("K~&f(wsWlqa)w:-06~67", "K~&f(wsWlqa)w:-06~67");
      assertEquals(0, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("", "+R$eN4[7M$i");
      assertEquals((-1), int0);
  }
}
