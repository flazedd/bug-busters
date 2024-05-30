package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
import java.nio.CharBuffer;

public class StringEncoder64_ESTest_6 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("&n&V9shC{FtY");
      assertEquals("Jm4mVjlzaEN7RnRZ", string0);
      assertNotNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[1] = (byte) (-105);
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 0, 2743);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 6
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[0] = (byte)32;
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 0, 2743);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 6
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 1, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 7
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      StringBuffer stringBuffer0 = StringEncoder64.encode(byteArray0, 0, 0, (StringBuffer) null);
      assertEquals(0, stringBuffer0.length());
  }

//  @Test
//  public void test05()  throws Throwable  {
//      byte[] byteArray0 = new byte[9];
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("ABV=V|`|/?GO");
//      mockFileOutputStream0.close();
//      DataOutputStream dataOutputStream0 = new DataOutputStream(mockFileOutputStream0);
//      boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte)1, (int) (byte)1, (OutputStream) dataOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test06()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("");
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("C=");
      assertEquals("", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("Hz%");
      assertArrayEquals(new byte[] {}, byteArray0);
  }

  @Test
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encodeStringUTF8((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 0, (int) (byte)37, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-1), (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test13()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test14()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode((String) null, (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test15()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      try {
//        StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", (OutputStream) pipedOutputStream0);
//        fail("Expecting exception: IOException");
//
//      } catch(IOException e) {
//         //
//         // Pipe not connected
//         //
//         //verifyException("java.io.PipedOutputStream", e);
//      }
//  }

  @Test
  public void test16()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test17()  throws Throwable  {
//      MockPrintStream mockPrintStream0 = new MockPrintStream("ABCDEFGHIJKLMNOPQRbTUVWXYZabcdeghijklmnopqrstuvwxyz123456789+/");
//      StringEncoder64.decode("QUJDREVGR0hJSktMTU5PUFFSYlRVVldYWVphYmNkZWdoaWprbG1ub3BxcnN0\r\ndXZ3eHl6MTIzNDU2Nzg5Ky8=", (OutputStream) mockPrintStream0);
//  }

  @Test
  public void test18()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      StringEncoder64.decode("/W=Qk4GbuR ", (OutputStream) byteArrayOutputStream0);
      assertEquals(1, byteArrayOutputStream0.size());
      assertEquals("\uFFFD", byteArrayOutputStream0.toString());
  }

  @Test
  public void test19()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.decode("MFnr`{13P=?dg=Ia,K", (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: `
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test20()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      StringEncoder64.decode("", (OutputStream) byteArrayOutputStream0);
      assertEquals("", byteArrayOutputStream0.toString());
  }

  @Test
  public void test21()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.decode(" zAN%zM/C%hw", (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: %
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test22()  throws Throwable  {
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      int int0 = StringEncoder64.decode('=');
      assertEquals(0, int0);
  }

  @Test
  public void test24()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test25()  throws Throwable  {
      int int0 = StringEncoder64.decode('b');
      assertEquals(27, int0);
  }

  @Test
  public void test26()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode('~');
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: ~
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test27()  throws Throwable  {
      int int0 = StringEncoder64.decode('2');
      assertEquals(54, int0);
  }

  @Test
  public void test28()  throws Throwable  {
      int int0 = StringEncoder64.decode('D');
      assertEquals(3, int0);
  }

  @Test
  public void test29()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[3];
      boolean boolean0 = StringEncoder64.encode(byteArray0, 8, 8, (OutputStream) byteArrayOutputStream0);
      assertTrue(boolean0);
  }

  @Test
  public void test30()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 1, 8, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 7
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test31()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      char[] charArray0 = new char[8];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      StringBuffer stringBuffer0 = new StringBuffer(charBuffer0);
      StringBuffer stringBuffer1 = StringEncoder64.encode(byteArray0, (int) (byte)0, (-1), stringBuffer0);
      assertEquals(8, stringBuffer1.length());
  }

  @Test
  public void test32()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer(2004);
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 2004, 2, stringBuffer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test33()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      StringBuffer stringBuffer0 = new StringBuffer(2757);
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (-1), 12, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test34()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("AAAA", string0);
  }

  @Test
  public void test35()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8(" vmOu]");
      assertEquals("\uFFFDc\uFFFD", string0);
  }

  @Test
  public void test36()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("UTF8");
      assertArrayEquals(new byte[] {(byte)81, (byte)49, (byte)124}, byteArray0);
  }

  @Test
  public void test37()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("71zn+?$?V");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: ?
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test38()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8("yL39g/{zY)b");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: {
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test39()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("==");
      assertEquals("PT0=", string0);
      assertNotNull(string0);
  }

  @Test
  public void test40()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[45];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 0, 118, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 45
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test41()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[45];
      StringEncoder64.encode(byteArray0, 0, 43, (OutputStream) byteArrayOutputStream0);
      assertEquals(60, byteArrayOutputStream0.size());
      assertEquals("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==", byteArrayOutputStream0.toString());
  }

  @Test
  public void test42()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 1, 1, (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test43()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)0);
      assertEquals("", string0);
  }

  @Test
  public void test44()  throws Throwable  {
      byte[] byteArray0 = new byte[14];
      StringBuffer stringBuffer0 = new StringBuffer();
      StringEncoder64.encode(byteArray0, 1, 1, stringBuffer0);
      assertEquals(4, stringBuffer0.length());
      assertEquals("AA==", stringBuffer0.toString());
  }

  @Test
  public void test45()  throws Throwable  {
      byte[] byteArray0 = new byte[10];
      String string0 = StringEncoder64.encode(byteArray0, 2, 2);
      assertEquals("AAA=", string0);
  }

  @Test
  public void test46()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }

  @Test
  public void test47()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }
}
