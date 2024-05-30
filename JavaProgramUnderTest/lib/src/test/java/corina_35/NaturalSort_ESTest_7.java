package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NaturalSort_ESTest_7 {

  @Test
  public void test00()  throws Throwable  {
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      int int0 = naturalSort_NaturalComparator0.compare("OHET4-|F2V3/", "OHET4-|F2V3/");
      assertEquals(0, int0);
  }

  @Test
  public void test01()  throws Throwable  {
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      int int0 = naturalSort_CINaturalComparator0.compare(" ^$2\b#1>)#b n{", " ^$2\b#1>)#b n{");
      assertEquals(0, int0);
  }

  @Test
  public void test02()  throws Throwable  {
      int int0 = NaturalSort.compare("OHET4-|F2V3/", "");
      assertEquals(1, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = NaturalSort.compare("", "5cG]%OtsiE");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
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
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("", "0`6v;x9>F;K'wb<70fC");
      assertEquals((-1), int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("1dpWx^/_", "x[1k +L Zmg%:");
      assertEquals((-1), int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("- ", "- ");
      assertEquals(0, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("2-", "0");
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("0`6v;x9>F;K'wb<70fC", "70/g} 8");
      assertEquals((-1), int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("0", "0");
      assertEquals(0, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("0", "04cOzq");
      assertEquals((-1), int0);
  }

  @Test
  public void test13()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("7q e)", "3}D7Ch:2SA[D");
      assertEquals(1, int0);
  }

  @Test
  public void test14()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("10", "7q e)");
      assertEquals(1, int0);
  }

  @Test
  public void test15()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("3}D7CKh:42SA[D", "74 e)0");
      assertEquals((-1), int0);
  }

  @Test
  public void test16()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("3", "3");
      assertEquals(0, int0);
  }

  @Test
  public void test17()  throws Throwable  {
      int int0 = NaturalSort.compare(" ^$2\b#1>)#b n{", " ^$2\b#1>)#b n{");
      assertEquals(0, int0);
  }
}
