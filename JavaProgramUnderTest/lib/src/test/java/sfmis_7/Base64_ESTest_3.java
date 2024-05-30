package sfmis_7;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Base64_ESTest_3 {

  @Test
  public void test00()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("d!==");
      assertArrayEquals(new byte[] {(byte)116}, byteArray0);
  }

  @Test
  public void test01()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.byteArrayToBase64((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test02()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.byteArrayToAltBase64((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test03()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("@6=");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 127
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.altBase64ToByteArray((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.altBase64ToByteArray("\"kA;YP\"?~uMa");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character A
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test07()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      String string0 = Base64.byteArrayToBase64(byteArray0);
      assertEquals("AAAAAAAAAAA=", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      byte[] byteArray0 = Base64.base64ToByteArray("");
      String string0 = Base64.byteArrayToAltBase64(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      byte[] byteArray0 = Base64.base64ToByteArray("AKcaQAC2ADA=");
      assertEquals(8, byteArray0.length);
      assertArrayEquals(new byte[] {(byte)0, (byte) (-89), (byte)26, (byte)64, (byte)0, (byte) (-74), (byte)0, (byte)48}, byteArray0);
  }

  @Test
  public void test10()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("Mhq^2{&>kQHElR*(");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character ^
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("==");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // String length must be a multiple of four.
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test12()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("");
      String string0 = Base64.byteArrayToBase64(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      Base64 base64_0 = new Base64();
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[4];
      Base64.main(stringArray0);
      assertEquals(4, stringArray0.length);
  }

  @Test
  public void test15()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      String string0 = Base64.byteArrayToAltBase64(byteArray0);
      assertEquals("!!==", string0);
  }
}
