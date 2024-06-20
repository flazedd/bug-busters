package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class WildcardSearch_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("8S8Jj^*@' d]w?v=9");
      boolean boolean0 = wildcardSearch0.doesMatch("net.sourceforge.beanbin.search.WildcardSearch");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("2xY");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch("2");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test02()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("$.R(a *");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test03()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*I");
      boolean boolean0 = wildcardSearch0.doesMatch("^vauqSUx~I,Xxu,L");
      assertFalse(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("'");
      boolean boolean0 = wildcardSearch0.doesMatch("'");
      assertTrue(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("rX");
      boolean boolean0 = wildcardSearch0.doesMatch("T)k2m");
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*I");
      boolean boolean0 = wildcardSearch0.doesMatch("rX");
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*',1*w)QqN");
      boolean boolean0 = wildcardSearch0.doesMatch("*',1*w)QqN");
      assertTrue(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*");
      boolean boolean0 = wildcardSearch0.doesMatch("OI++>G\"zP)<Gh/");
      assertTrue(boolean0);
  }

  @Test
  public void test09()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("C<hW~");
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
