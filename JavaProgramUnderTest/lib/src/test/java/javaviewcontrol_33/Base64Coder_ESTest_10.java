package javaviewcontrol_33;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Base64Coder_ESTest_10 {

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
      byte[] byteArray0 = new byte[1];
      char[] charArray0 = Base64Coder.encode(byteArray0, (int) (byte) (-1));
      assertEquals(0, charArray0.length);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = Base64Coder.encodeString("");
      assertEquals("", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = Base64Coder.decodeString("");
      assertEquals("", string0);
  }

  @Test
  public void test04()  throws Throwable  {
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
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.encode((byte[]) null, (-151));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
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
  public void test07()  throws Throwable  {
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
  public void test08()  throws Throwable  {
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
  public void test09()  throws Throwable  {
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
  public void test10()  throws Throwable  {
      char[] charArray0 = new char[8];
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
  public void test11()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[0] = 't';
      charArray0[1] = 'R';
      charArray0[2] = 'i';
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
  public void test12()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[0] = 'v';
      charArray0[1] = 'S';
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
      byte[] byteArray0 = new byte[1];
      char[] charArray0 = Base64Coder.encode(byteArray0);
      byte[] byteArray1 = Base64Coder.decode(charArray0);
      assertArrayEquals(new byte[] {(byte)0}, byteArray1);
      assertEquals(4, charArray0.length);
  }

  @Test
  public void test14()  throws Throwable  {
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
  public void test15()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        Base64Coder.encode(byteArray0, (int) (byte)118);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 8
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test16()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      char[] charArray0 = Base64Coder.encode(byteArray0, 1);
      assertArrayEquals(new char[] {'A', 'A', '=', '='}, charArray0);
  }

  @Test
  public void test17()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      char[] charArray0 = Base64Coder.encode(byteArray0, (int) (byte)0);
      assertEquals(0, charArray0.length);
      
      byte[] byteArray1 = Base64Coder.decode(charArray0);
      assertEquals(0, byteArray1.length);
  }

  @Test
  public void test18()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.encode((byte[]) null, 117);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test19()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      char[] charArray0 = Base64Coder.encode(byteArray0);
      assertEquals(8, charArray0.length);
      
      byte[] byteArray1 = Base64Coder.decode(charArray0);
      assertEquals(6, byteArray1.length);
      assertArrayEquals(new char[] {'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'}, charArray0);
  }

  @Test
  public void test20()  throws Throwable  {
      byte[] byteArray0 = Base64Coder.decode("Lg==");
      assertArrayEquals(new byte[] {(byte)46}, byteArray0);
      assertEquals(1, byteArray0.length);
  }

  @Test
  public void test21()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decode("kut&XAWWt+j6");
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
      // Undeclared exception!
      try { 
        Base64Coder.decodeString("J8>=");
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
      charArray0[0] = 'Q';
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
      charArray0[3] = '\u008F';
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
      charArray0[2] = '\u008F';
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
      char[] charArray0 = new char[4];
      charArray0[1] = '\u008F';
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
  public void test27()  throws Throwable  {
      char[] charArray0 = new char[4];
      charArray0[0] = '\u008C';
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
  public void test28()  throws Throwable  {
      byte[] byteArray0 = Base64Coder.decode("");
      char[] charArray0 = Base64Coder.encode(byteArray0);
      assertEquals(0, charArray0.length);
  }

  @Test
  public void test29()  throws Throwable  {
      String string0 = Base64Coder.decodeString("t7N=");
      assertEquals("\uFFFD\uFFFD", string0);
  }

  @Test
  public void test30()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base64Coder.decode("?~`,n YKC2e<!0[");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in Base64 encoded data.
         //
         //verifyException("com.pmdesigns.jvc.tools.Base64Coder", e);
      }
  }

  @Test
  public void test31()  throws Throwable  {
      String string0 = Base64Coder.encodeString("?~`,n YKC2e<!0[");
      assertEquals("fz9+YCxuIFlLQzJlPCEwWw==", string0);
  }
}
