package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.OutputStream;

public class StringEncoder64_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
      assertEquals("\u0000\u0010\uFFFD\u0010Q\uFFFD \uFFFD\uFFFD0\u04CFA\u0014\uFFFDQU\uFFFDa\uFFFD\uFFFDq\u05DF\uFFFD\u0018\uFFFD\uFFFDY\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\u06EF\uFFFD\u001C\uFFFD\uFFFD]\uFFFD\u37BB\uFFFD\u07FF", string0);
  }

  @Test
  public void test01()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer(1);
      byte[] byteArray0 = new byte[6];
      byteArray0[3] = (byte)14;
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 2, 575, stringBuffer0);
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
      StringBuffer stringBuffer0 = new StringBuffer(1);
      byte[] byteArray0 = new byte[6];
      byteArray0[2] = (byte)2;
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 2, 575, stringBuffer0);
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
        StringEncoder64.encode(byteArray0, (int) (byte)65, (int) (byte)68);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 65
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)2, (int) (byte)2);
      assertEquals("AAA=", string0);
  }

  @Test
  public void test05()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test06()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      StringBuffer stringBuffer0 = new StringBuffer("osa.ora.server.utils.StringEncoder64");
      StringBuffer stringBuffer1 = StringEncoder64.encode(byteArray0, 1077, 1077, stringBuffer0);
      assertSame(stringBuffer1, stringBuffer0);
  }

