package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_1 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, (byte)0, 64);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      byteVector0.put12(1, 2538);
      ByteVector byteVector1 = byteVector0.putUTF8("");
      ByteVector byteVector2 = byteVector1.put12(1, 0);
      byteVector1.putLong(1);
      byteVector1.putUTF8("");
      ByteVector byteVector3 = byteVector2.put11((byte) (-64), 8);
      byteVector3.putShort(113);
      ByteVector byteVector4 = byteVector2.putUTF8("");
      assertSame(byteVector4, byteVector3);
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putLong((-1300));
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(12);
      ByteVector byteVector1 = byteVector0.putUTF8("");
      byteVector1.putShort((-2307));
      ByteVector byteVector2 = byteVector1.putLong(0L);
      assertSame(byteVector0, byteVector2);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putInt((-1012));
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      byteVector0.putInt(1);
      ByteVector byteVector1 = byteVector0.putUTF8("");
      ByteVector byteVector2 = byteVector1.putShort((byte) (-64));
      assertSame(byteVector2, byteVector1);
  }

  @Test
  public void test06()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(188);
      byte[] byteArray0 = new byte[4];
      byteVector0.data = byteArray0;
      ByteVector byteVector1 = byteVector0.putUTF8("M7^10wl/(,26oO$");
      byteVector0.put12(188, 188);
      ByteVector byteVector2 = byteVector0.putLong(188);
      byteVector0.putUTF8("},5?Z%JDc9TuA:e");
      byteVector2.put11(0, 965);
      ByteVector byteVector3 = byteVector1.putShort((byte) (-71));
      byteVector3.putUTF8("M7^10wl/(,26oO$");
      ByteVector byteVector4 = byteVector3.put11(2, 0);
      assertSame(byteVector0, byteVector4);
  }

  @Test
  public void test07()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putByte(2182);
      assertSame(byteVector1, byteVector0);
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
      byteVector0.length = 1684;
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("|VBxfi ");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test10()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putShort((-859));
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
      byteVector0.length = (-4481);
      // Undeclared exception!
      try { 
        byteVector0.putShort((-4481));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -4481
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
        byteVector0.putLong(1553L);
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
      byteVector0.length = (-1084);
      // Undeclared exception!
      try { 
        byteVector0.putLong((-1084));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1084
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
        byteVector0.putInt(192);
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
      byteVector0.length = 692;
      // Undeclared exception!
      try { 
        byteVector0.putInt(692);
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
        byteVector0.putByteArray((byte[]) null, (-876), (-876));
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
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, 16, 16);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test18()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByte((-876));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test19()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 640;
      // Undeclared exception!
      try { 
        byteVector0.putByte(640);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test20()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.put12(463, 463);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test21()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 692;
      // Undeclared exception!
      try { 
        byteVector0.put12(692, 692);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test22()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.put11(2629, 2629);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test23()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-6671);
      // Undeclared exception!
      try { 
        byteVector0.put11((-6671), (-6671));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -6671
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test24()  throws Throwable  {
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-1));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test25()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(188);
      ByteVector byteVector1 = byteVector0.putByteArray(byteVector0.data, (byte)31, (byte)31);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putInt(1);
      ByteVector byteVector2 = byteVector1.put12(0, 0);
      byteVector2.put12(15, (-1063));
      ByteVector byteVector3 = byteVector2.putUTF8("");
      assertSame(byteVector3, byteVector1);
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      byteVector0.putByteArray((byte[]) null, 3264, 15);
      ByteVector byteVector1 = byteVector0.put12(15, (-1063));
      ByteVector byteVector2 = byteVector0.putLong(1);
      assertSame(byteVector2, byteVector1);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putInt(1);
      ByteVector byteVector2 = byteVector1.put12(0, 0);
      byteVector2.put12(15, (-1063));
      ByteVector byteVector3 = byteVector0.putInt(1);
      assertSame(byteVector0, byteVector3);
  }

  @Test
  public void test29()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.put12(1, 1);
      ByteVector byteVector2 = byteVector1.putUTF8("");
      ByteVector byteVector3 = byteVector0.put12(673, 44);
      ByteVector byteVector4 = byteVector3.put12(44, 44);
      ByteVector byteVector5 = byteVector2.putUTF8("//s d]^UGe(yQHm ");
      ByteVector byteVector6 = byteVector1.putInt(1);
      byteVector2.putShort(1);
      ByteVector byteVector7 = byteVector5.put12(1, 59);
      byteVector7.putLong(0L);
      ByteVector byteVector8 = byteVector6.putShort(59);
      byteVector4.putLong(1);
      ByteVector byteVector9 = byteVector0.put12(673, 59);
      assertSame(byteVector9, byteVector8);
  }

  @Test
  public void test30()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(127);
      ByteVector byteVector1 = byteVector0.putShort(127);
      ByteVector byteVector2 = byteVector1.putShort(16);
      byte[] byteArray0 = new byte[5];
      byteVector2.data = byteArray0;
      byteVector0.putShort((-1));
      ByteVector byteVector3 = byteVector0.putInt(48);
      assertSame(byteVector0, byteVector3);
  }

  @Test
  public void test31()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.put11(1, 1);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test32()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putInt(1);
      byteVector1.put12(0, 0);
      ByteVector byteVector2 = byteVector0.putByte(0);
      assertSame(byteVector0, byteVector2);
  }
}
