/*
 * This file was automatically generated by EvoSuite
 * Tue May 28 16:39:13 GMT 2024
 */

package fim1_73;

import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StringEncoder64_ESTest_3 {

    @Test
    public void test00()  throws Throwable  {
        byte[] byteArray0 = StringEncoder64.decode("dKPv,&!");
        assertArrayEquals(new byte[] {(byte)116, (byte) (-93), (byte) (-17)}, byteArray0);
    }

    @Test
    public void test01()  throws Throwable  {
        byte[] byteArray0 = new byte[5];
        byteArray0[1] = (byte)35;
        StringBuffer stringBuffer0 = new StringBuffer("");
        // Undeclared exception!
        try {
            StringEncoder64.encode(byteArray0, 0, 3662, stringBuffer0);
            fail("Expecting exception: ArrayIndexOutOfBoundsException");

        } catch(ArrayIndexOutOfBoundsException e) {
            //
            // 5
            //
            //verifyException("osa.ora.server.utils.StringEncoder64", e);
        }
    }

    @Test
    public void test02()  throws Throwable  {
        byte[] byteArray0 = new byte[5];
        byteArray0[0] = (byte) (-56);
        StringBuffer stringBuffer0 = new StringBuffer("");
        // Undeclared exception!
        try {
            StringEncoder64.encode(byteArray0, 0, 3662, stringBuffer0);
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
        byte[] byteArray0 = new byte[8];
        StringBuffer stringBuffer0 = new StringBuffer();
        StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)3, stringBuffer0);
        assertEquals(4, stringBuffer0.length());
        assertEquals("AAAA", stringBuffer0.toString());
    }

    @Test
    public void test04()  throws Throwable  {
        byte[] byteArray0 = new byte[9];
        String string0 = StringEncoder64.encode(byteArray0, (int) (byte)7, 1);
        assertEquals("AA==", string0);
    }

    @Test
    public void test05()  throws Throwable  {
        String string0 = StringEncoder64.encodeStringUTF8("");
        assertEquals("", string0);
    }

