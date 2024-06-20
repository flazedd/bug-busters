package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
public class StringEncoder64_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("Uu2MyZSnn6/");
      assertEquals("R\uFFFD\u0254\uFFFD", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==");
      assertEquals("UVVKRFJFVkdSMGhKU2t0TVRVNVBVRkZTVTFSVlZsZFlXVnBoWW1Oa1pXWm5h\r\nR2xxYTJ4dGJtOXdjWEp6DQpkSFYyZDNoNWVqQXhNak0wTlRZM09Ea3JMdz09\r\n", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      StringBuffer stringBuffer0 = new StringBuffer((CharSequence) "AgAAAAA=");
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)0, 262, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 5
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[3] = (byte)2;
      StringBuffer stringBuffer0 = new StringBuffer("JT_<V");
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)2, (int) (byte)14, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 6
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[2] = (byte)14;
      StringBuffer stringBuffer0 = new StringBuffer("JT_<V");
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)2, (int) (byte)14, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 6
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 42, 45);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 42
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test06()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      String string0 = StringEncoder64.encode(byteArray0, 2, 2);
      assertEquals("AAA=", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("2");
      StringBuffer stringBuffer0 = new StringBuffer("=");
      StringBuffer stringBuffer1 = StringEncoder64.encode(byteArray0, 3019, 3019, stringBuffer0);
      assertSame(stringBuffer0, stringBuffer1);
  }

//  @Test
//  public void test09()  throws Throwable  {
//      byte[] byteArray0 = new byte[9];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)121, (OutputStream) pipedOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test10()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)64, (int) (byte)64);
      assertEquals("", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      String string0 = StringEncoder64.encode(byteArray0);
      assertNotNull(string0);
      assertEquals("AA==", string0);
  }

  @Test
  public void test12()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test13()  throws Throwable  {
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
  public void test14()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-1034), (-722), (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 54, 54);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test16()  throws Throwable  {
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
  public void test17()  throws Throwable  {
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
  public void test18()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.decode("`:k*X|/", (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: `
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("UTF8", (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test20()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      try {
//        StringEncoder64.decode("BMcGXSTE", (OutputStream) pipedOutputStream0);
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
  public void test21()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("T.j/_>ojX*`0");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: .
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test22()  throws Throwable  {
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
  public void test23()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      StringEncoder64.decode("nYUBEf8Z3ME=", (OutputStream) byteArrayOutputStream0);
      assertEquals(8, byteArrayOutputStream0.size());
      assertEquals("\uFFFD\uFFFD\u0001\u0011\uFFFD\u0019\uFFFD\uFFFD", byteArrayOutputStream0.toString());
  }

  @Test
  public void test24()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      StringEncoder64.decode("", (OutputStream) byteArrayOutputStream0);
      assertEquals("", byteArrayOutputStream0.toString());
  }

  @Test
  public void test25()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      StringEncoder64.decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", (OutputStream) byteArrayOutputStream0);
      assertEquals(64, byteArrayOutputStream0.size());
      assertEquals("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", byteArrayOutputStream0.toString());
  }

  @Test
  public void test26()  throws Throwable  {
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test27()  throws Throwable  {
      int int0 = StringEncoder64.decode('=');
      assertEquals(0, int0);
  }

  @Test
  public void test28()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test29()  throws Throwable  {
      int int0 = StringEncoder64.decode('5');
      assertEquals(57, int0);
  }

  @Test
  public void test30()  throws Throwable  {
      int int0 = StringEncoder64.decode('v');
      assertEquals(47, int0);
  }

  @Test
  public void test31()  throws Throwable  {
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
  public void test32()  throws Throwable  {
      int int0 = StringEncoder64.decode('A');
      assertEquals(0, int0);
  }

//  @Test
//  public void test33()  throws Throwable  {
//      byte[] byteArray0 = new byte[4];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      MockPrintStream mockPrintStream0 = new MockPrintStream(pipedOutputStream0);
//      boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte)61, (int) (byte) (-100), (OutputStream) mockPrintStream0);
//      assertTrue(boolean0);
//  }
//
//  @Test
//  public void test34()  throws Throwable  {
//      byte[] byteArray0 = new byte[8];
//      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
//      MockPrintStream mockPrintStream0 = new MockPrintStream(byteArrayOutputStream0);
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, 61, 2, (OutputStream) mockPrintStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 61
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }
//
//  @Test
//  public void test35()  throws Throwable  {
//      MockFile mockFile0 = new MockFile("`:k*X|/", "`:k*X|/");
//      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
//      byte[] byteArray0 = new byte[4];
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, (int) (byte)50, (int) (byte)1, (OutputStream) mockPrintStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 50
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test36()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)1, (int) (byte)1, (StringBuffer) null);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test37()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 2, 2, (StringBuffer) null);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 2
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test38()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-1), (-1), (StringBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test39()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("9Qz5 =O6Q");
      assertArrayEquals(new byte[] {(byte) (-11), (byte)12, (byte) (-7), (byte)0, (byte) (-18), (byte) (-112)}, byteArray0);
  }

  @Test
  public void test40()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8("Tl~~LX0cFlaSKX=Gg[");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: ~
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test41()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

//  @Test
//  public void test42()  throws Throwable  {
//      byte[] byteArray0 = new byte[46];
//      PipedInputStream pipedInputStream0 = new PipedInputStream();
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream(pipedInputStream0);
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, 0, 3829, (OutputStream) pipedOutputStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 46
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test43()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 55, 55, (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test44()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      String string0 = StringEncoder64.encode(byteArray0, 1, 1);
      assertEquals("AA==", string0);
  }

  @Test
  public void test45()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      StringBuffer stringBuffer0 = new StringBuffer();
      StringBuffer stringBuffer1 = StringEncoder64.encode(byteArray0, 62, 62, stringBuffer0);
      assertSame(stringBuffer1, stringBuffer0);
  }

  @Test
  public void test46()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }

  @Test
  public void test47()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("&M~>BJ}yU3}Pz-");
      assertEquals("Jk1+PkJKfXlVM31Qei0=", string0);
      assertNotNull(string0);
  }
}
