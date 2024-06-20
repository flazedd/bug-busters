package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NaturalSort_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      int int0 = naturalSort_NaturalComparator0.compare("Xh@", "Xh@");
      assertEquals(0, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      int int0 = NaturalSort.compare("9YlP`c:-ATRE!.DqB", "4[D");
      assertEquals(1, int0);
  }

  @Test
  public void test02()  throws Throwable  {
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
  public void test03()  throws Throwable  {
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
  public void test04()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("", " S)5l7}`>");
      assertEquals((-1), int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = NaturalSort.compare("6TZ!a", "qrX]z8H]xEyWw88R1");
      assertEquals((-1), int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compare("O58K]2&.^'\"M7K<Z  ", "O58K]2&.^'\"M7K<Z  ");
      assertEquals(0, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("2F}", "0_P]>s)>FG'uI=M");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("0_P>s)>F'I=M", "2F}");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("K'$2]037 ", "K'$2]0j7 ");
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("l~YT1sjB7f0", "l~YT1sjB7f0");
      assertEquals(0, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("88OC(", "9YlP`c:-ATRE!.DqB");
      assertEquals(1, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("9YlP`c:-ATRE!.DqB", "16");
      assertEquals((-1), int0);
  }

  @Test
  public void test13()  throws Throwable  {
      int int0 = NaturalSort.compare(" Fr:5Ex6", " Fr:5Ex6");
      assertEquals(0, int0);
  }

  @Test
  public void test14()  throws Throwable  {
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      int int0 = naturalSort_CINaturalComparator0.compare("corina.util.NaturalSort", "%ozflf,");
      assertEquals(1, int0);
  }

  @Test
  public void test15()  throws Throwable  {
      int int0 = NaturalSort.compare("K'$2]0j7 ", "K'$2]037 ");
      assertEquals((-1), int0);
  }
}
