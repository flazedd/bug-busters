package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class WildcardSearch_ESTest_6 {

  @Test
  public void test00()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("5q,iGV{E");
      boolean boolean0 = wildcardSearch0.doesMatch("*");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("lSRwVZZ.fkjtt");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch("l");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test02()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*$4:M");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test03()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*$4:M");
      boolean boolean0 = wildcardSearch0.doesMatch("*$4:Mb");
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("5q,iGV{E");
      boolean boolean0 = wildcardSearch0.doesMatch("5q,iGV{E");
      assertTrue(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("&H0IvNT->XAh$d*Spz-");
      boolean boolean0 = wildcardSearch0.doesMatch("_57%QoAI.RopNo{c^x");
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*T&z4:Mb");
      boolean boolean0 = wildcardSearch0.doesMatch("*\"aPqbT6%v01r&FhJ`");
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("5@TPA**");
      boolean boolean0 = wildcardSearch0.doesMatch("5@TPA**");
      assertTrue(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("&H0IvNT->XAh$d*Spz-");
      boolean boolean0 = wildcardSearch0.doesMatch("");
      assertFalse(boolean0);
  }

  @Test
  public void test09()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("");
      boolean boolean0 = wildcardSearch0.doesMatch("");
      assertFalse(boolean0);
  }

  @Test
  public void test10()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*$4:M");
      boolean boolean0 = wildcardSearch0.doesMatch("*$4:M");
      assertTrue(boolean0);
  }
}
