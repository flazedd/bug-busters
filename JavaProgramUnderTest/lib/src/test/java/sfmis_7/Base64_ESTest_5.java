package sfmis_7;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Base64_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("Y,Pg[43iH:80");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character ,
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("");
      String string0 = Base64.byteArrayToBase64(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = Base64.base64ToByteArray("");
      assertEquals(0, byteArray0.length);
  }

  @Test
  public void test03()  throws Throwable  {
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
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
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
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("8GP6<W7BaO");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // String length must be a multiple of four.
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.base64ToByteArray("a7{#2<PueeAK<YQ");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 123
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
        Base64.altBase64ToByteArray("<tT");
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
      byte[] byteArray0 = new byte[4];
      String string0 = Base64.byteArrayToBase64(byteArray0);
      assertEquals("AAAAAA==", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      byte[] byteArray0 = Base64.base64ToByteArray("fwDq3Q==");
      assertEquals(4, byteArray0.length);
      assertArrayEquals(new byte[] {(byte)127, (byte)0, (byte) (-22), (byte) (-35)}, byteArray0);
  }

  @Test
  public void test12()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      String string0 = Base64.byteArrayToAltBase64(byteArray0);
      assertEquals("!!!!!!!=", string0);
  }

  @Test
  public void test13()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("}e0=");
      assertArrayEquals(new byte[] {(byte)97, (byte) (-19)}, byteArray0);
  }

  @Test
  public void test14()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64.altBase64ToByteArray("}+!1ZxA@yw9Ww91n");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character Z
         //
         //verifyException("com.hf.sfm.crypt.Base64", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      byte[] byteArray0 = Base64.altBase64ToByteArray("");
      String string0 = Base64.byteArrayToAltBase64(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test16()  throws Throwable  {
      Base64 base64_0 = new Base64();
  }

  @Test
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[0];
      Base64.main(stringArray0);
      assertEquals(0, stringArray0.length);
  }
}
