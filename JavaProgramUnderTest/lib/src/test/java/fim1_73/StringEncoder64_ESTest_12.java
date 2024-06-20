package fim1_73;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
public class StringEncoder64_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("a8_");
      assertEquals(0, byteArray0.length);
  }

  @Test
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      byteArray0[1] = (byte)1;
      StringBuffer stringBuffer0 = new StringBuffer(26);
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)0, 26, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 3
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      byteArray0[0] = (byte)54;
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, (int) (byte)0, 1054);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 9
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[14];
      String string0 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)6);
      assertEquals("AAAAAAAA", string0);
  }

  @Test
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      StringBuffer stringBuffer0 = new StringBuffer("mdr");
      StringEncoder64.encode(byteArray0, 1, 1, stringBuffer0);
      assertEquals(7, stringBuffer0.length());
      assertEquals("mdrAA==", stringBuffer0.toString());
  }

  @Test
  public void test05()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer("(Xr;/o");
      StringBuffer stringBuffer1 = StringEncoder64.encode((byte[]) null, 0, 0, stringBuffer0);
      assertEquals(6, stringBuffer1.length());
  }

//  @Test
//  public void test06()  throws Throwable  {
//      byte[] byteArray0 = new byte[6];
//      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//      boolean boolean0 = StringEncoder64.encode(byteArray0, 1, 63, (OutputStream) pipedOutputStream0);
//      assertFalse(boolean0);
//  }

  @Test
  public void test07()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      String string0 = StringEncoder64.encode(byteArray0, 0, 0);
      assertEquals("", string0);
  }

  @Test
  public void test08()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("", string0);
  }

  @Test
  public void test09()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("`");
      assertEquals("", string0);
  }

  @Test
  public void test10()  throws Throwable  {
      byte[] byteArray0 = StringEncoder64.decode("ACDEFGHIJKLNOPQRSTUVWXYZawcdefghijklmnopqrstuvwxyz01234Z789+/");
      String string0 = StringEncoder64.encode(byteArray0);
      assertEquals("ACDEFGHIJKLNOPQRSTUVWXYZawcdefghijklmnopqrstuvwxyz01234Z789+\r\n", string0);
  }

  @Test
  public void test11()  throws Throwable  {
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
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, 4, 4);
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
        StringEncoder64.decode("86g)JH=ue.G9jff^", (OutputStream) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: )
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test16()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.decode((String) null, (OutputStream) byteArrayOutputStream0);
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
//      try {
//        StringEncoder64.decode("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==", (OutputStream) pipedOutputStream0);
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
//      MockPrintStream mockPrintStream0 = new MockPrintStream("7AE=");
//      StringEncoder64.decode("7AE=", (OutputStream) mockPrintStream0);
//  }
//
//  @Test
//  public void test20()  throws Throwable  {
//      MockFile mockFile0 = new MockFile("=", "");
//      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
//      StringEncoder64.decode("", (OutputStream) mockPrintStream0);
//  }
//
//  @Test
//  public void test21()  throws Throwable  {
//      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==");
//      StringEncoder64.decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", (OutputStream) mockFileOutputStream0);
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
      int int0 = StringEncoder64.decode('+');
      assertEquals(62, int0);
  }

  @Test
  public void test25()  throws Throwable  {
      int int0 = StringEncoder64.decode('u');
      assertEquals(46, int0);
  }

  @Test
  public void test26()  throws Throwable  {
      int int0 = StringEncoder64.decode('A');
      assertEquals(0, int0);
  }

  @Test
  public void test27()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(177);
      byte[] byteArray0 = new byte[7];
      StringEncoder64.encode(byteArray0, (int) (byte)0, 1, (OutputStream) byteArrayOutputStream0);
      assertEquals("AA==", byteArrayOutputStream0.toString());
      assertEquals(4, byteArrayOutputStream0.size());
  }

  @Test
  public void test28()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(0);
      boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)0, (OutputStream) byteArrayOutputStream0);
      assertTrue(boolean0);
  }

  @Test
  public void test29()  throws Throwable  {
      byte[] byteArray0 = new byte[46];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 1, 2591, (OutputStream) byteArrayOutputStream0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 46
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test30()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(5);
      StringEncoder64.encode(byteArray0, 1, 5, (OutputStream) byteArrayOutputStream0);
      assertEquals(8, byteArrayOutputStream0.size());
      assertEquals("AAAAAAA=", byteArrayOutputStream0.toString());
  }

  @Test
  public void test31()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      // Undeclared exception!
      try { 
        StringEncoder64.encode((byte[]) null, (-1990), 1, (OutputStream) byteArrayOutputStream0);
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
      StringBuffer stringBuffer0 = new StringBuffer();
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 2, 2, stringBuffer0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 2
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test33()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 1, 63, (StringBuffer) null);
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
        StringEncoder64.encode((byte[]) null, 255, 255, (StringBuffer) null);
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
      // Undeclared exception!
      try { 
        StringEncoder64.decodeStringUTF8(" R\"L)Dc~zZNk};cPVg");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: \"
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test36()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringEncoder64.decode("=Ww0O/l+\"jX`XmJ");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // unexpected code: \"
         //
         //verifyException("osa.ora.server.utils.StringEncoder64", e);
      }
  }

  @Test
  public void test37()  throws Throwable  {
      int int0 = StringEncoder64.decode('6');
      assertEquals(58, int0);
  }

  @Test
  public void test38()  throws Throwable  {
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
  public void test39()  throws Throwable  {
      String string0 = StringEncoder64.decodeStringUTF8("+Jn=iceQsvk");
      assertEquals("\uFFFD\uFFFD", string0);
      assertNotNull(string0);
  }

  @Test
  public void test40()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("");
      assertEquals("", string0);
  }

  @Test
  public void test41()  throws Throwable  {
      String string0 = StringEncoder64.encodeStringUTF8("C=");
      assertEquals("Qz0=", string0);
      assertNotNull(string0);
  }

  @Test
  public void test42()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        StringEncoder64.encode(byteArray0, 42, 42, (OutputStream) null);
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
      byte[] byteArray0 = new byte[9];
      String string0 = StringEncoder64.encode(byteArray0, 2, 2);
      assertEquals("AAA=", string0);
  }

  @Test
  public void test44()  throws Throwable  {
      StringBuffer stringBuffer0 = new StringBuffer();
      StringBuffer stringBuffer1 = StringEncoder64.encode((byte[]) null, 7, 7, stringBuffer0);
      assertSame(stringBuffer1, stringBuffer0);
  }

  @Test
  public void test45()  throws Throwable  {
      StringEncoder64 stringEncoder64_0 = new StringEncoder64();
  }
}
