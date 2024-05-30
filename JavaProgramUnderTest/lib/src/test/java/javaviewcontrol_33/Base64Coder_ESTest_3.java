package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Base64Coder_ESTest_3 {

  @Test
  public void test00()  throws Throwable  {
      char[] charArray0 = new char[4];
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
      byte[] byteArray0 = new byte[7];
      char[] charArray0 = Base64Coder.encode(byteArray0, (int) (byte) (-1));
      assertEquals(0, charArray0.length);
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      char[] charArray0 = Base64Coder.encode(byteArray0);
      assertEquals(0, charArray0.length);
  }

  @Test
  public void test05()  throws Throwable  {
      byte[] byteArray0 = Base64Coder.decode("");
      assertEquals(0, byteArray0.length);
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
        Base64Coder.encode((byte[]) null, 344);
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
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        Base64Coder.encode(byteArray0, (-544));
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
        Base64Coder.decodeString("/1}u");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test12()  throws Throwable  {
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
  public void test13()  throws Throwable  {
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
  public void test14()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      char[] charArray0 = Base64Coder.encode(byteArray0);
      byte[] byteArray1 = Base64Coder.decode(charArray0);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
      assertEquals(12, charArray0.length);
  }

  @Test
  public void test15()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[0] = 'T';
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
      assertEquals(0, byteArray0.length);
  }

  @Test
  public void test17()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      // Undeclared exception!
      try { 
        Base64Coder.encode(byteArray0, 122);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 6
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test18()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      char[] charArray0 = Base64Coder.encode(byteArray0, 1);
      assertArrayEquals(new char[] {'A', 'A', '=', '='}, charArray0);
  }

  @Test
  public void test19()  throws Throwable  {
      String string0 = Base64Coder.decodeString("8zsP");
      assertEquals("\uFFFD;\u000F", string0);
  }

  @Test
  public void test20()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[0] = 'k';
      charArray0[1] = 'l';
      charArray0[2] = '4';
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
  public void test21()  throws Throwable  {
      char[] charArray0 = new char[8];
      charArray0[0] = 'G';
      charArray0[1] = 'y';
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
      charArray0[3] = '\u008A';
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
      charArray0[2] = '\u0085';
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
      charArray0[1] = '\u0092';
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
      charArray0[0] = '\u0082';
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
      // Undeclared exception!
      try { 
        Base64Coder.decode("J@M\"");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test27()  throws Throwable  {
      byte[] byteArray0 = Base64Coder.decode("Y3B=");
      assertArrayEquals(new byte[] {(byte)99, (byte)112}, byteArray0);
      assertEquals(2, byteArray0.length);
  }

  @Test
  public void test28()  throws Throwable  {
      char[] charArray0 = new char[7];
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
  public void test29()  throws Throwable  {
      String string0 = Base64Coder.decodeString("");
      assertEquals("", string0);
  }

  @Test
  public void test30()  throws Throwable  {
      String string0 = Base64Coder.encodeString("8z(^");
      assertEquals("OHooXg==", string0);
  }
}
