package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
public class StringEncoder64_ESTest_10 {

//  @Test
//  public void test00()  throws Throwable  {
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("pZBc:e_", true);
//      FilterOutputStream filterOutputStream0 = new FilterOutputStream(mockFileOutputStream0);
//      StringEncoder64.decode("pZBc:e_", (OutputStream) filterOutputStream0);
//  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      byteArray0[1] = (byte)16;
      String string0 = StringEncoder64.encode(byteArray0, 0, (int) (byte)8);
      assertEquals("ABAAAAAAAAA=", string0);
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      byteArray0[3] = (byte)1;
      String string0 = StringEncoder64.encode(byteArray0, 0, (int) (byte)8);
      assertEquals("AAAAAQAAAAA=", string0);
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      StringBuffer stringBuffer0 = new StringBuffer(2555);
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (-1), 2, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[13];
      String string0 = StringEncoder64.encode(byteArray0, 1, 1);
      assertEquals("AA==", string0);
  }

  @Test
  public void test05()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("%TF8");
      assertEquals("JVRGOA==", string0);
  }

//  @Test
//  public void test06()  throws Throwable  {
//      byte[] byteArray0 = new byte[3];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 0, 33, (OutputStream) pipedOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test07()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      String string0 = StringEncoder64.encode(byteArray0, 97, 97);
      assertEquals("", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("");
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
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

  @Test
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 7, 7);
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
        StringEncoder64.decode("Lf<wMV|+_BQUJknsrqf", (OutputStream) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: <
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", (OutputStream) null);
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
        StringEncoder64.decode("Q\"h>FJ*%5ym`R4");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: \"
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test17()  throws Throwable  {
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
//  public void test18()  throws Throwable  {
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("AA==", true);
//      StringEncoder64.decode("AA==", (OutputStream) mockFileOutputStream0);
//  }
//
//  @Test
//  public void test19()  throws Throwable  {
//      MockFile mockFile0 = new MockFile("-b`G");
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(mockFile0);
//      StringEncoder64.decode("AAAAAAAAAAAAAAA=", (OutputStream) mockFileOutputStream0);
//      assertEquals(11L, mockFile0.length());
//  }
//
//  @Test
//  public void test20()  throws Throwable  {
//      File file0 = MockFile.createTempFile("DAAA", "1:Jw 7KDI`r0R`");
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0, false);
//      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFileOutputStream0);
//      StringEncoder64.decode("\f\u0000\u0000", (OutputStream) mockPrintStream0);
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
      int int0 = StringEncoder64.decode('1');
      assertEquals(53, int0);
  }

  @Test
  public void test24()  throws Throwable  {
      int int0 = StringEncoder64.decode('t');
      assertEquals(45, int0);
  }

  @Test
  public void test25()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode('\u0088');
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: \u0088
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test26()  throws Throwable  {
      int int0 = StringEncoder64.decode('W');
      assertEquals(22, int0);
  }

//  @Test
//  public void test27()  throws Throwable  {
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("pZBc:e_", true);
//      byte[] byteArray0 = new byte[3];
//      boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte) (-35), (-148), (OutputStream) mockFileOutputStream0);
//      assertTrue(boolean0);
//  }

  @Test
  public void test28()  throws Throwable  {
      byte[] byteArray0 = new byte[47];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 0, 48, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 47
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test29()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      StringEncoder64.encode(byteArray0, 0, 8, (OutputStream) byteArrayOutputStream0);
      assertEquals(12, byteArrayOutputStream0.size());
      assertEquals("AAAAAAAAAAA=", byteArrayOutputStream0.toString());
  }

  @Test
  public void test30()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 0, 24, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test31()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      StringBuffer stringBuffer0 = new StringBuffer(2757);
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 1, 1, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test32()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      StringBuffer stringBuffer0 = new StringBuffer(43);
      StringEncoder64.encode(byteArray0, 2, 2, stringBuffer0);
      assertEquals(4, stringBuffer0.length());
      assertEquals("AAA=", stringBuffer0.toString());
  }

  @Test
  public void test33()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 1, 1144, (StringBuffer) null);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 9
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test34()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 1, 1, (StringBuffer) null);
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
      String string0 = StringEncoder64.decodeStringUTF8("9aBjTK7cT=Z=}]F");
      assertEquals("\uFFFD\uFFFDcL\uFFFD\uFFFDL\u0006", string0);
      assertNotNull(string0);
  }

  @Test
  public void test36()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("XL3L hK9dD");
      assertEquals("\\\uFFFD\u02C4\uFFFD]", string0);
  }

  @Test
  public void test37()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
      assertEquals(48, byteArray0.length);
  }

  @Test
  public void test38()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test39()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8("h4ZO_Yc1QEw6ii&b");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: 
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

//  @Test
//  public void test40()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      try {
//        StringEncoder64.decode("TtIE>d}i(nb", (OutputStream) pipedOutputStream0);
//        fail("Expecting exception: IOException");
//
//      } catch(IOException e) {
//         //
//         // Pipe not connected
//         //
//         //verifyException("java.io.PipedOutputStream", e);
//      }
//  }
//
//  @Test
//  public void test41()  throws Throwable  {
//      byte[] byteArray0 = new byte[0];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode(byteArray0, 1, 1, (OutputStream) pipedOutputStream0);
//        fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//      } catch(ArrayIndexOutOfBoundsException e) {
//         //
//         // 1
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }

  @Test
  public void test42()  throws Throwable  {
      byte[] byteArray0 = new byte[47];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\r\nAAA=", string0);
  }

  @Test
  public void test43()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 19, 19, (OutputStream) null);
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
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 1
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test45()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      StringBuffer stringBuffer0 = new StringBuffer();
      StringBuffer stringBuffer1 = StringEncoder64.encode(byteArray0, 2611, 2611, stringBuffer0);
      assertSame(stringBuffer1, stringBuffer0);
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
