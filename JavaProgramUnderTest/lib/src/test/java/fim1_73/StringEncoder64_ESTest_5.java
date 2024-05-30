package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.OutputStream;

public class StringEncoder64_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      byteArray0[1] = (byte)5;
      StringBuffer stringBuffer0 = new StringBuffer();
      StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)5, stringBuffer0);
      assertEquals(8, stringBuffer0.length());
      assertEquals("AAUAAAA=", stringBuffer0.toString());
  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      byteArray0[0] = (byte)28;
      StringBuffer stringBuffer0 = new StringBuffer();
      StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)5, stringBuffer0);
      assertEquals(8, stringBuffer0.length());
      assertEquals("HAAAAAA=", stringBuffer0.toString());
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)0, 6);
      assertEquals("AAAAAAAA", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }

//  @Test
//  public void test04()  throws Throwable  {
//      byte[] byteArray0 = new byte[8];
//      FileSystemHandling.shouldAllThrowIOExceptions();
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("Qp63*S");
//      boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte)0, 58, (OutputStream) mockFileOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test06()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("");
      assertEquals(0, byteArray0.length);
  }

  @Test
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 42, 42);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test08()  throws Throwable  {
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
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8("ABCDEFGHIJKLMNOPQ`STUVWXYZabcdefghijklmnopqrs%uvwyz0123}5789+/");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: `
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.decode("X~y@|eb", (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: ~
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test12()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      try {
//        StringEncoder64.decode("GROVacIOH}xrMD1se", (OutputStream) pipedOutputStream0);
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
  public void test13()  throws Throwable  {
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
//  public void test14()  throws Throwable  {
//      File file0 = MockFile.createTempFile("cTEmMWs3VHUueyUya2h+NVUndno=", "#wEJV2&(_C:_");
//      MockPrintStream mockPrintStream0 = new MockPrintStream(file0);
//      StringEncoder64.decode("cTEmMWs3VHUueyUya2h+NVUndno=", (OutputStream) mockPrintStream0);
//      assertEquals(20L, file0.length());
//  }

  @Test
  public void test15()  throws Throwable  {
      StringEncoder64.decode("", (OutputStream) null);
  }

//  @Test
//  public void test16()  throws Throwable  {
//      File file0 = MockFile.createTempFile("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", "#wEJV2&(_C:_");
//      MockPrintStream mockPrintStream0 = new MockPrintStream(file0);
//      StringEncoder64.decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", (OutputStream) mockPrintStream0);
//      assertEquals(64L, file0.length());
//  }

  @Test
  public void test17()  throws Throwable  {
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test18()  throws Throwable  {
      int int0 = StringEncoder64.decode('=');
      assertEquals(0, int0);
  }

  @Test
  public void test19()  throws Throwable  {
      int int0 = StringEncoder64.decode('9');
      assertEquals(61, int0);
  }

  @Test
  public void test20()  throws Throwable  {
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
  public void test21()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test22()  throws Throwable  {
      int int0 = StringEncoder64.decode('D');
      assertEquals(3, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      int int0 = StringEncoder64.decode('x');
      assertEquals(49, int0);
  }

//  @Test
//  public void test24()  throws Throwable  {
//      byte[] byteArray0 = new byte[3];
//      MockPrintStream mockPrintStream0 = new MockPrintStream("O]");
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 0, 1, (OutputStream) mockPrintStream0);
//      assertTrue(boolean0);
//  }

  @Test
  public void test25()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream((byte)62);
      boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte)62, (-1), (OutputStream) byteArrayOutputStream0);
      assertTrue(boolean0);
  }

  @Test
  public void test26()  throws Throwable  {
      byte[] byteArray0 = new byte[49];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 0, 53, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 49
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test27()  throws Throwable  {
//      byte[] byteArray0 = new byte[1];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, 3831, (int) (byte)2, (OutputStream) pipedOutputStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 3831
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test28()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 13, 1324, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test29()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer();
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 1, 1, stringBuffer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test30()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      StringBuffer stringBuffer0 = StringEncoder64.encode(byteArray0, 322, (int) (byte)0, (StringBuffer) null);
      assertEquals("", stringBuffer0.toString());
  }

  @Test
  public void test31()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("ABCDEFGHIJK=MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwnyz012456789+/");
      assertEquals("\u0000\u0010\uFFFD\u0010Q\uFFFD \uFFFD", string0);
      assertNotNull(string0);
  }

  @Test
  public void test32()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("aJe2 57Mc|!0");
      assertEquals("h\uFFFD\uFFFD\uFFFD\u001C", string0);
  }

  @Test
  public void test33()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("M/ii$@eHz", (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test34()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("2}&T<yOU3yC");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: }
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test35()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      String string0 = StringEncoder64.encode(byteArray0);
      assertNotNull(string0);
      assertEquals("AAAAAAAA", string0);
  }

  @Test
  public void test36()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234789+/");
      assertNotNull(string0);
      assertEquals("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0Nzg5Ky8=", string0);
  }

  @Test
  public void test37()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 0, 0, (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test38()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)0);
      assertEquals("", string0);
  }

  @Test
  public void test39()  throws Throwable  {
      byte[] byteArray0 = new byte[12];
      String string0 = StringEncoder64.encode(byteArray0, 1, 1);
      assertEquals("AA==", string0);
  }

  @Test
  public void test40()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      StringBuffer stringBuffer0 = new StringBuffer();
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (-725), 3124, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -725
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test41()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (-1445), (int) (byte)0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1445
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test42()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test43()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }

  @Test
  public void test44()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("uV=M_t");
      assertArrayEquals(new byte[] {(byte) (-71)}, byteArray0);
  }

  @Test
  public void test45()  throws Throwable  {
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
}
