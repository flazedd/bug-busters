package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.util.function.Function;

public class NaturalSort_ESTest_8 {

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
      int int0 = NaturalSort.compareIgnoreCase("", "[&!K9\"Y@)@69y");
      assertEquals((-1), int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = NaturalSort.compare("2", "corina.util.NaturalSort");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("2", "0");
      assertEquals(1, int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = NaturalSort.compare("0", "8%T+0teaA%H4y$");
      assertEquals((-1), int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("lrXDe0 ", "lrXDe01 ");
      assertEquals((-1), int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compare("0", "0");
      assertEquals(0, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compare("13]6r!H8U&W3j9", "7A`|i");
      assertEquals(1, int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = NaturalSort.compare("72:1c", "7v-,0j#`7J`z");
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = NaturalSort.compare("7A`|i", "13]6r!H8U&W3j9");
      assertEquals((-1), int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("2", "2");
      assertEquals(0, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      Function<Object, Object> function0 = Function.identity();
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        naturalSort_NaturalComparator0.compare(object0, function0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // java.lang.Object cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$NaturalComparator", e);
      }
  }

  @Test
  public void test13()  throws Throwable  {
      NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
      int int0 = naturalSort_NaturalComparator0.compare("", "");
      assertEquals(0, int0);
  }

  @Test
  public void test14()  throws Throwable  {
      NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
      int int0 = naturalSort_CINaturalComparator0.compare("[&!K9\"Y@)@69y", "");
      assertEquals(1, int0);
  }

  @Test
  public void test15()  throws Throwable  {
      int int0 = NaturalSort.compare("`>7vq#_V0ss$YBP }Q", "`>7vq#_V0ss$YBP }Q");
      assertEquals(0, int0);
  }

  @Test
  public void test16()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("LunKPa:j5V`]{$^86 ", "LunKPa:j5V`]{$^86 ");
      assertEquals(0, int0);
  }
}
