package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class WildcardSearch_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("h#X7hO8&CLmMQugVZ");
      boolean boolean0 = wildcardSearch0.doesMatch("*");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("hbBB==SBqnVsm]");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch("h");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test02()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch((String) null);
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test03()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*@l.L?>hePIi2@p");
      boolean boolean0 = wildcardSearch0.doesMatch("*@l.L?>hePIi2@p");
      assertTrue(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("(qx#q$O;6tL5@");
      boolean boolean0 = wildcardSearch0.doesMatch("(qx#q$O;6tL5@");
      assertTrue(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("(qx#q$O;6tL5@");
      boolean boolean0 = wildcardSearch0.doesMatch("?Xxb1qU-un+,t");
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*s");
      boolean boolean0 = wildcardSearch0.doesMatch("%&'3");
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("**");
      boolean boolean0 = wildcardSearch0.doesMatch("**");
      assertTrue(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("(qx#q$O;6tL5@");
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
      WildcardSearch wildcardSearch0 = new WildcardSearch("*s");
      boolean boolean0 = wildcardSearch0.doesMatch("{1?r6%~hTs UN");
      assertFalse(boolean0);
  }
}
