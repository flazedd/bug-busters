package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class WildcardSearch_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("em[=`*}XZqq");
      boolean boolean0 = wildcardSearch0.doesMatch("6/uJ J");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch(",%_p");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch(",");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test02()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*J");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test03()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*J");
      boolean boolean0 = wildcardSearch0.doesMatch("R7J }u2<`{}V%HCt+");
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("qf!%Sk:#,zNxF");
      boolean boolean0 = wildcardSearch0.doesMatch("qf!%Sk:#,zNxF");
      assertTrue(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("({eu6vB)r\"?*s8!d");
      boolean boolean0 = wildcardSearch0.doesMatch("-B0>-K");
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*J");
      boolean boolean0 = wildcardSearch0.doesMatch("w");
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("t['*;w)V5V*F'o%-6p");
      boolean boolean0 = wildcardSearch0.doesMatch("t['*;w)V5V*F'o%-6p");
      assertTrue(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*");
      boolean boolean0 = wildcardSearch0.doesMatch("*");
      assertTrue(boolean0);
  }

  @Test
  public void test09()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*J");
      boolean boolean0 = wildcardSearch0.doesMatch("");
      assertFalse(boolean0);
  }

  @Test
  public void test10()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("");
      boolean boolean0 = wildcardSearch0.doesMatch("");
      assertFalse(boolean0);
  }
}
