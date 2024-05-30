package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.OutputStream;

public class StringEncoder64_ESTest_7 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdfghijklmnopqrstuvwxyz0123456789+/");
      assertEquals("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZmdoaWprbG1ub3BxcnN0\r\ndXZ3eHl6MDEyMzQ1Njc4OSsv", string0);
      assertNotNull(string0);
  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[1] = (byte) (-100);
      StringBuffer stringBuffer0 = new StringBuffer();
      StringEncoder64.encode(byteArray0, 0, (int) (byte)3, stringBuffer0);
      assertEquals(4, stringBuffer0.length());
      assertEquals("AJwA", stringBuffer0.toString());
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[0] = (byte)3;
      StringBuffer stringBuffer0 = new StringBuffer();
      StringEncoder64.encode(byteArray0, 0, (int) (byte)3, stringBuffer0);
      assertEquals(4, stringBuffer0.length());
      assertEquals("AwAA", stringBuffer0.toString());
  }

  @Test
  public void test03()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("%");
      assertNotNull(string0);
      assertEquals("JQ==", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)116, (int) (byte)116);
      assertEquals("", string0);
  }

  @Test
  public void test05()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("GwY");
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test06()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8(" ");
      assertEquals("", string0);
  }

  @Test
  public void test07()  throws Throwable  {
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
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 35, 35, (StringBuffer) null);
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
        StringEncoder64.encode((byte[]) null, 0, 0);
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
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8("k4 vFIJ:]&z__A");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code:  
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
        StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh=jkzmnopqltuvwxyz0123456789+/", (OutputStream) null);
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
//        StringEncoder64.decode("yu6kH[_`yQH,!X", (OutputStream) pipedOutputStream0);
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
  public void test16()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(1192);
      StringEncoder64.decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", (OutputStream) byteArrayOutputStream0);
      assertEquals(64, byteArrayOutputStream0.size());
      assertEquals("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", byteArrayOutputStream0.toString());
  }

//  @Test
//  public void test17()  throws Throwable  {
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("BL5,\"VJ", false);
//      StringEncoder64.decode("g78=U%ErXC", (OutputStream) mockFileOutputStream0);
//  }

  @Test
  public void test18()  throws Throwable  {
      int int0 = StringEncoder64.decode('=');
      assertEquals(0, int0);
  }

  @Test
  public void test19()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test20()  throws Throwable  {
      int int0 = StringEncoder64.decode('4');
      assertEquals(56, int0);
  }

  @Test
  public void test21()  throws Throwable  {
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
  public void test22()  throws Throwable  {
      int int0 = StringEncoder64.decode('M');
      assertEquals(12, int0);
  }

  @Test
  public void test23()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(706);
      boolean boolean0 = StringEncoder64.encode(byteArray0, 706, 706, (OutputStream) byteArrayOutputStream0);
      assertTrue(boolean0);
  }

//  @Test
//  public void test24()  throws Throwable  {
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("osa.ora.serve$.utils.StringEncoder64");
//      FilterOutputStream filterOutputStream0 = new FilterOutputStream(mockFileOutputStream0);
//      MockPrintStream mockPrintStream0 = new MockPrintStream(filterOutputStream0, true);
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode((byte[]) null, 33, 2, (OutputStream) mockPrintStream0);
//        fail("Expecting exception: NullPointerException");
//
//      } catch(NullPointerException e) {
//         //
//         // no message in exception (getMessage() returned null)
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

//  @Test
//  public void test25()  throws Throwable  {
//      byte[] byteArray0 = new byte[49];
//      MockPrintStream mockPrintStream0 = new MockPrintStream("AA==");
//      BufferedOutputStream bufferedOutputStream0 = new BufferedOutputStream(mockPrintStream0, 77);
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, 0, 77, (OutputStream) bufferedOutputStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 49
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

//  @Test
//  public void test26()  throws Throwable  {
//      byte[] byteArray0 = new byte[47];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 0, 5, (OutputStream) pipedOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test27()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      StringBuffer stringBuffer0 = StringEncoder64.encode(byteArray0, 1, 1, (StringBuffer) null);
      assertEquals("AA==", stringBuffer0.toString());
  }

  @Test
  public void test28()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      StringBuffer stringBuffer0 = new StringBuffer("C=");
      StringEncoder64.encode(byteArray0, 2, 2, stringBuffer0);
      assertEquals(6, stringBuffer0.length());
      assertEquals("C=AAA=", stringBuffer0.toString());
  }

  @Test
  public void test29()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 1, (int) (byte)107, (StringBuffer) null);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 8
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test30()  throws Throwable  {
      byte[] byteArray0 = new byte[47];
      StringBuffer stringBuffer0 = StringEncoder64.encode(byteArray0, 42, 42, (StringBuffer) null);
      assertEquals(0, stringBuffer0.length());
  }

  @Test
  public void test31()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh=jkzmnopqltuvwxyz0123456789+/");
      assertEquals(25, byteArray0.length);
  }

//  @Test
//  public void test32()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      StringEncoder64.decode("\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000", (OutputStream) pipedOutputStream0);
//  }

  @Test
  public void test33()  throws Throwable  {
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test34()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("qgpyMM3b4PM_$+Hw");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: _
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test35()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("/jS=H`^J>2M?VtnD[%8");
      assertEquals("\uFFFD4", string0);
      assertNotNull(string0);
  }

  @Test
  public void test36()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.decode("}1Ib! Gkl8=*^=jk", (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: }
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test37()  throws Throwable  {
      int int0 = StringEncoder64.decode('h');
      assertEquals(33, int0);
  }

  @Test
  public void test38()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-1), 1, (OutputStream) byteArrayOutputStream0);
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
      byte[] byteArray0 = new byte[47];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\r\nAAA=", string0);
      assertNotNull(string0);
  }

  @Test
  public void test40()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-3182), (-3182), (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test41()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      String string0 = StringEncoder64.encode(byteArray0, 2, 2);
      assertEquals("AAA=", string0);
  }

  @Test
  public void test42()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)0, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test43()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }

  @Test
  public void test44()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }
}
