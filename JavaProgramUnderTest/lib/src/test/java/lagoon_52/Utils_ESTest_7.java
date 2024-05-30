package lagoon_52;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Utils_ESTest_7 {

  @Test
  public void test00()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("$]RurVz");
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL(":b)!=6Z=F@kr&H^giE%");
      assertTrue(boolean0);
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
      Utils.nChars(5465, '$');
      // Undeclared exception!
      Utils.nChars(5465, 'V');
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        Utils.nChars((-2004), 'M');
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
      String string0 = Utils.nChars(2513, '.');
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
      String string0 = Utils.nChars(2513, '.');
      String string1 = Utils.encodePathAsIdentifier(string0);
      // Undeclared exception!
      Utils.encodePath(string1);
  }

  @Test
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
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
  public void test12()  throws Throwable  {
      String string0 = Utils.nChars(0, 'l');
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("/|K;HLXhZIfGo");
      assertTrue(boolean0);
  }

  @Test
  public void test14()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("k:mLb5hdnZVb");
      assertFalse(boolean0);
  }

  @Test
  public void test15()  throws Throwable  {
      boolean boolean0 = Utils.pseudoAbsoluteURL("");
      assertFalse(boolean0);
  }

  @Test
  public void test16()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("/?5u|.y U:7gst");
      assertFalse(boolean0);
  }

  @Test
  public void test17()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("-~\"X7:/_CR");
      assertTrue(boolean0);
  }

  @Test
  public void test18()  throws Throwable  {
      boolean boolean0 = Utils.absoluteURL("{n.Z");
      assertFalse(boolean0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Utils.encodePath(";v~+.S-\"Z}");
      assertEquals(";v~~+.S--\"Z}", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      String string0 = Utils.encodePath("k:mLb5hdnZVb");
      assertEquals("k~mLb5hdnZVb", string0);
  }

  @Test
  public void test21()  throws Throwable  {
      String string0 = Utils.encodePath("/e");
      assertEquals("-e", string0);
  }

  @Test
  public void test22()  throws Throwable  {
      String string0 = Utils.encodePath("Qce*Y9D6(e");
      assertEquals("Qce_Y9D6(e", string0);
  }

  @Test
  public void test23()  throws Throwable  {
      String string0 = Utils.encodePath("0$ztCs3EoXu<");
      assertEquals("0$$ztCs3EoXu<", string0);
  }

  @Test
  public void test24()  throws Throwable  {
      String string0 = Utils.encodePath("jx}Lz=r\"TD4Pw<v?%VT");
      assertEquals("jx}Lz=r\"TD4Pw<v$%VT", string0);
  }
}
