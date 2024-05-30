package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.OutputStream;

public class StringEncoder64_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("$S?");
      assertEquals("", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8("\u0000\u0010\uFFFD\u0010Q\uFFFD \uFFFD\uFFFD0\u04CFA\u0014\uFFFDQU\uFFFDa\uFFFD\uFFFDq\u05DF\uFFFD\u0018\uFFFD\uFFFDY\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\u06EF\uFFFD\u001C\uFFFD\uFFFD]\uFFFD\u37BB\uFFFD\u07FF");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: \uFFFD
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[23];
      byteArray0[1] = (byte)54;
      StringBuffer stringBuffer0 = new StringBuffer(450);
      StringEncoder64.encode(byteArray0, 0, (int) (byte)13, stringBuffer0);
      assertEquals("ADYAAAAAAAAAAAAAAA==", stringBuffer0.toString());
      assertEquals(20, stringBuffer0.length());
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[23];
      byteArray0[0] = (byte) (-77);
      StringBuffer stringBuffer0 = new StringBuffer(450);
      StringEncoder64.encode(byteArray0, 0, (int) (byte)13, stringBuffer0);
      assertEquals(20, stringBuffer0.length());
      assertEquals("swAAAAAAAAAAAAAAAA==", stringBuffer0.toString());
  }

//  @Test
//  public void test04()  throws Throwable  {
//      byte[] byteArray0 = new byte[9];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 1, (int) (byte)59, (OutputStream) pipedOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[10];
      String string0 = StringEncoder64.encode(byteArray0, 1, 1);
      assertEquals("AA==", string0);
  }

  @Test
  public void test06()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567\r\n89+/", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("");
      assertArrayEquals(new byte[] {}, byteArray0);
  }

  @Test
  public void test08()  throws Throwable  {
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
  public void test09()  throws Throwable  {
      byte[] byteArray0 = new byte[23];
      StringBuffer stringBuffer0 = new StringBuffer();
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (-1), 3, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test10()  throws Throwable  {
//      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode((byte[]) null, 1, 1, (OutputStream) byteArrayOutputStream0);
//        fail("Expecting exception: NullPointerException");
//
//      } catch(NullPointerException e) {
//         //
//         // no message in exception (getMessage() returned null)
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 1538, 1538);
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
        StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZacdefghijklmnopqrstuvwxyz0123456789+/", (OutputStream) null);
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
//        StringEncoder64.decode("7NsLq#qY>>", (OutputStream) pipedOutputStream0);
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

  @Test
  public void test17()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(18);
      StringEncoder64.decode("8r=K", (OutputStream) byteArrayOutputStream0);
      assertEquals("\uFFFD", byteArrayOutputStream0.toString());
      assertEquals(1, byteArrayOutputStream0.size());
  }

//  @Test
//  public void test18()  throws Throwable  {
//      MockFile mockFile0 = new MockFile("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=");
//      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
//      StringEncoder64.decode("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=", (OutputStream) mockPrintStream0);
//      assertEquals(23L, mockFile0.length());
//  }

  @Test
  public void test19()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      StringEncoder64.decode("", (OutputStream) byteArrayOutputStream0);
      assertEquals("", byteArrayOutputStream0.toString());
  }

//  @Test
//  public void test20()  throws Throwable  {
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("UTF8", false);
//      // Undeclared exception!
//      try {
//        StringEncoder64.decode(" cf(\"&s$dY~2", (OutputStream) mockFileOutputStream0);
//        fail("Expecting exception: RuntimeException");
//
//      } catch(RuntimeException e) {
//         //
//         // unexpected code: (
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test21()  throws Throwable  {
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test22()  throws Throwable  {
      int int0 = StringEncoder64.decode('=');
      assertEquals(0, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      int int0 = StringEncoder64.decode('4');
      assertEquals(56, int0);
  }

  @Test
  public void test24()  throws Throwable  {
      int int0 = StringEncoder64.decode('s');
      assertEquals(44, int0);
  }

  @Test
  public void test25()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode('{');
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: {
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test26()  throws Throwable  {
      int int0 = StringEncoder64.decode('A');
      assertEquals(0, int0);
  }

//  @Test
//  public void test27()  throws Throwable  {
//      byte[] byteArray0 = StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, 1040, 2, (OutputStream) pipedOutputStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 1040
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test28()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer();
      StringBuffer stringBuffer1 = StringEncoder64.encode((byte[]) null, 3, 3, stringBuffer0);
      assertEquals(0, stringBuffer1.length());
  }

  @Test
  public void test29()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
      StringBuffer stringBuffer0 = new StringBuffer();
      StringEncoder64.encode(byteArray0, 2, 2, stringBuffer0);
      assertEquals(4, stringBuffer0.length());
      assertEquals("gxA=", stringBuffer0.toString());
  }

  @Test
  public void test30()  throws Throwable  {
      byte[] byteArray0 = new byte[19];
      StringBuffer stringBuffer0 = new StringBuffer();
      StringEncoder64.encode(byteArray0, 1, 13, stringBuffer0);
      assertEquals(20, stringBuffer0.length());
      assertEquals("AAAAAAAAAAAAAAAAAA==", stringBuffer0.toString());
  }

  @Test
  public void test31()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-1089), (-1), (StringBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test32()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test33()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("CPy=C%_fO");
      assertEquals("\b\uFFFD", string0);
      assertNotNull(string0);
  }

  @Test
  public void test34()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test35()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode(" +cI1z|Y\"1~QI#<TI");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: |
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test36()  throws Throwable  {
//      byte[] byteArray0 = new byte[8];
//      MockFile mockFile0 = new MockFile("unexpected code: ");
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(mockFile0);
//      StringEncoder64.encode(byteArray0, 1, 4, (OutputStream) mockFileOutputStream0);
//      assertEquals(8L, mockFile0.length());
//  }

  @Test
  public void test37()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdfghijklmnopqrstuvwxyz0123456789v");
      assertNotNull(string0);
      assertEquals("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZmdoaWprbG1ub3BxcnN0\r\ndXZ3eHl6MDEyMzQ1Njc4OXY=", string0);
  }

//  @Test
//  public void test38()  throws Throwable  {
//      byte[] byteArray0 = new byte[57];
//      MockFile mockFile0 = new MockFile("=");
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(mockFile0);
//      StringEncoder64.encode(byteArray0, 0, 57, (OutputStream) mockFileOutputStream0);
//      assertEquals(78L, mockFile0.length());
//  }

  @Test
  public void test39()  throws Throwable  {
      byte[] byteArray0 = new byte[75];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (-279), (-279), (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test40()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)0);
      assertEquals("", string0);
  }

  @Test
  public void test41()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 2, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 2
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test42()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }

  @Test
  public void test43()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }
}
