package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class WildcardSearch_ESTest_7 {

  @Test
  public void test0()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("]L#$j$(4b7\"I*o*P:\"");
      boolean boolean0 = wildcardSearch0.doesMatch("4l:1S6_!5^-");
      assertFalse(boolean0);
  }

  @Test
  public void test1()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("6 {~'[^4q h");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch("6");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test2()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch((String) null);
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test3()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("<fJuM&]=0N");
      boolean boolean0 = wildcardSearch0.doesMatch("<fJuM&]=0N");
      assertTrue(boolean0);
  }

  @Test
  public void test4()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("]L#$j$(4b7\"I*o*P:\"");
      boolean boolean0 = wildcardSearch0.doesMatch("rbD9\"=FSNY8kz/5)`(");
      assertFalse(boolean0);
  }

  @Test
  public void test5()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*eo`okERK7Q");
      boolean boolean0 = wildcardSearch0.doesMatch("IE");
      assertFalse(boolean0);
  }

  @Test
  public void test6()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*a|D_*E4R9");
      boolean boolean0 = wildcardSearch0.doesMatch("*a|D_*E4R9");
      assertTrue(boolean0);
  }

  @Test
  public void test7()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*");
      boolean boolean0 = wildcardSearch0.doesMatch("*");
      assertTrue(boolean0);
  }

  @Test
  public void test8()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("]L#$j$(4b7\"I*o*P:\"");
      boolean boolean0 = wildcardSearch0.doesMatch("");
      assertFalse(boolean0);
  }

  @Test
  public void test9()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("");
      boolean boolean0 = wildcardSearch0.doesMatch("");
      assertFalse(boolean0);
  }
}
