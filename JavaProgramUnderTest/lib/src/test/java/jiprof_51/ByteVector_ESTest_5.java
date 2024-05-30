package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_5 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, 2577, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putUTF8("RFh3U>3v)3.9Pd}(");
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putUTF8("2^zX>Fa:my\"@!cp@.");
      ByteVector byteVector2 = byteVector1.put12(0, 0);
      ByteVector byteVector3 = byteVector0.putByte((-300));
      byteVector0.put12(224, 0);
      byteVector0.putShort(0);
      byteVector1.put11(17, (byte)0);
      ByteVector byteVector4 = byteVector3.putUTF8("org.objectweb.asm.jip.ByteVector");
      assertSame(byteVector4, byteVector2);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(2);
      ByteVector byteVector1 = byteVector0.putByte(2);
      ByteVector byteVector2 = byteVector1.putLong(0);
      byteVector2.putByte(44);
      ByteVector byteVector3 = byteVector2.putLong((-767L));
      assertSame(byteVector2, byteVector3);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putInt((-4381));
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.put12((-332), (-332));
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test06()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(2);
      ByteVector byteVector1 = byteVector0.putByte(2);
      ByteVector byteVector2 = byteVector0.put12(2, 0);
      ByteVector byteVector3 = byteVector2.putByte(437);
      byteVector3.putShort(0);
      ByteVector byteVector4 = byteVector1.putByte(0);
      ByteVector byteVector5 = byteVector2.putLong((-1L));
      ByteVector byteVector6 = byteVector5.putShort(0);
      byteVector5.putShort(2);
      byteVector4.putInt(2);
      byteVector0.putUTF8("<vO3/K3nc:3l");
      ByteVector byteVector7 = byteVector0.putInt(437);
      byteVector7.put11(2, 0);
      byteVector6.putLong(1);
      ByteVector byteVector8 = byteVector1.put11(0, (-1508));
      byteVector2.put12((-501), 17);
      ByteVector byteVector9 = byteVector3.putShort(78);
      byteVector9.putShort(0);
      ByteVector byteVector10 = byteVector8.put12(2136, 3);
      assertSame(byteVector10, byteVector8);
  }

  @Test
  public void test07()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putShort((-2577));
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test08()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byte[] byteArray0 = new byte[6];
      ByteVector byteVector1 = byteVector0.putInt(1);
      byteVector0.data = byteArray0;
      ByteVector byteVector2 = byteVector0.put12(1, 1);
      ByteVector byteVector3 = byteVector2.putShort(64);
      ByteVector byteVector4 = byteVector3.putByte((byte)3);
      ByteVector byteVector5 = byteVector4.put11(3, (-1));
      assertSame(byteVector5, byteVector1);
  }

  @Test
  public void test09()  throws Throwable  {
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
  public void test10()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.length = (-1295);
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("3DGYYYW>]");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1295
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
        byteVector0.putShort(62);
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
      byteVector0.length = 1148;
      // Undeclared exception!
      try { 
        byteVector0.putShort(1148);
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
        byteVector0.putLong(568L);
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
      byteVector0.length = 69;
      // Undeclared exception!
      try { 
        byteVector0.putLong(69);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test15()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putInt(0);
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
      byteVector0.length = 109;
      // Undeclared exception!
      try { 
        byteVector0.putInt(109);
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
        byteVector0.putByteArray((byte[]) null, 97, 97);
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
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putByte(1451);
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
      byteVector0.length = 1148;
      // Undeclared exception!
      try { 
        byteVector0.putByte(1148);
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
        byteVector0.put12(62, 62);
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
      byteVector0.length = 1148;
      // Undeclared exception!
      try { 
        byteVector0.put12(1148, 1148);
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
        byteVector0.put11(4, 4);
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
      byteVector0.length = (-2391);
      // Undeclared exception!
      try { 
        byteVector0.put11((-2391), (-2391));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -2391
         //
         //verifyException("org.objectweb.asm.jip.ByteVector", e);
      }
  }

  @Test
  public void test24()  throws Throwable  {
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-2150));
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
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, 6, 6);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, (-1600), 2047);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putUTF8("2^zX>Fa:my\"@!cp@.");
      ByteVector byteVector2 = byteVector1.putUTF8("2^zX>Fa:my\"@!cp@.");
      ByteVector byteVector3 = byteVector2.putInt(0);
      ByteVector byteVector4 = byteVector0.putByte((-300));
      byteVector3.putLong(0L);
      ByteVector byteVector5 = byteVector0.put12(224, 0);
      ByteVector byteVector6 = byteVector5.putShort(0);
      byteVector6.putInt(0);
      ByteVector byteVector7 = byteVector5.putInt(1);
      assertSame(byteVector7, byteVector4);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putInt(1);
      ByteVector byteVector2 = byteVector1.put11(1148, 1148);
      ByteVector byteVector3 = byteVector2.putShort(522);
      assertSame(byteVector1, byteVector3);
  }
}
