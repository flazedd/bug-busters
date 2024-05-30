package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_8 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putShort(1);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byte[] byteArray0 = new byte[2];
      ByteVector byteVector1 = byteVector0.putByteArray(byteArray0, (byte)0, 0);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(24);
      ByteVector byteVector1 = byteVector0.putUTF8("acaK");
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 1;
      ByteVector byteVector1 = byteVector0.putByte(64);
      ByteVector byteVector2 = byteVector0.putInt((-827));
      byteVector2.putUTF8("org.objectweb.asm.jip.ByteVector");
      ByteVector byteVector3 = byteVector2.putUTF8("m!f60JsVX");
      byteVector3.putUTF8("m!f60JsVX");
      ByteVector byteVector4 = byteVector1.putUTF8("");
      assertSame(byteVector0, byteVector4);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(40);
      ByteVector byteVector1 = byteVector0.putByte(0);
      ByteVector byteVector2 = byteVector1.putShort(0);
      ByteVector byteVector3 = byteVector2.putUTF8("");
      ByteVector byteVector4 = byteVector3.put11(61, 127);
      ByteVector byteVector5 = byteVector0.putUTF8("R0M7;e");
      ByteVector byteVector6 = byteVector5.putLong(0L);
      ByteVector byteVector7 = byteVector4.putInt((-2073));
      byteVector7.putUTF8("R0M7;e");
      byteVector6.putByte((byte) (-55));
      ByteVector byteVector8 = byteVector6.putInt(261);
      assertSame(byteVector8, byteVector6);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12((-306), (-306));
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test06()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putShort(121);
      ByteVector byteVector2 = byteVector1.putByte(121);
      byteVector2.put11(121, 121);
      byteVector2.put12(32, 0);
      byteVector2.putByte(2696);
      ByteVector byteVector3 = byteVector1.putInt(0);
      byteVector3.putByte(78);
      ByteVector byteVector4 = byteVector1.put11(128, (-1191));
      assertSame(byteVector4, byteVector0);
  }

  @Test
  public void test07()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putUTF8("");
      ByteVector byteVector2 = byteVector1.putUTF8("");
      ByteVector byteVector3 = byteVector0.putUTF8("");
      ByteVector byteVector4 = byteVector3.putUTF8("");
      ByteVector byteVector5 = byteVector0.putByte((-1366));
      byteVector5.putInt((-1366));
      ByteVector byteVector6 = byteVector0.putShort((-1366));
      byteVector6.put11((-1366), 32);
      byteVector0.putShort((-1366));
      ByteVector byteVector7 = byteVector0.putLong(597L);
      byteVector7.put11((-1366), (-1366));
      ByteVector byteVector8 = byteVector0.putShort(0);
      byteVector8.putLong(0L);
      ByteVector byteVector9 = byteVector2.putByte(0);
      byteVector4.putShort(0);
      ByteVector byteVector10 = byteVector9.putLong(0L);
      ByteVector byteVector11 = byteVector4.putUTF8("ZH&6/ 36n7");
      ByteVector byteVector12 = byteVector11.putByte((-1366));
      assertSame(byteVector12, byteVector10);
  }

  @Test
  public void test08()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      // Undeclared exception!
      try { 
        byteVector0.putUTF8((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test09()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-1695);
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("j ");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1695
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putShort((-377));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test11()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 3089;
      // Undeclared exception!
      try { 
        byteVector0.putShort(3089);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test12()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putLong(0L);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test13()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 3150;
      // Undeclared exception!
      try { 
        byteVector0.putLong(3150);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test14()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putInt((-1718));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test15()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-3915);
      // Undeclared exception!
      try { 
        byteVector0.putInt((-3915));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -3915
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test16()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByteArray((byte[]) null, (-1718), (-1718));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test17()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByte(960);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test18()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-3915);
      // Undeclared exception!
      try { 
        byteVector0.putByte((-3915));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -3915
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test19()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.put12(267, 267);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test20()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 574;
      // Undeclared exception!
      try { 
        byteVector0.put12(2928, 2928);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test21()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.put11(3631, 3);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test22()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-3915);
      // Undeclared exception!
      try { 
        byteVector0.put11((-3915), (-3915));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -3915
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test23()  throws Throwable  {
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-202));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test24()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(40);
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, (-2073), 2682);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test25()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(40);
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, (-1848), 0);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(24);
      ByteVector byteVector1 = byteVector0.putUTF8("org.objectweb.asm.jip.ByteVector");
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(8);
      ByteVector byteVector1 = byteVector0.put12(8, 0);
      ByteVector byteVector2 = byteVector0.put12(0, 8);
      byteVector1.putShort(35);
      ByteVector byteVector3 = byteVector0.put11(521, 8);
      assertSame(byteVector3, byteVector2);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(8);
      ByteVector byteVector1 = byteVector0.put12(8, 0);
      ByteVector byteVector2 = byteVector0.put12(0, 8);
      ByteVector byteVector3 = byteVector1.putInt(521);
      byteVector1.putShort(35);
      ByteVector byteVector4 = byteVector2.putLong((-1));
      ByteVector byteVector5 = byteVector4.put11(521, 8);
      byteVector3.putShort(1);
      ByteVector byteVector6 = byteVector1.putLong(8);
      byteVector6.putByte(192);
      ByteVector byteVector7 = byteVector3.putUTF8("ZH&6/ 36n7");
      assertSame(byteVector7, byteVector5);
  }

  @Test
  public void test29()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byte[] byteArray0 = new byte[6];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, 1327, 1327);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }
}
