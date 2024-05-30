package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.OutputStream;

public class StringEncoder64_ESTest_1 {

//  @Test
//  public void test00()  throws Throwable  {
//      MockPrintStream mockPrintStream0 = new MockPrintStream(".Q<");
//      StringEncoder64.decode(".Q<", (OutputStream) mockPrintStream0);
//  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==");
      assertEquals(64, byteArray0.length);
  }

  @Test
  public void test02()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("AAAAAAAAAAA=");
      assertEquals("QUFBQUFBQUFBQUE9", string0);
      assertNotNull(string0);
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      byteArray0[0] = (byte)8;
      StringBuffer stringBuffer0 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)0, (StringBuffer) null);
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)18, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 5
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      byteArray0[3] = (byte)2;
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)2, 1915);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 4
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      StringBuffer stringBuffer0 = new StringBuffer("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==");
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 63, 66, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 63
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test06()  throws Throwable  {
//      FileSystemHandling.shouldAllThrowIOExceptions();
//      byte[] byteArray0 = new byte[3];
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("cHBw");
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 1, 1, (OutputStream) mockFileOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test07()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("s");
      assertArrayEquals(new byte[] {}, byteArray0);
  }

  @Test
  public void test10()  throws Throwable  {
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

//  @Test
//  public void test11()  throws Throwable  {
//      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
//      BufferedOutputStream bufferedOutputStream0 = new BufferedOutputStream(byteArrayOutputStream0, 1);
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode((byte[]) null, 62, 106, (OutputStream) bufferedOutputStream0);
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
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 2518, 2518);
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
  public void test14()  throws Throwable  {
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
  public void test15()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("osa.ora.server.utils.StringEncoder64", (OutputStream) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: .
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test16()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      // Undeclared exception!
//      try {
//        StringEncoder64.decode((String) null, (OutputStream) pipedOutputStream0);
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
  public void test17()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("FVWJj}2AYaHN$rEo.(");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: }
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test18()  throws Throwable  {
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
//  public void test19()  throws Throwable  {
//      MockPrintStream mockPrintStream0 = new MockPrintStream("cABwcA==");
//      StringEncoder64.decode("cABwcA==", (OutputStream) mockPrintStream0);
//  }
//
//  @Test
//  public void test20()  throws Throwable  {
//      MockPrintStream mockPrintStream0 = new MockPrintStream("UTF8");
//      StringEncoder64.decode("372=?D0", (OutputStream) mockPrintStream0);
//  }
//
//  @Test
//  public void test21()  throws Throwable  {
//      MockPrintStream mockPrintStream0 = new MockPrintStream("AAAAAAAAAAA=");
//      StringEncoder64.decode(" ", (OutputStream) mockPrintStream0);
//  }

  @Test
  public void test22()  throws Throwable  {
      int int0 = StringEncoder64.decode('=');
      assertEquals(0, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test24()  throws Throwable  {
      int int0 = StringEncoder64.decode('3');
      assertEquals(55, int0);
  }

  @Test
  public void test25()  throws Throwable  {
      int int0 = StringEncoder64.decode('i');
      assertEquals(34, int0);
  }

  @Test
  public void test26()  throws Throwable  {
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test27()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode('');
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: 
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test28()  throws Throwable  {
      int int0 = StringEncoder64.decode('J');
      assertEquals(9, int0);
  }

//  @Test
//  public void test29()  throws Throwable  {
//      byte[] byteArray0 = new byte[8];
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("\"<FsRn:(S4");
//      boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte)112, (int) (byte)97, (OutputStream) mockFileOutputStream0);
//      assertTrue(boolean0);
//  }
//
//  @Test
//  public void test30()  throws Throwable  {
//      byte[] byteArray0 = new byte[1];
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, 36, 2, (OutputStream) mockFileOutputStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 36
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test31()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer((CharSequence) "D&)9A:i.HM<@OP %");
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
  public void test32()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer((CharSequence) "MkY3SC8=");
      byte[] byteArray0 = new byte[4];
      StringEncoder64.encode(byteArray0, 0, (int) (byte)2, stringBuffer0);
      assertEquals(12, stringBuffer0.length());
      assertEquals("MkY3SC8=AAA=", stringBuffer0.toString());
  }

  @Test
  public void test33()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      String string0 = StringEncoder64.encode(byteArray0);
      assertNotNull(string0);
      assertEquals("AAAAAAAAAAA=", string0);
  }

  @Test
  public void test34()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("OM=+,F");
      assertNotNull(string0);
      assertEquals("8", string0);
  }

//  @Test
//  public void test35()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      try {
//        StringEncoder64.decode("+Dpf2ln$m {", (OutputStream) pipedOutputStream0);
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
  public void test36()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
      assertNotNull(string0);
      assertEquals("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", string0);
  }

  @Test
  public void test37()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }

//  @Test
//  public void test38()  throws Throwable  {
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("(ZT");
//      byte[] byteArray0 = new byte[48];
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, (int) (byte)0, 1065, (OutputStream) mockFileOutputStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 48
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test39()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 6, 6, (OutputStream) null);
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
      byte[] byteArray0 = new byte[8];
      String string0 = StringEncoder64.encode(byteArray0, 1, 1);
      assertEquals("AA==", string0);
  }

  @Test
  public void test41()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)0);
      assertEquals("", string0);
  }

  @Test
  public void test42()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }

  @Test
  public void test43()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8(" mD}5*");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: }
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }
}
