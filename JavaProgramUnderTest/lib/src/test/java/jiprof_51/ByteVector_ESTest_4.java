package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_4 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(63);
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, 63, 63);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putUTF8("y\";gyKI}*0mA,:");
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putUTF8("");
      byte[] byteArray0 = new byte[7];
      byteVector1.data = byteArray0;
      ByteVector byteVector2 = byteVector0.put11(0, 0);
      ByteVector byteVector3 = byteVector0.putByte(2475);
      ByteVector byteVector4 = byteVector2.putUTF8("");
      assertSame(byteVector4, byteVector3);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putShort(0);
      byteVector1.putUTF8("[|su+fyk");
      ByteVector byteVector2 = byteVector0.putUTF8("org.objectweb.asm.jip.ByteVector");
      ByteVector byteVector3 = byteVector2.putLong((-1471L));
      ByteVector byteVector4 = byteVector3.put11(191, 191);
      ByteVector byteVector5 = byteVector4.putLong((-1471L));
      assertSame(byteVector2, byteVector5);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putInt((-2091));
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putShort(0);
      ByteVector byteVector2 = byteVector0.put12(0, 3254);
      byteVector1.putByte(0);
      ByteVector byteVector3 = byteVector2.putInt(3254);
      assertSame(byteVector0, byteVector3);
  }

  @Test
  public void test06()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(16);
      byteVector0.putLong((-2410L));
      byteVector0.put11(16, 224);
      ByteVector byteVector1 = byteVector0.putUTF8("Ps5[zsJIY~x$X");
      ByteVector byteVector2 = byteVector1.putShort((-95));
      byteVector2.putUTF8("");
      ByteVector byteVector3 = byteVector0.put12(16, (-1));
      assertSame(byteVector0, byteVector3);
  }

  @Test
  public void test07()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putByte((-1508));
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
      byteVector0.length = 1897;
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("A");
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
        byteVector0.putShort(89);
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
        byteVector0.putShort((-1));
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
        byteVector0.putLong(240L);
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
  public void test14()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putInt(89);
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
  public void test16()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByteArray((byte[]) null, 66, 66);
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
        byteVector0.putByte(0);
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
      byteVector0.length = (-1);
      // Undeclared exception!
      try { 
        byteVector0.putByte(55);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1
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
        byteVector0.put12((-2250), (-2250));
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
      byteVector0.length = (-3793);
      // Undeclared exception!
      try { 
        byteVector0.put12((-3793), (-3793));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -3793
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test21()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.put11(59, 59);
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
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-3600));
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
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, (-1302), (-1344));
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test24()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(16);
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, 0, 171);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test25()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(16);
      byteVector0.putLong((-2410L));
      byteVector0.put11(16, 224);
      ByteVector byteVector1 = byteVector0.putLong(0L);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putInt(0);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byteVector0.putShort(0);
      ByteVector byteVector1 = byteVector0.put11(0, (-1));
      ByteVector byteVector2 = byteVector1.put11(0, 785);
      ByteVector byteVector3 = byteVector2.put11(785, (-562));
      assertSame(byteVector3, byteVector2);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(24);
      ByteVector byteVector1 = byteVector0.putInt(24);
      ByteVector byteVector2 = byteVector1.putUTF8("org.objectweb.asm.jip.ByteVector");
      ByteVector byteVector3 = byteVector2.putLong(24);
      ByteVector byteVector4 = byteVector3.putShort(2);
      assertSame(byteVector4, byteVector3);
  }

  @Test
  public void test29()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-3793);
      // Undeclared exception!
      try { 
        byteVector0.put11((-3793), (-3793));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -3793
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }
}
