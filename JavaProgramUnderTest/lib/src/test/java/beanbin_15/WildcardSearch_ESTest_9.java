package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class WildcardSearch_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("O/#<\"*>HC$V15@s}g");
      boolean boolean0 = wildcardSearch0.doesMatch("*");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("O/#<\"*>HC$V15@s}W");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch("O");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test02()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("O/#<\"*>HC$V15@s}g");
      // Undeclared exception!
      try { 
        wildcardSearch0.doesMatch((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test
  public void test03()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("q");
      boolean boolean0 = wildcardSearch0.doesMatch("q");
      assertTrue(boolean0);
  }

  @Test
  public void test04()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("O/#<\"*>HC$V15@s}g");
      boolean boolean0 = wildcardSearch0.doesMatch("oU^5%B,j4|");
      assertFalse(boolean0);
  }

  @Test
  public void test05()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("O/#<\"*>HC$J15@s}W");
      boolean boolean0 = wildcardSearch0.doesMatch("O/#<\"*>HCJ15@s}");
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      WildcardSearch wildcardSearch0 = new WildcardSearch("*/#<\"*>HC$J15@s}W");
      boolean boolean0 = wildcardSearch0.doesMatch("*/#<\"*>HC$J15@s}W");
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
      WildcardSearch wildcardSearch0 = new WildcardSearch("O/#<\"*>HC$V15@s}W");
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
      WildcardSearch wildcardSearch0 = new WildcardSearch("O/#<\"*>HC$V15@s}");
      boolean boolean0 = wildcardSearch0.doesMatch("O/#<\"*>HC$V15@s}W");
      assertFalse(boolean0);
  }
}
