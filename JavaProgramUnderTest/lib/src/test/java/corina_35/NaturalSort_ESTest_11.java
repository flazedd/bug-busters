package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NaturalSort_ESTest_11 {

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
      int int0 = NaturalSort.compare("5ah 1@snSr", "2_qFmF>&bIVCjSn7:");
      assertEquals(1, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = NaturalSort.compare("", "qU~ZI*5");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = NaturalSort.compare("3v3t{~", "Q)qJ");
      assertEquals((-1), int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = NaturalSort.compare("%wUd5 lc1H^,2Q ", "%wUd5 lc1H^,2Q ");
      assertEquals(0, int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("5ah 1@snr", "0mDd");
      assertEquals(1, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compare("0O{:~]i;W1LJ&", "6oB=U12%V");
      assertEquals((-1), int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("09C$fao3", "0mG");
      assertEquals(1, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = NaturalSort.compare("0mG", "09C$fao3");
      assertEquals((-1), int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("78-mf", "5ah 1@snr");
      assertEquals(1, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("5ah 1@snr", "78-mf");
      assertEquals((-1), int0);
  }

  @Test
  public void test12()  throws Throwable  {
      int int0 = NaturalSort.compare("(u5cSl[5{UfT?Biq-`6", "(u5cSl[5{UfT?Biq-`6");
      assertEquals(0, int0);
  }

  @Test
  public void test13()  throws Throwable  {
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      // Undeclared exception!
      try { 
        naturalSort_NaturalComparator0.compare(naturalSort_CINaturalComparator0, "J/p$$bWE 7u&D");
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // corina.util.NaturalSort$CINaturalComparator cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$NaturalComparator", e);
      }
  }

  @Test
  public void test14()  throws Throwable  {
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      // Undeclared exception!
      try { 
        naturalSort_CINaturalComparator0.compare("J4JM!!", naturalSort_NaturalComparator0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // corina.util.NaturalSort$NaturalComparator cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$CINaturalComparator", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      int int0 = naturalSort_CINaturalComparator0.compare("", "qU~ZI*5");
      assertEquals((-1), int0);
  }

  @Test
  public void test16()  throws Throwable  {
      int int0 = NaturalSort.compare("f.fGd(PsHAO5$!H0", "f.fGd(PsHAO5$!H0");
      assertEquals(0, int0);
  }

  @Test
  public void test17()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("J4JM!!", "J4JM!!");
      assertEquals(0, int0);
  }
}
