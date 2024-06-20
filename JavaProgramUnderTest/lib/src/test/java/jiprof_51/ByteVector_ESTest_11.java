package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_11 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.put11((-55), 0);
      byte[] byteArray0 = new byte[7];
      byteVector1.data = byteArray0;
      ByteVector byteVector2 = byteVector1.putShort((-216));
      ByteVector byteVector3 = byteVector2.putUTF8("7@p>k4uW");
      assertSame(byteVector3, byteVector2);
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, 1345, 0);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(2);
      ByteVector byteVector1 = byteVector0.putUTF8("");
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12(0, 0);
      ByteVector byteVector2 = byteVector1.putByte(0);
      ByteVector byteVector3 = byteVector2.putShort(0);
      byteVector3.putInt((-702));
      ByteVector byteVector4 = byteVector3.putInt(0);
      byteVector0.putUTF8("");
      ByteVector byteVector5 = byteVector0.putLong(0L);
      assertSame(byteVector5, byteVector4);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12(0, 0);
      byteVector1.putByte(0);
      byteVector0.putInt((-702));
      ByteVector byteVector2 = byteVector1.putInt(0);
      assertSame(byteVector1, byteVector2);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.put12(1967, 1967);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test06()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byteVector0.putByte((-205));
      ByteVector byteVector1 = byteVector0.put11(128, 2971);
      byteVector1.putShort(0);
      ByteVector byteVector2 = byteVector1.putByte((-2046));
      assertSame(byteVector2, byteVector0);
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
      byteVector0.length = 2482;
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("qfc.0nHzP.X%jI");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test09()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putShort(93);
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
      byteVector0.length = (-774);
      // Undeclared exception!
      try { 
        byteVector0.putShort((-774));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -774
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test11()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putLong(1860L);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test12()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = 1173;
      // Undeclared exception!
      try { 
        byteVector0.putLong(0L);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test13()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putInt(1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test14()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-780);
      // Undeclared exception!
      try { 
        byteVector0.putInt((-780));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -780
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
  public void test16()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByte(64);
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
      byteVector0.length = 75;
      // Undeclared exception!
      try { 
        byteVector0.putByte(75);
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
        byteVector0.put12(361, 361);
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
      byteVector0.length = 2106;
      // Undeclared exception!
      try { 
        byteVector0.put12(2106, 2106);
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
        byteVector0.put11(0, 0);
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
      byteVector0.length = (-780);
      // Undeclared exception!
      try { 
        byteVector0.put11((-780), (-780));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -780
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test22()  throws Throwable  {
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-795));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test23()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, 5628, 5628);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test24()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(2);
      ByteVector byteVector1 = byteVector0.putLong((-3705L));
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test25()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12(0, 0);
      ByteVector byteVector2 = byteVector0.putShort(0);
      byteVector2.putInt((-702));
      ByteVector byteVector3 = byteVector1.put12(8, (-702));
      assertSame(byteVector3, byteVector1);
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12(0, 0);
      ByteVector byteVector2 = byteVector1.putByte(0);
      ByteVector byteVector3 = byteVector2.putShort(0);
      byteVector3.putInt((-702));
      ByteVector byteVector4 = byteVector3.putInt(0);
      ByteVector byteVector5 = byteVector0.putByte((-702));
      ByteVector byteVector6 = byteVector5.putLong((-156L));
      byteVector6.putInt(0);
      byteVector5.putUTF8("RSk#FcY^_``>Z");
      byteVector1.putInt((-702));
      ByteVector byteVector7 = byteVector4.put11(3316, 1612);
      assertSame(byteVector7, byteVector4);
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.put12(0, 0);
      byteVector1.putByte(0);
      ByteVector byteVector2 = byteVector1.put11(12, 0);
      assertSame(byteVector2, byteVector0);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteVector0.data, 1, (-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }
}
