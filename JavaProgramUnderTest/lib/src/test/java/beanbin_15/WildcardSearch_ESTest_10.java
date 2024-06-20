package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class WildcardSearch_ESTest_10 {

  @Test
  public void test0()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("~**");
      boolean boolean0 = wildcardSearch0.doesMatch("*");
      assertFalse(boolean0);
  }

  @Test
  public void test1()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch((String) null);
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test2()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("p");
      boolean boolean0 = wildcardSearch0.doesMatch("p");
      assertTrue(boolean0);
  }

  @Test
  public void test3()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("!:e`v[K#i.e0B*p");
      boolean boolean0 = wildcardSearch0.doesMatch("(A:i.sk");
      assertFalse(boolean0);
  }

  @Test
  public void test4()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("!:e`v[K#i.e0B*p");
      boolean boolean0 = wildcardSearch0.doesMatch("!:e`v[K#i.e0B*p");
      assertTrue(boolean0);
  }

  @Test
  public void test5()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*");
      boolean boolean0 = wildcardSearch0.doesMatch(",p_[%(S]");
      assertTrue(boolean0);
  }

  @Test
  public void test6()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("p");
      boolean boolean0 = wildcardSearch0.doesMatch("");
      assertFalse(boolean0);
  }

  @Test
  public void test7()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("");
      boolean boolean0 = wildcardSearch0.doesMatch("");
      assertFalse(boolean0);
  }

  @Test
  public void test8()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("-tG**`^Q %;*d");
      boolean boolean0 = wildcardSearch0.doesMatch("-tG**`^Q %;*d");
      assertTrue(boolean0);
  }
}