//  @Test
//  public void test07()  throws Throwable  {
//      byte[] byteArray0 = StringEncoder64.decode("QUhDREVGR0hJSktMTU5PUFFAU1RVVlhZWmFiY2RlZmdoaWprbG1ub3BxcnN0\r\ndXZ3eHl6MDEyMzQ1Njc4OSsv");
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      DataOutputStream dataOutputStream0 = new DataOutputStream(pipedOutputStream0);
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 47, 455, (OutputStream) dataOutputStream0);
//      assertFalse(boolean0);
//      assertEquals(63, byteArray0.length);
//  }

  @Test
  public void test08()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      String string0 = StringEncoder64.encode(byteArray0, (-73), (-73));
      assertEquals("", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("l^&");
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test10()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test11()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("WF=jOKNr");
      assertArrayEquals(new byte[] {(byte)88}, byteArray0);
  }

  @Test
  public void test12()  throws Throwable  {
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
//  public void test13()  throws Throwable  {
//      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
//      // Undeclared exception!
//      try {
//        StringEncoder64.encode((byte[]) null, (-1196), 65, (OutputStream) byteArrayOutputStream0);
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
  public void test14()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (int) (byte)0, (int) (byte)0);
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
  public void test16()  throws Throwable  {
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

//  @Test
//  public void test17()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      // Undeclared exception!
//      try {
//        StringEncoder64.decode("!smwgDO^|{jr", (OutputStream) pipedOutputStream0);
//        fail("Expecting exception: RuntimeException");
//
//      } catch(RuntimeException e) {
//         //
//         // unexpected code: !
//         //
//         //verifyException("osa.ora.server.utils.StringEncoder64", e);
//      }
//  }
//
//  @Test
//  public void test18()  throws Throwable  {
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
//
//  @Test
//  public void test19()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      try {
//        StringEncoder64.decode("AHCDEFGHIJKLMNOPQ@STUVXYZabcdefghijklmnopqrstuvwxyz0123456789+/", (OutputStream) pipedOutputStream0);
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
  public void test20()  throws Throwable  {
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
//  public void test21()  throws Throwable  {
//      MockFile mockFile0 = new MockFile("1 Lp+r}");
//      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
//      BufferedOutputStream bufferedOutputStream0 = new BufferedOutputStream(mockPrintStream0, 57);
//      StringEncoder64.decode("SSohKTwnNXBRXEJkTCYsOWlbdA==", (OutputStream) bufferedOutputStream0);
//  }
//
//  @Test
//  public void test22()  throws Throwable  {
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      MockPrintStream mockPrintStream0 = new MockPrintStream(pipedOutputStream0);
//      StringEncoder64.decode("YD3X", (OutputStream) mockPrintStream0);
//  }

  @Test
  public void test23()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream((byte)102);
      StringEncoder64.decode("QUJDREVGR0hJSktMTU5QUVJTVFVWV1hZWmFiY2RlZmdoaWprbG1ub3BxcnN0\r\ndXd4eXowMTIzNDU2Nzg5Ky8=", (OutputStream) byteArrayOutputStream0);
      assertEquals(62, byteArrayOutputStream0.size());
      assertEquals("ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuwxyz0123456789+/", byteArrayOutputStream0.toString());
  }

  @Test
  public void test24()  throws Throwable  {
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test25()  throws Throwable  {
      int int0 = StringEncoder64.decode('=');
      assertEquals(0, int0);
  }

  @Test
  public void test26()  throws Throwable  {
      int int0 = StringEncoder64.decode('1');
      assertEquals(53, int0);
  }

  @Test
  public void test27()  throws Throwable  {
      int int0 = StringEncoder64.decode('x');
      assertEquals(49, int0);
  }

  @Test
  public void test28()  throws Throwable  {
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
  public void test29()  throws Throwable  {
      int int0 = StringEncoder64.decode('/');
      assertEquals(63, int0);
  }

  @Test
  public void test30()  throws Throwable  {
      int int0 = StringEncoder64.decode('M');
      assertEquals(12, int0);
  }

//  @Test
//  public void test31()  throws Throwable  {
//      byte[] byteArray0 = new byte[2];
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("g=)J", false);
//      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFileOutputStream0, false);
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 1, 1, (OutputStream) mockPrintStream0);
//      assertTrue(boolean0);
//  }

  @Test
  public void test32()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[5];
      StringEncoder64.encode(byteArray0, (int) (byte)2, (int) (byte)2, (OutputStream) byteArrayOutputStream0);
      assertEquals("AAA=", byteArrayOutputStream0.toString());
  }

//  @Test
//  public void test33()  throws Throwable  {
//      byte[] byteArray0 = new byte[2];
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("g=)J", false);
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 90, 0, (OutputStream) mockFileOutputStream0);
//      assertTrue(boolean0);
//  }

  @Test
  public void test34()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer(1);
      byte[] byteArray0 = new byte[1];
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
  public void test35()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      StringBuffer stringBuffer0 = new StringBuffer();
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)0, 575, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 2
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test36()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-4120), (-4120), (StringBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test37()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8(" :-ilh.QHe");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: :
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test38()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("GKB/14u0{[!Z|Fg;A");
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
      String string0 = StringEncoder64.encodeStringUTF8("*");
      assertNotNull(string0);
      assertEquals("Kg==", string0);
  }

  @Test
  public void test40()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("AAA=", string0);
      assertNotNull(string0);
  }

  @Test
  public void test41()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[49];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)0, 2366, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 49
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test42()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-592), (-592), (OutputStream) null);
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
      StringBuffer stringBuffer0 = new StringBuffer(42);
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)62, 2, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 62
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test44()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer();
      byte[] byteArray0 = new byte[0];
      StringBuffer stringBuffer1 = StringEncoder64.encode(byteArray0, (-7130), (-7130), stringBuffer0);
      assertEquals("", stringBuffer1.toString());
  }

  @Test
  public void test45()  throws Throwable  {
      byte[] byteArray0 = new byte[11];
      String string0 = StringEncoder64.encode(byteArray0, 1, 1);
      assertEquals("AA==", string0);
  }

  @Test
  public void test46()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }

  @Test
  public void test47()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("#Wq+vhk%~");
      assertNotNull(string0);
      assertEquals("I1dxK3ZoayV+", string0);
  }
}
