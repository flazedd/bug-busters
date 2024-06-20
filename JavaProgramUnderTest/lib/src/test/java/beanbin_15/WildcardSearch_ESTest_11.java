package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class WildcardSearch_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("W,tVxbm,.|FqXv)*");
      boolean boolean0 = wildcardSearch0.doesMatch("=IEDoo-U}; \"hxF");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("GK?CTi");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch("G");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test02()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*a");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test03()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("r0w&EN;7Etfn+");
      boolean boolean0 = wildcardSearch0.doesMatch("r0w&EN;7Etfn+");
      assertTrue(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("GL");
      boolean boolean0 = wildcardSearch0.doesMatch("net.sourceforge.beanbin.search.WildcardSearch");
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*a");
      boolean boolean0 = wildcardSearch0.doesMatch("*oIr*8CSjp");
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*oIr*80BCSjp");
      boolean boolean0 = wildcardSearch0.doesMatch("*oIr*80BCSjp");
      assertTrue(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*");
      boolean boolean0 = wildcardSearch0.doesMatch("*");
      assertTrue(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*oIr*8CSjp");
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
      WildcardSearch wildcardSearch0 = new WildcardSearch("*a");
      boolean boolean0 = wildcardSearch0.doesMatch("nAgi)]aFJLr3cySGkF4");
      assertFalse(boolean0);
  }
}
