package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_3 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put11(0, 0);
      ByteVector byteVector2 = byteVector1.putShort((-3972));
      ByteVector byteVector3 = byteVector2.putShort(4);
      ByteVector byteVector4 = byteVector1.putUTF8("");
      assertSame(byteVector4, byteVector3);
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putInt((-903));
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12((-283), (-903));
      ByteVector byteVector2 = byteVector0.putInt(273);
      ByteVector byteVector3 = byteVector1.put12((-903), (-903));
      ByteVector byteVector4 = byteVector2.putInt(0);
      assertSame(byteVector4, byteVector3);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putByte(3163);
      ByteVector byteVector2 = byteVector1.put11((byte)0, 268);
      ByteVector byteVector3 = byteVector1.putShort((-1312));
      byteVector3.putByte(268);
      byteVector3.putByte(3163);
      byteVector3.put11((-465), (-5829));
      ByteVector byteVector4 = byteVector2.put12(0, 0);
      assertSame(byteVector2, byteVector4);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put11(0, 0);
      ByteVector byteVector2 = byteVector1.putShort((-3972));
      byteVector2.putShort(4);
      ByteVector byteVector3 = byteVector1.put11(0, 0);
      assertSame(byteVector3, byteVector2);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putShort(3);
      ByteVector byteVector2 = byteVector1.put12((-2928), 24);
      ByteVector byteVector3 = byteVector0.putInt(128);
      ByteVector byteVector4 = byteVector2.putByte(3);
      assertSame(byteVector4, byteVector3);
  }

  @Test
  public void test06()  throws Throwable  {
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
  public void test07()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 392;
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test08()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putShort(0);
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
      byteVector0.length = (-1000);
      // Undeclared exception!
      try { 
        byteVector0.putShort((-1000));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1000
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test10()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putLong(0);
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
      byteVector0.length = (-1);
      // Undeclared exception!
      try { 
        byteVector0.putLong((-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test12()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putInt(745);
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
      byteVector0.length = (-1);
      // Undeclared exception!
      try { 
        byteVector0.putInt((-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test14()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByteArray((byte[]) null, 2543, 2543);
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
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByte(31);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test16()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 844;
      // Undeclared exception!
      try { 
        byteVector0.putByte(844);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test17()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.put12(1358, 1358);
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
      byteVector0.length = (-192);
      // Undeclared exception!
      try { 
        byteVector0.put12((-192), (-192));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -192
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
        byteVector0.put11(109, 109);
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
      byteVector0.length = 406;
      // Undeclared exception!
      try { 
        byteVector0.put11(406, 406);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test21()  throws Throwable  {
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-1444));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test22()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, 3, 63);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test23()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byte[] byteArray0 = new byte[3];
      ByteVector byteVector1 = byteVector0.putByteArray(byteArray0, 0, (byte)0);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test24()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putUTF8("xC!14yv;Ks7j");
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test25()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(3);
      ByteVector byteVector1 = byteVector0.putLong(3);
      byteVector0.putShort(28);
      ByteVector byteVector2 = byteVector1.putUTF8(".");
      assertSame(byteVector2, byteVector0);
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(9);
      ByteVector byteVector1 = byteVector0.putLong(0L);
      ByteVector byteVector2 = byteVector1.put11(0, (-1));
      ByteVector byteVector3 = byteVector2.putLong((-1));
      assertSame(byteVector2, byteVector3);
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(3);
      ByteVector byteVector1 = byteVector0.putShort(3);
      ByteVector byteVector2 = byteVector0.putShort(1);
      byteVector2.putLong(3);
      ByteVector byteVector3 = byteVector1.putShort(28);
      ByteVector byteVector4 = byteVector3.put11((-1), (-1));
      ByteVector byteVector5 = byteVector1.putInt(3);
      byteVector3.putLong((-572L));
      byteVector5.putLong(690L);
      byteVector3.putLong(2392);
      ByteVector byteVector6 = byteVector4.put11(1, 2478);
      byteVector6.putShort(2478);
      ByteVector byteVector7 = byteVector4.putByte(10);
      assertSame(byteVector7, byteVector5);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(3);
      ByteVector byteVector1 = byteVector0.putByte(10);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test29()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, (-1346), (-1346));
      assertSame(byteVector0, byteVector1);
  }
}
