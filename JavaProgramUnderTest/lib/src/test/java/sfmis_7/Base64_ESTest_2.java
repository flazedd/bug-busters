package sfmis_7;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Base64_ESTest_2 {

  @Test
  public void test00()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.altBase64ToByteArray("aAsV/t+B`u#=");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character A
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test01()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.altBase64ToByteArray(")HZozX= ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character H
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("");
      String string0 = Base64.byteArrayToBase64(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("");
      String string0 = Base64.byteArrayToAltBase64(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
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
  public void test06()  throws Throwable  {
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
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("G|h{");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 124
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
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
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.altBase64ToByteArray("ex2k}fv");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 127
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      String string0 = Base64.byteArrayToBase64(byteArray0);
      assertEquals("AAAAAAAAAAA=", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      String string0 = Base64.byteArrayToAltBase64(byteArray0);
      assertEquals("!!!!", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      byte[] byteArray0 = Base64.base64ToByteArray("4tHi");
      assertArrayEquals(new byte[] {(byte) (-30), (byte) (-47), (byte) (-30)}, byteArray0);
  }

  @Test
  public void test13()  throws Throwable  {
      byte[] byteArray0 = Base64.base64ToByteArray("");
      assertEquals(0, byteArray0.length);
  }

  @Test
  public void test14()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("xOmoIGh");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // String length must be a multiple of four.
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("~f8n!%g^b'o=");
      assertEquals(8, byteArray0.length);
      assertArrayEquals(new byte[] {(byte)101, (byte) (-1), (byte)39, (byte)0, (byte)72, (byte)19, (byte)108, (byte)106}, byteArray0);
  }

  @Test
  public void test16()  throws Throwable  {
      Base64 base64_0 = new Base64();
  }

  @Test
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[9];
      Base64.main(stringArray0);
      assertEquals(9, stringArray0.length);
  }
}
