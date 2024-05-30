package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Base64Coder_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decode("~KBc>2A");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test01()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decode("eM6");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Base64Coder.encodeString("");
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      char[] charArray0 = Base64Coder.encode(byteArray0);
      assertEquals(0, charArray0.length);
  }

  @Test
  public void test04()  throws Throwable  {
      String string0 = Base64Coder.decodeString("SEY8Q0RVSG84X248RVkiLw==");
      assertEquals("HF<CDUHo8_n<EY\"/", string0);
  }

  @Test
  public void test05()  throws Throwable  {
      String string0 = Base64Coder.decodeString("");
      assertEquals("", string0);
  }

  @Test
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.encodeString((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.encode((byte[]) null, 15);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.encode((byte[]) null, (-2573));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.encode((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decodeString((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decode((char[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decode((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test13()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[0] = '4';
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test14()  throws Throwable  {
      char[] charArray0 = new char[4];
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[0] = 'n';
      charArray0[1] = 'P';
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test16()  throws Throwable  {
      char[] charArray0 = new char[0];
      byte[] byteArray0 = Base64Coder.decode(charArray0);
      char[] charArray1 = Base64Coder.encode(byteArray0, (-1));
      assertEquals(0, byteArray0.length);
      assertEquals(0, charArray1.length);
  }

  @Test
  public void test17()  throws Throwable  {
      char[] charArray0 = new char[5];
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Length of Base64 encoded input string is not a multiple of 4.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test18()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      // Undeclared exception!
      try { 
        Base64Coder.encode(byteArray0, 48);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 4
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test19()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      char[] charArray0 = Base64Coder.encode(byteArray0, 1);
      assertEquals(4, charArray0.length);
      assertArrayEquals(new char[] {'A', 'A', '=', '='}, charArray0);
  }

  @Test
  public void test20()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      char[] charArray0 = Base64Coder.encode(byteArray0);
      byte[] byteArray1 = Base64Coder.decode(charArray0);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
      assertEquals(7, byteArray1.length);
      assertEquals(12, charArray0.length);
  }

  @Test
  public void test21()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[0] = 'Q';
      charArray0[1] = '6';
      charArray0[2] = 'e';
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test22()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[3] = '\u0088';
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test23()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[2] = '\u0082';
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test24()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[1] = '\u0087';
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test25()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[0] = '\u0087';
      // Undeclared exception!
      try { 
        Base64Coder.decode(charArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test26()  throws Throwable  {
      byte[] byteArray0 = Base64Coder.decode("");
      assertEquals(0, byteArray0.length);
  }

  @Test
  public void test27()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decodeString("FCCQ|P1(Tbz=CQJ%");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test28()  throws Throwable  {
      byte[] byteArray0 = Base64Coder.decode("dzotI1JYZ0B4cmBjaiFtNg==");
      assertEquals(16, byteArray0.length);
  }

  @Test
  public void test29()  throws Throwable  {
      String string0 = Base64Coder.encodeString("w:-#RXg@xr`cj!m6");
      assertEquals("dzotI1JYZ0B4cmBjaiFtNg==", string0);
  }
}
