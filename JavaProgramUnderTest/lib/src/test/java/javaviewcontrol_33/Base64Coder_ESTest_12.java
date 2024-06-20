package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Base64Coder_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[1] = '';
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
  public void test01()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[0] = '';
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
  public void test02()  throws Throwable  {
      String string0 = Base64Coder.encodeString("");
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = Base64Coder.decodeString("S1MxRlN3PT0=");
      assertEquals("KS1FSw==", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = Base64Coder.decode("KS1FSw==");
      assertArrayEquals(new byte[] {(byte)41, (byte)45, (byte)69, (byte)75}, byteArray0);
      assertEquals(4, byteArray0.length);
  }

  @Test
  public void test05()  throws Throwable  {
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
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.encode((byte[]) null, 1478);
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
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        Base64Coder.encode(byteArray0, (-2573));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
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
  public void test09()  throws Throwable  {
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
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
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
  public void test12()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[0] = 'V';
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
  public void test13()  throws Throwable  {
      char[] charArray0 = new char[8];
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
  public void test14()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      char[] charArray0 = Base64Coder.encode(byteArray0, (int) (byte) (-3));
      assertEquals(0, charArray0.length);
      
      byte[] byteArray1 = Base64Coder.decode(charArray0);
      assertEquals(0, byteArray1.length);
  }

  @Test
  public void test15()  throws Throwable  {
      char[] charArray0 = new char[1];
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
  public void test16()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      char[] charArray0 = Base64Coder.encode(byteArray0, (int) (byte)1);
      assertArrayEquals(new char[] {'A', 'A', '=', '='}, charArray0);
      assertEquals(4, charArray0.length);
  }

  @Test
  public void test17()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      // Undeclared exception!
      try { 
        Base64Coder.encode(byteArray0, 860);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 5
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test18()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[0] = '7';
      charArray0[1] = 'u';
      charArray0[2] = 'v';
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
  public void test19()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[0] = 'a';
      charArray0[1] = 'M';
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
  public void test20()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decodeString("I&G?z?+jGKR\" )2v");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test21()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[3] = '\u0085';
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
      char[] charArray0 = new char[4];
      charArray0[2] = '\u0086';
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
      char[] charArray0 = new char[4];
      charArray0[1] = '\u0086';
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
      // Undeclared exception!
      try { 
        Base64Coder.decode("\uFFFD\u04DE^\u0012");
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
      byte[] byteArray0 = new byte[7];
      char[] charArray0 = Base64Coder.encode(byteArray0);
      byte[] byteArray1 = Base64Coder.decode(charArray0);
      assertEquals(12, charArray0.length);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
  }

  @Test
  public void test26()  throws Throwable  {
      String string0 = Base64Coder.decodeString("");
      assertEquals("", string0);
  }

  @Test
  public void test27()  throws Throwable  {
      byte[] byteArray0 = Base64Coder.decode("");
      char[] charArray0 = Base64Coder.encode(byteArray0);
      assertEquals(0, charArray0.length);
  }

  @Test
  public void test28()  throws Throwable  {
      String string0 = Base64Coder.encodeString(")-EK");
      assertEquals("KS1FSw==", string0);
  }
}
