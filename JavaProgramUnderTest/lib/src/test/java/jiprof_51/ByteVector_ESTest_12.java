package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_12 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, 4370, 0);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putUTF8("ckYT`M");
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putUTF8("org.objectweb.asm.jip.ByteVector");
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12(0, 0);
      byteVector0.putByte(958);
      ByteVector byteVector2 = byteVector1.putUTF8("");
      assertSame(byteVector1, byteVector2);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putLong(0L);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putInt((-2286));
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test06()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.put12((-2366), (-2286));
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test07()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12(0, 0);
      byte[] byteArray0 = new byte[7];
      byteVector1.put12((byte) (-21), 0);
      byteVector0.data = byteArray0;
      ByteVector byteVector2 = byteVector1.putByte((byte)12);
      assertSame(byteVector2, byteVector0);
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
      byteVector0.length = (-1815);
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("HMEH}r{m8lIodW*3");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1815
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
        byteVector0.putShort(1);
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
      byteVector0.length = 1808;
      // Undeclared exception!
      try { 
        byteVector0.putShort((-3493));
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
        byteVector0.putLong((-1894L));
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
      byteVector0.length = 558;
      // Undeclared exception!
      try { 
        byteVector0.putLong((-3235L));
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
        byteVector0.putInt((-3171));
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
      byteVector0.length = 1779;
      // Undeclared exception!
      try { 
        byteVector0.putInt(1779);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test16()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByteArray((byte[]) null, 1, 1);
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
      ByteVector byteVector0 = new ByteVector(1);
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByte(1);
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
      byteVector0.length = 1795;
      // Undeclared exception!
      try { 
        byteVector0.putByte(1795);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test19()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.put12(71, 71);
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
      byteVector0.length = 1779;
      // Undeclared exception!
      try { 
        byteVector0.put12(1779, 1779);
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
        byteVector0.put11(111, 111);
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
      byteVector0.length = 1779;
      // Undeclared exception!
      try { 
        byteVector0.put11(1779, 1779);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test23()  throws Throwable  {
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-2339));
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
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, 77, 77);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test25()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, (byte)86, 2034);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byte[] byteArray0 = new byte[6];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, 2190, (byte)0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putShort(0);
      byteVector0.putUTF8("");
      byteVector1.putLong((-5527L));
      ByteVector byteVector2 = byteVector0.putLong((-5527L));
      ByteVector byteVector3 = byteVector2.putLong((-1L));
      ByteVector byteVector4 = byteVector3.putUTF8(" Q\\5_x:&UE;8(kmR");
      assertSame(byteVector4, byteVector1);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putShort(0);
      byteVector0.putLong((-5527L));
      byteVector0.putShort(2034);
      ByteVector byteVector2 = byteVector1.putLong((-5527L));
      assertSame(byteVector0, byteVector2);
  }

  @Test
  public void test29()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putShort(0);
      ByteVector byteVector2 = byteVector1.put12(0, 0);
      ByteVector byteVector3 = byteVector2.putByte((-545));
      ByteVector byteVector4 = byteVector3.putInt(2440);
      assertSame(byteVector3, byteVector4);
  }

  @Test
  public void test30()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putShort(0);
      ByteVector byteVector2 = byteVector1.put12(0, 0);
      byteVector2.putUTF8("");
      ByteVector byteVector3 = byteVector0.put12(0, 0);
      assertSame(byteVector0, byteVector3);
  }

  @Test
  public void test31()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putShort(0);
      ByteVector byteVector2 = byteVector1.put12(0, 0);
      byteVector2.putUTF8("");
      ByteVector byteVector3 = byteVector2.putShort(2034);
      assertSame(byteVector0, byteVector3);
  }

  @Test
  public void test32()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put11(3690, 1);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test33()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(3);
      ByteVector byteVector1 = byteVector0.put11(16, 24);
      byteVector1.put11(0, 1368);
      ByteVector byteVector2 = byteVector1.putShort((-1393));
      ByteVector byteVector3 = byteVector2.putUTF8("");
      byteVector3.putUTF8("");
      ByteVector byteVector4 = byteVector3.put11((byte) (-23), (byte) (-23));
      assertSame(byteVector4, byteVector3);
  }

  @Test
  public void test34()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putByte(1720);
      assertSame(byteVector0, byteVector1);
  }
}