//    @Test
//    public void test06()  throws Throwable  {
//        byte[] byteArray0 = new byte[7];
//        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//        boolean boolean0 = StringEncoder64.encode(byteArray0, (int) (byte)0, 62, (OutputStream) pipedOutputStream0);
//        assertFalse(boolean0);
//    }

    @Test
    public void test07()  throws Throwable  {
        byte[] byteArray0 = new byte[7];
        String string0 = StringEncoder64.encode(byteArray0, 4, (int) (byte)2);
        assertEquals("AAA=", string0);
    }

    @Test
    public void test08()  throws Throwable  {
        byte[] byteArray0 = StringEncoder64.decode("C=");
        String string0 = StringEncoder64.encode(byteArray0);
        assertEquals("", string0);
    }

    @Test
    public void test09()  throws Throwable  {
        String string0 = StringEncoder64.decodeStringUTF8("");
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
            StringEncoder64.decodeStringUTF8("=KA5U|)`a)t\"eG{-");
            fail("Expecting exception: RuntimeException");

        } catch(RuntimeException e) {
            //
            // unexpected code: |
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

//    @Test
//    public void test16()  throws Throwable  {
//        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//        try {
//            StringEncoder64.decode("UTF8", (OutputStream) pipedOutputStream0);
//            fail("Expecting exception: IOException");
//
//        } catch(IOException e) {
//            //
//            // Pipe not connected
//            //
//            //verifyException("java.io.PipedOutputStream", e);
//        }
//    }

    @Test
    public void test17()  throws Throwable  {
        // Undeclared exception!
        try {
            StringEncoder64.decode("a,!CPL@x28#x@<");
            fail("Expecting exception: RuntimeException");

        } catch(RuntimeException e) {
            //
            // unexpected code: ,
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

    @Test
    public void test19()  throws Throwable  {
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(82);
        StringEncoder64.decode("fFstc18+WXYzeHA=", (OutputStream) byteArrayOutputStream0);
        assertEquals(11, byteArrayOutputStream0.size());
        assertEquals("|[-s_>Yv3xp", byteArrayOutputStream0.toString());
    }

//    @Test
//    public void test20()  throws Throwable  {
//        MockFile mockFile0 = new MockFile("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
//        MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
//        StringEncoder64.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", (OutputStream) mockPrintStream0);
//        assertEquals(48L, mockFile0.length());
//    }

    @Test
    public void test21()  throws Throwable  {
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream((byte)39);
        StringEncoder64.decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", (OutputStream) byteArrayOutputStream0);
        assertEquals(64, byteArrayOutputStream0.size());
        assertEquals("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", byteArrayOutputStream0.toString());
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
        int int0 = StringEncoder64.decode('0');
        assertEquals(52, int0);
    }

    @Test
    public void test26()  throws Throwable  {
        int int0 = StringEncoder64.decode('a');
        assertEquals(26, int0);
    }

    @Test
    public void test27()  throws Throwable  {
        // Undeclared exception!
        try {
            StringEncoder64.decode('*');
            fail("Expecting exception: RuntimeException");

        } catch(RuntimeException e) {
            //
            // unexpected code: *
            //
            //verifyException("osa.ora.server.utils.StringEncoder64", e);
        }
    }

    @Test
    public void test28()  throws Throwable  {
        int int0 = StringEncoder64.decode('A');
        assertEquals(0, int0);
    }

    @Test
    public void test29()  throws Throwable  {
        byte[] byteArray0 = StringEncoder64.decode("C=");
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(32);
        // Undeclared exception!
        try {
            StringEncoder64.encode(byteArray0, 452, 1, (OutputStream) byteArrayOutputStream0);
            fail("Expecting exception: ArrayIndexOutOfBoundsException");

        } catch(ArrayIndexOutOfBoundsException e) {
            //
            // 452
            //
            //verifyException("osa.ora.server.utils.StringEncoder64", e);
        }
    }

//    @Test
//    public void test30()  throws Throwable  {
//        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
//        // Undeclared exception!
//        try {
//            StringEncoder64.encode((byte[]) null, 2, 2, (OutputStream) pipedOutputStream0);
//            fail("Expecting exception: NullPointerException");
//
//        } catch(NullPointerException e) {
//            //
//            // no message in exception (getMessage() returned null)
//            //
//            //verifyException("osa.ora.server.utils.StringEncoder64", e);
//        }
//    }

    @Test
    public void test31()  throws Throwable  {
        byte[] byteArray0 = new byte[7];
        StringBuffer stringBuffer0 = new StringBuffer((CharSequence) "AAA=");
        // Undeclared exception!
        try {
            StringEncoder64.encode(byteArray0, (-1), 1, stringBuffer0);
            fail("Expecting exception: ArrayIndexOutOfBoundsException");

        } catch(ArrayIndexOutOfBoundsException e) {
            //
            // -1
            //
            //verifyException("osa.ora.server.utils.StringEncoder64", e);
        }
    }

    @Test
    public void test32()  throws Throwable  {
        // Undeclared exception!
        try {
            StringEncoder64.encode((byte[]) null, 40, 40, (StringBuffer) null);
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
        byte[] byteArray0 = new byte[7];
        String string0 = StringEncoder64.encode(byteArray0);
        assertNotNull(string0);
        assertEquals("AAAAAAAAAA==", string0);
    }

    @Test
    public void test34()  throws Throwable  {
        byte[] byteArray0 = StringEncoder64.decode(" ");
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(1);
        boolean boolean0 = StringEncoder64.encode(byteArray0, 330, (-1782), (OutputStream) byteArrayOutputStream0);
        assertTrue(boolean0);
    }

    @Test
    public void test35()  throws Throwable  {
        // Undeclared exception!
        try {
            StringEncoder64.decode("b,`39KfsL&Xoo|", (OutputStream) null);
            fail("Expecting exception: RuntimeException");

        } catch(RuntimeException e) {
            //
            // unexpected code: ,
            //
            //verifyException("osa.ora.server.utils.StringEncoder64", e);
        }
    }

    @Test
    public void test36()  throws Throwable  {
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
    public void test37()  throws Throwable  {
        String string0 = StringEncoder64.encodeStringUTF8("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");
        assertNotNull(string0);
        assertEquals("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJz\r\ndHV2d3h5ejAxMjM0NTY3ODkrLw==", string0);
    }

    @Test
    public void test38()  throws Throwable  {
        String string0 = StringEncoder64.encodeStringUTF8("C=");
        assertEquals("Qz0=", string0);
        assertNotNull(string0);
    }

//    @Test
//    public void test39()  throws Throwable  {
//        byte[] byteArray0 = new byte[56];
//        MockPrintStream mockPrintStream0 = new MockPrintStream("Z");
//        // Undeclared exception!
//        try {
//            StringEncoder64.encode(byteArray0, 0, 1570, (OutputStream) mockPrintStream0);
//            fail("Expecting exception: ArrayIndexOutOfBoundsException");
//
//        } catch(ArrayIndexOutOfBoundsException e) {
//            //
//            // 56
//            //
//            //verifyException("osa.ora.server.utils.StringEncoder64", e);
//        }
//    }

    @Test
    public void test40()  throws Throwable  {
        // Undeclared exception!
        try {
            StringEncoder64.encode((byte[]) null, (-1398), (-1398), (OutputStream) null);
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
        byte[] byteArray0 = new byte[0];
        // Undeclared exception!
        try {
            StringEncoder64.encode(byteArray0, 128, 1);
            fail("Expecting exception: ArrayIndexOutOfBoundsException");

        } catch(ArrayIndexOutOfBoundsException e) {
            //
            // 128
            //
            //verifyException("osa.ora.server.utils.StringEncoder64", e);
        }
    }

    @Test
    public void test42()  throws Throwable  {
        byte[] byteArray0 = new byte[8];
        StringBuffer stringBuffer0 = new StringBuffer();
        StringEncoder64.encode(byteArray0, 2, 2, stringBuffer0);
        assertEquals(4, stringBuffer0.length());
        assertEquals("AAA=", stringBuffer0.toString());
    }

    @Test
    public void test43()  throws Throwable  {
        StringBuffer stringBuffer0 = new StringBuffer();
        byte[] byteArray0 = new byte[7];
        StringBuffer stringBuffer1 = StringEncoder64.encode(byteArray0, (int) (byte)0, (int) (byte)0, stringBuffer0);
        assertEquals(0, stringBuffer1.length());
    }

    @Test
    public void test44()  throws Throwable  {
        byte[] byteArray0 = new byte[7];
        String string0 = StringEncoder64.encode(byteArray0, 43, (int) (byte) (-103));
        assertEquals("", string0);
    }

    @Test
    public void test45()  throws Throwable  {
        String string0 = StringEncoder64.decodeStringUTF8("W7=dfYr");
        assertEquals("[", string0);
    }

    @Test
    public void test46()  throws Throwable  {
        StringEncoder64 stringEncoder64_0 = new StringEncoder64();
    }

    @Test
    public void test47()  throws Throwable  {
        String string0 = StringEncoder64.encodeStringUTF8(";B,qq)8}jj-Q+9");
        assertEquals("O39CLHFxKTh9amotUSs5", string0);
    }
}
