package schemaspy_36;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Version_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      Version version0 = new Version("5");
      Version version1 = new Version((String) null);
      boolean boolean0 = version1.equals(version0);
      assertFalse(version0.equals((Object)version1));
      assertFalse(boolean0);
  }

  @Test
  public void test01()  throws Throwable  {
      Version version0 = new Version("5");
      Version version1 = new Version("49");
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
      Version version0 = new Version("");
      String string0 = version0.toString();
      assertEquals("", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      Version version0 = null;
      try {
        version0 = new Version("hw9}\"b7/RC]B@`5");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"hw9}\"b7/RC]B@`5\"
         //
         //verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      Version version0 = new Version("5");
      Version version1 = new Version((String) null);
      boolean boolean0 = version0.equals(version1);
      assertFalse(version1.equals((Object)version0));
      assertFalse(boolean0);
  }

  @Test
  public void test06()  throws Throwable  {
      Version version0 = new Version("5");
      Object object0 = new Object();
      boolean boolean0 = version0.equals(object0);
      assertFalse(boolean0);
  }

  @Test
  public void test07()  throws Throwable  {
      Version version0 = new Version("5");
      boolean boolean0 = version0.equals(version0);
      assertTrue(boolean0);
  }

  @Test
  public void test08()  throws Throwable  {
      Version version0 = new Version("5");
      boolean boolean0 = version0.equals((Object) null);
      assertFalse(boolean0);
  }

  @Test
  public void test09()  throws Throwable  {
      Version version0 = new Version("5");
      Version version1 = new Version((String) null);
      int int0 = version0.compareTo(version1);
      assertEquals(1, int0);
      assertFalse(version1.equals((Object)version0));
  }

  @Test
  public void test10()  throws Throwable  {
      Version version0 = new Version("5");
      Version version1 = new Version((String) null);
      int int0 = version1.compareTo(version0);
      assertFalse(version0.equals((Object)version1));
      assertEquals((-1), int0);
  }

  @Test
  public void test11()  throws Throwable  {
      Version version0 = new Version("5");
      Version version1 = new Version("4");
      int int0 = version0.compareTo(version1);
      assertFalse(version1.equals((Object)version0));
      assertEquals(1, int0);
  }

  @Test
  public void test12()  throws Throwable  {
      Version version0 = new Version("5");
      int int0 = version0.compareTo(version0);
      assertEquals(0, int0);
  }

  @Test
  public void test13()  throws Throwable  {
      Version version0 = new Version((String) null);
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
  public void test14()  throws Throwable  {
      Version version0 = new Version("5");
      version0.hashCode();
  }

  @Test
  public void test15()  throws Throwable  {
      Version version0 = new Version("5");
      String string0 = version0.toString();
      assertEquals("5", string0);
  }
}
