package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("!n$");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":3O&");
      assertTrue(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Utils.nChars(0, '(');
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = Utils.encodePath("");
      assertEquals("", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.pseudoAbsoluteURL((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      Utils.nChars(3379, 'L');
      Utils.nChars(3379, 'L');
      // Undeclared exception!
      Utils.nChars(3379, 'L');
  }

  @Test
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-669), '?');
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test
  public void test07()  throws Throwable  {
      String string0 = Utils.nChars(5261, 'C');
      Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePathAsIdentifier(string0);
  }

  @Test
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier("");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      String string0 = Utils.nChars(3379, 'L');
      String string1 = Utils.encodePath(string0);
      Utils.encodePath(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePath((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.absoluteURL((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("nu.staldal.util.Utils", e);
      }
  }

  @Test
  public void test13()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("/&D&5!((gv6GPZ5");
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("__");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/`:Hr@IFJ;&T<$;'E");
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("v4@7nZU:/c`l");
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("_94_Re_93_W53l_46_K7Qi_94_");
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePathAsIdentifier("Kcf]C*Cw|vgz");
      assertEquals("Kcf_93_C_42_Cw_124_vgz", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePathAsIdentifier("^Re]W53l.K7Qi^");
      assertEquals("_94_Re_93_W53l_46_K7Qi_94_", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("hp~hf'Hnt");
      assertEquals("hp~~hf'Hnt", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("__");
      assertEquals("____", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath(":UmkqcK?R4#jJRZ");
      assertEquals("~UmkqcK$R4#jJRZ", string0);
  }

  @Test
  public void test24()  throws Throwable  {
      String string0 = Utils.encodePath("jcpW-qY9zVpg*habV");
      assertEquals("jcpW--qY9zVpg_habV", string0);
  }

  @Test
  public void test25()  throws Throwable  {
      String string0 = Utils.encodePath("*LNZwgo`/W5q#9$;*Qv");
      assertEquals("_LNZwgo`-W5q#9$$;_Qv", string0);
  }
}
