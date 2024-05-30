package sfmis_7;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Base64_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("\"(YsW,]|");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character \"
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      String string0 = Base64.byteArrayToBase64(byteArray0);
      assertEquals("AAAAAA==", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = Base64.byteArrayToAltBase64(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = Base64.base64ToByteArray("");
      assertEquals(0, byteArray0.length);
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
        Base64.base64ToByteArray("8|S1");
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
        Base64.altBase64ToByteArray("8;H=");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character H
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("l2i!");
      assertArrayEquals(new byte[] {(byte) (-105), (byte)104, (byte) (-128)}, byteArray0);
  }

  @Test
  public void test11()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = Base64.byteArrayToBase64(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("rg$?>!==");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character $
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test13()  throws Throwable  {
      byte[] byteArray0 = Base64.base64ToByteArray("1XAC1QCGACM=");
      assertArrayEquals(new byte[] {(byte) (-43), (byte)112, (byte)2, (byte) (-43), (byte)0, (byte) (-122), (byte)0, (byte)35}, byteArray0);
      assertEquals(8, byteArray0.length);
  }

  @Test
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[6];
      Base64.main(stringArray0);
      assertEquals(6, stringArray0.length);
  }

  @Test
  public void test15()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("");
      assertEquals(0, byteArray0.length);
  }

  @Test
  public void test16()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("x<]p<G)Z;}4UG<I");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // String length must be a multiple of four.
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test17()  throws Throwable  {
      Base64 base64_0 = new Base64();
  }

  @Test
  public void test18()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      String string0 = Base64.byteArrayToAltBase64(byteArray0);
      assertEquals("!!!!!!!!!!!=", string0);
  }
}
