package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NaturalSort_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      int int0 = NaturalSort.compare("{22S,oqK73->ZUg", " +L& .O}H(h%x\"");
      assertEquals(1, int0);
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
      int int0 = NaturalSort.compare("", "7)~'5g=f{A");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("0^bh/LTje9r*NR&'o ", "");
      assertEquals(1, int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("8O< 2X_Gdp", "8O< 2X_Gdp");
      assertEquals(0, int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("7)~'5g=f{A", "0^bh/LTje9r*NR&'o ");
      assertEquals(1, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compare("0^bh/LTje9r*NR&'o ", "7)~'5g=f{A");
      assertEquals((-1), int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("0P'%@YJp0", "0P'%@YJp0");
      assertEquals(0, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("49{vb,ERNGv", "2^!} 5JR[K]:");
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("2^!} 5JR[K]:", "49{vb,ERNGv");
      assertEquals((-1), int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase(",X$f?d80eN|5", ",X$f?d80eN|5");
      assertEquals(0, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      int int0 = naturalSort_NaturalComparator0.compare("0^bh/LTje9r*NR&'o ", "0^bh/LTje9r*NR&'o ");
      assertEquals(0, int0);
  }

  @Test
  public void test13()  throws Throwable  {
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
  public void test14()  throws Throwable  {
      int int0 = NaturalSort.compare("0^bh/LTje9r*NR&'o ", "0^bh/LTje9r*NR&'o ");
      assertEquals(0, int0);
  }
}
