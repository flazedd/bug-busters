package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
public class StringEncoder64_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("r7");
      assertEquals("", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      byteArray0[2] = (byte)48;
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)1, (int) (byte)44, (StringBuffer) null);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 8
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      byteArray0[1] = (byte)106;
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)1, (int) (byte)44, (StringBuffer) null);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 8
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 0, 3);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)0, 1);
      assertEquals("AA==", string0);
  }

//  @Test
//  public void test05()  throws Throwable  {
//      byte[] byteArray0 = new byte[9];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 0, 56, (OutputStream) pipedOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test06()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = StringEncoder64.encode(byteArray0, (-8), (-8));
      assertEquals("", string0);
  }

  @Test
  public void test07()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("");
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("b0J6");
      assertArrayEquals(new byte[] {(byte)111, (byte)66, (byte)122}, byteArray0);
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
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 57, 57);
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
  public void test12()  throws Throwable  {
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
  public void test13()  throws Throwable  {
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
//  public void test14()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      try {
//        StringEncoder64.decode("UTF8", (OutputStream) pipedOutputStream0);
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
  public void test15()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("|AQ1Y0}R\")i");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: |
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test16()  throws Throwable  {
//      MockPrintStream mockPrintStream0 = new MockPrintStream("Gx6zVgAAAA==");
//      StringEncoder64.decode("Gx6zVgAAAA==", (OutputStream) mockPrintStream0);
//  }

//  @Test
//  public void test17()  throws Throwable  {
//      MockPrintStream mockPrintStream0 = new MockPrintStream("\u0000\u0000\u0000\u0000\u0000");
//      StringEncoder64.decode("AAAAAAA=", (OutputStream) mockPrintStream0);
//  }

  @Test
  public void test18()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("r;qizk.", (OutputStream) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: ;
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test19()  throws Throwable  {
      StringEncoder64.decode("\u0000\u0000\u0000\u0000\u0000\u0000", (OutputStream) null);
  }

  @Test
  public void test20()  throws Throwable  {
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test21()  throws Throwable  {
      int int0 = StringEncoder64.decode('=');
      assertEquals(0, int0);
  }

  @Test
  public void test22()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      int int0 = StringEncoder64.decode('9');
      assertEquals(61, int0);
  }

  @Test
  public void test24()  throws Throwable  {
      int int0 = StringEncoder64.decode('a');
      assertEquals(26, int0);
  }

  @Test
  public void test25()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode('}');
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: }
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test26()  throws Throwable  {
      int int0 = StringEncoder64.decode('Y');
      assertEquals(24, int0);
  }

  @Test
  public void test27()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      boolean boolean0 = StringEncoder64.encode(byteArray0, 29, (-773), (OutputStream) byteArrayOutputStream0);
      assertTrue(boolean0);
  }

//  @Test
//  public void test28()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode((byte[]) null, 1, 1, (OutputStream) pipedOutputStream0);
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
  public void test29()  throws Throwable  {
      byte[] byteArray0 = new byte[48];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 0, 258, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 48
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test30()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      StringBuffer stringBuffer0 = new StringBuffer("");
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (-1), (int) (byte)1, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test31()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      StringBuffer stringBuffer0 = new StringBuffer(2);
      StringEncoder64.encode(byteArray0, 2, 2, stringBuffer0);
      assertEquals(4, stringBuffer0.length());
      assertEquals("AAA=", stringBuffer0.toString());
  }

  @Test
  public void test32()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 416, 416, (StringBuffer) null);
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
      byte[] byteArray0 = new byte[6];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("AAAAAAAA", string0);
  }

  @Test
  public void test34()  throws Throwable  {
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
  public void test35()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("CJ=S");
      assertEquals("\b", string0);
  }

  @Test
  public void test36()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8(" !");
      assertEquals("", string0);
  }

  @Test
  public void test37()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
      assertEquals("\u0000\u0010\uFFFD\u0010Q\uFFFD \uFFFD\uFFFD0\u04CFA\u0014\uFFFDQU\uFFFDa\uFFFD\uFFFDq\u05DF\uFFFD\u0018\uFFFD\uFFFDY\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\u06EF\uFFFD\u001C\uFFFD\uFFFD]\uFFFD\u37BB\uFFFD\u07FF", string0);
      assertNotNull(string0);
  }

  @Test
  public void test38()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8("R=~ wp]");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: ~
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test39()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test40()  throws Throwable  {
      byte[] byteArray0 = new byte[10];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      StringEncoder64.encode(byteArray0, 1, 2, (OutputStream) byteArrayOutputStream0);
      assertEquals(4, byteArrayOutputStream0.size());
      assertEquals("AAA=", byteArrayOutputStream0.toString());
  }

  @Test
  public void test41()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 122, 122, (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test42()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      StringBuffer stringBuffer0 = new StringBuffer(10);
      StringBuffer stringBuffer1 = StringEncoder64.encode(byteArray0, 10, 10, stringBuffer0);
      assertSame(stringBuffer1, stringBuffer0);
  }

  @Test
  public void test43()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }

  @Test
  public void test44()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
      assertEquals("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", string0);
  }
}
