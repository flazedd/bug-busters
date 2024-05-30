package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("--");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/}TOpF4kr/:%z\f%");
      assertFalse(boolean0);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Utils.encodePath("");
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
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
  public void test04()  throws Throwable  {
      Utils.nChars(5138, 'R');
      // Undeclared exception!
      Utils.nChars(5138, 'R');
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-54), '3');
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      String string0 = Utils.nChars(5421, 'r');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePathAsIdentifier(string1);
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier("");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.encodePathAsIdentifier((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test
  public void test09()  throws Throwable  {
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
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
      String string0 = Utils.encodePath("f }#Y02cAwCxX;%");
      assertEquals("f }#Y02cAwCxX;%", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      String string0 = Utils.nChars(5420, 'r');
      Utils.encodePath(string0);
      // Undeclared exception!
      Utils.encodePath(string0);
  }

  @Test
  public void test13()  throws Throwable  {
      String string0 = Utils.nChars(0, 'T');
      assertEquals("", string0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("T?gl`Dq AjZJO1fxyap");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("/U");
      assertTrue(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("Z/ M8:ELiQ");
      assertFalse(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":");
      assertTrue(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("T$gl`Dq AjZJO1fxyap");
      assertFalse(boolean0);
  }

  @Test
  public void test20()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("IyriI>#wq:[IO%C7o/");
      assertTrue(boolean0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePathAsIdentifier("nbx:Lz-9d!xx=^4`A");
      assertEquals("nbx_58_Lz_45_9d_33_xx_61__94_4_96_A", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePathAsIdentifier("5");
      assertEquals("_53_", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath(";1}@#~:?/:r{");
      assertEquals(";1}@#~~~$-~r{", string0);
  }

  @Test
  public void test24()  throws Throwable  {
      String string0 = Utils.encodePath("yjS={E&'oE<[v_?;");
      assertEquals("yjS={E&'oE<[v__$;", string0);
  }

  @Test
  public void test25()  throws Throwable  {
      String string0 = Utils.encodePath("d@`6?$ S:JBbX");
      assertEquals("d@`6$$$ S~JBbX", string0);
  }

  @Test
  public void test26()  throws Throwable  {
      String string0 = Utils.encodePath("of-:n3Csp05XEdxd/x1");
      assertEquals("of--~n3Csp05XEdxd-x1", string0);
  }

  @Test
  public void test27()  throws Throwable  {
      String string0 = Utils.encodePath("Jm`Yl*p");
      assertEquals("Jm`Yl_p", string0);
  }
}
