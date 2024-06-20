package schemaspy_36;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Version_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      Version version0 = new Version((String) null);
      Version version1 = new Version("0");
      boolean boolean0 = version1.equals(version0);
      assertFalse(boolean0);
      assertFalse(version0.equals((Object)version1));
  }

  @Test
  public void test01()  throws Throwable  {
      Version version0 = new Version("0");
      Version version1 = new Version(". 3_");
      int int0 = version0.compareTo(version1);
      assertEquals((-1), int0);
      assertFalse(version1.equals((Object)version0));
  }

  @Test
  public void test02()  throws Throwable  {
      Version version0 = new Version((String) null);
      String string0 = version0.toString();
      assertNull(string0);
  }

  @Test
  public void test03()  throws Throwable  {
      Version version0 = new Version(". -_");
      String string0 = version0.toString();
      assertEquals(". -_", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      Version version0 = new Version("");
      // Undeclared exception!
      try { 
        version0.compareTo((Version) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("net.sourceforge.schemaspy.util.Version", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      Version version0 = null;
      try {
        version0 = new Version("1.8u");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"8u\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      Version version0 = new Version((String) null);
      Version version1 = new Version("0");
      boolean boolean0 = version0.equals(version1);
      assertFalse(boolean0);
      assertFalse(version1.equals((Object)version0));
  }

  @Test
  public void test07()  throws Throwable  {
      Version version0 = new Version((String) null);
      boolean boolean0 = version0.equals(version0);
      assertTrue(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      Version version0 = new Version("0");
      boolean boolean0 = version0.equals("");
      assertFalse(boolean0);
  }

  @Test
  public void test09()  throws Throwable  {
      Version version0 = new Version((String) null);
      boolean boolean0 = version0.equals((Object) null);
      assertFalse(boolean0);
  }

  @Test
  public void test10()  throws Throwable  {
      Version version0 = new Version("0");
      Version version1 = new Version((String) null);
      int int0 = version0.compareTo(version1);
      assertFalse(version1.equals((Object)version0));
      assertEquals(1, int0);
  }

  @Test
  public void test11()  throws Throwable  {
      Version version0 = new Version("0");
      int int0 = version0.compareTo(version0);
      assertEquals(0, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      Version version0 = new Version(". 8-_");
      Version version1 = new Version("0");
      int int0 = version0.compareTo(version1);
      assertFalse(version1.equals((Object)version0));
      assertEquals(1, int0);
  }

  @Test
  public void test13()  throws Throwable  {
      Version version0 = new Version((String) null);
      Version version1 = new Version("0");
      int int0 = version0.compareTo(version1);
      assertEquals((-1), int0);
      assertFalse(version1.equals((Object)version0));
  }

  @Test
  public void test14()  throws Throwable  {
      Version version0 = new Version("");
      version0.hashCode();
  }

  @Test
  public void test15()  throws Throwable  {
      Version version0 = new Version("");
      String string0 = version0.toString();
      assertEquals("", string0);
  }
}
