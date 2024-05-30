package corina_35;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NaturalSort_ESTest_6 {

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
      int int0 = NaturalSort.compare("7", "5w$%(;X`Ol /!h");
      assertEquals(1, int0);
  }

  @Test
  public void test03()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("", "BN#Cx<_4IVlY4");
      assertEquals((-1), int0);
  }

  @Test
  public void test04()  throws Throwable  {
      int int0 = NaturalSort.compare("6r/xuCcg}Rh9\"o7\"K", "BN#Cx<_4IVlY4");
      assertEquals((-1), int0);
  }

  @Test
  public void test05()  throws Throwable  {
      int int0 = NaturalSort.compare(" ", " ");
      assertEquals(0, int0);
  }

  @Test
  public void test06()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("5w$%(;X`Ol /!h", "5w$%(;X`Ol /!h");
      assertEquals(0, int0);
  }

  @Test
  public void test07()  throws Throwable  {
      int int0 = NaturalSort.compare("5w$%(;X`Ol /!h", "0@gKP1:NF&e~]jI'");
      assertEquals(1, int0);
  }

  @Test
  public void test08()  throws Throwable  {
      int int0 = NaturalSort.compare("0@gKP1:NF&e~]jI'", "1b+vkuy7");
      assertEquals((-1), int0);
  }

  @Test
  public void test09()  throws Throwable  {
      int int0 = NaturalSort.compare("050", "0,|t+kVpr4 n|t{I(");
      assertEquals(1, int0);
  }

  @Test
  public void test10()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("0@gP1:F&@i", "05Rxo9^iRDnW:");
      assertEquals((-1), int0);
  }

  @Test
  public void test11()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("36e?UR4#T_2O%3", "9}_I7Q`?@a:i??vAZ");
      assertEquals(1, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      int int0 = NaturalSort.compare("6.6R*9;2d[3q!#g)", "57$2[Z05G");
      assertEquals((-1), int0);
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
      Integer integer0 = new Integer(1);
      // Undeclared exception!
      try { 
        naturalSort_CINaturalComparator0.compare(integer0, "");
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // java.lang.Integer cannot be cast to java.lang.String
         //
         //verifyException("corina.util.NaturalSort$CINaturalComparator", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      int int0 = NaturalSort.compare("Xsz\u0006[0jb", "Xsz\u0006[0jb");
      assertEquals(0, int0);
  }

  @Test
  public void test16()  throws Throwable  {
      int int0 = NaturalSort.compareIgnoreCase("1Om0vYL.KME50", "1Om0vYL.KME50");
      assertEquals(0, int0);
  }
}
