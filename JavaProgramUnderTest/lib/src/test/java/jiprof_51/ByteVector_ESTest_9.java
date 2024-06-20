package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_9 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putUTF8("");
      ByteVector byteVector2 = byteVector1.put11(245, 1473);
      assertSame(byteVector0, byteVector2);
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putLong(0L);
      ByteVector byteVector2 = byteVector0.put12((-1407), (-1500));
      ByteVector byteVector3 = byteVector1.putByte((-1500));
      byteVector3.put11((-1407), 0);
      byteVector3.putUTF8("F0Qy%{CjZ");
      byteVector1.put12((-1), (-1));
      ByteVector byteVector4 = byteVector0.putLong(0L);
      byteVector4.putShort((-1407));
      byteVector1.putLong((-1376L));
      byte[] byteArray0 = new byte[4];
      ByteVector byteVector5 = byteVector2.putShort(8);
      // Undeclared exception!
      try { 
        byteVector5.putByteArray(byteArray0, (-1407), 15);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putInt((-1));
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(15);
      ByteVector byteVector1 = byteVector0.put12((-1), (-1));
      ByteVector byteVector2 = byteVector1.putLong((-780L));
      ByteVector byteVector3 = byteVector2.putInt(15);
      assertSame(byteVector0, byteVector3);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putLong(0L);
      byteVector0.put12((-1407), (-1500));
      ByteVector byteVector2 = byteVector0.putInt(0);
      byteVector2.put11((-1407), 0);
      byteVector2.putUTF8("F0Qy%{CjZ");
      byteVector1.put12((-1), (-1));
      ByteVector byteVector3 = byteVector0.putLong(0L);
      ByteVector byteVector4 = byteVector3.putShort((-1407));
      byteVector1.putLong((-1376L));
      byteVector4.putInt(0);
      byteVector3.putLong(0);
      ByteVector byteVector5 = byteVector4.putShort((-1));
      assertSame(byteVector3, byteVector5);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putByte(0);
      ByteVector byteVector2 = byteVector1.putInt(0);
      ByteVector byteVector3 = byteVector2.put12((-913), 0);
      ByteVector byteVector4 = byteVector3.put11(0, (-913));
      assertSame(byteVector4, byteVector2);
  }

  @Test
  public void test06()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.put12((-1), 0);
      ByteVector byteVector2 = byteVector1.putShort(0);
      ByteVector byteVector3 = byteVector2.putByte(1);
      byteVector0.put12(0, (-2061));
      ByteVector byteVector4 = byteVector3.put12(452, 452);
      assertSame(byteVector3, byteVector4);
  }

  @Test
  public void test07()  throws Throwable  {
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
  public void test08()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-306);
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("org.objectweb.asm.jip.ByteVector");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -306
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test09()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
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
  public void test10()  throws Throwable  {
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
  public void test11()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-3910);
      // Undeclared exception!
      try { 
        byteVector0.putLong((-1L));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -3910
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
        byteVector0.putInt(876);
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
      byteVector0.length = 251;
      // Undeclared exception!
      try { 
        byteVector0.putInt(251);
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
        byteVector0.putByteArray((byte[]) null, 971, 971);
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
  public void test16()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 596;
      // Undeclared exception!
      try { 
        byteVector0.putByte(596);
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
        byteVector0.put12(985, 985);
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
      byteVector0.length = 589;
      // Undeclared exception!
      try { 
        byteVector0.put12(589, 589);
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
        byteVector0.put11(84, 84);
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
      byteVector0.length = (-650);
      // Undeclared exception!
      try { 
        byteVector0.put11(2296, 2296);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -650
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test21()  throws Throwable  {
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-21));
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
      ByteVector byteVector1 = byteVector0.putUTF8("}wP Z6");
      ByteVector byteVector2 = byteVector1.putInt(1);
      assertSame(byteVector1, byteVector2);
  }

  @Test
  public void test23()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, 404, 404);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test24()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byte[] byteArray0 = new byte[4];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, (-1407), 15);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test25()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putUTF8("}wP Z6");
      byteVector0.put11(49, 0);
      ByteVector byteVector2 = byteVector0.putUTF8("Wl|(");
      assertSame(byteVector2, byteVector1);
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putLong(1);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put11(49, 0);
      ByteVector byteVector2 = byteVector0.putUTF8("}wP Z6");
      byteVector0.put11(49, 0);
      ByteVector byteVector3 = byteVector2.putLong(757L);
      assertSame(byteVector3, byteVector1);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 596;
      // Undeclared exception!
      try { 
        byteVector0.putShort(596);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }
}
