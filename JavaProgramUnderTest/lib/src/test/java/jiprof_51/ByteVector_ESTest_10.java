package jiprof_51;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ByteVector_ESTest_10 {

  @Test
  public void test00()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byte[] byteArray0 = new byte[3];
      ByteVector byteVector1 = byteVector0.putByteArray(byteArray0, (byte)3, 0);
      assertSame(byteVector0, byteVector1);
  }

  @Test
  public void test01()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      byteVector0.putByte(0);
      ByteVector byteVector1 = byteVector0.putLong(188L);
      byteVector1.put12(124, 0);
      ByteVector byteVector2 = byteVector1.putUTF8("Parx");
      assertSame(byteVector2, byteVector1);
  }

  @Test
  public void test02()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(0);
      ByteVector byteVector1 = byteVector0.putUTF8("x{xmo12N`jyND4`O");
      ByteVector byteVector2 = byteVector1.putShort(0);
      ByteVector byteVector3 = byteVector2.putLong((-2366L));
      ByteVector byteVector4 = byteVector3.putInt(0);
      ByteVector byteVector5 = byteVector4.putInt(1);
      assertSame(byteVector4, byteVector5);
  }

  @Test
  public void test03()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(2);
      ByteVector byteVector1 = byteVector0.put12(2, 2);
      ByteVector byteVector2 = byteVector1.putLong(2);
      byteVector1.putLong((byte)3);
      ByteVector byteVector3 = byteVector2.put12((-301), (-1566));
      assertSame(byteVector3, byteVector0);
  }

  @Test
  public void test04()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(3);
      ByteVector byteVector1 = byteVector0.putInt(3);
      ByteVector byteVector2 = byteVector1.put11(3, 3);
      assertSame(byteVector2, byteVector0);
  }

  @Test
  public void test05()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(2);
      ByteVector byteVector1 = byteVector0.put12(2, 2);
      byteVector0.putShort(1458);
      ByteVector byteVector2 = byteVector1.putShort(1417);
      ByteVector byteVector3 = byteVector2.putByte(1417);
      assertSame(byteVector0, byteVector3);
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
      byteVector0.length = 2185;
      // Undeclared exception!
      try { 
        byteVector0.putUTF8("y^LV!+3h[");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test08()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      byteVector0.data = null;
      // Undeclared exception!
      try { 
        byteVector0.putShort(1403);
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
      byteVector0.length = 224;
      // Undeclared exception!
      try { 
        byteVector0.putShort(224);
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
        byteVector0.putLong(182L);
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
        byteVector0.putInt(4382);
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
      byteVector0.length = 121;
      // Undeclared exception!
      try { 
        byteVector0.putInt(121);
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
        byteVector0.putByteArray((byte[]) null, 975, 975);
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
        byteVector0.putByte((-285));
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
      byteVector0.length = 224;
      // Undeclared exception!
      try { 
        byteVector0.putByte(224);
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
        byteVector0.put12(3826, 3826);
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
      byteVector0.length = 121;
      // Undeclared exception!
      try { 
        byteVector0.put12(121, 121);
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
        byteVector0.put11((-1488), (-1488));
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
      byteVector0.length = 215;
      // Undeclared exception!
      try { 
        byteVector0.put11(215, 215);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test21()  throws Throwable  {
      ByteVector byteVector0 = null;
      try {
        byteVector0 = new ByteVector((-682));
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
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putByteArray((byte[]) null, 1793, 1793);
      assertSame(byteVector1, byteVector0);
  }

  @Test
  public void test23()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector();
      ByteVector byteVector1 = byteVector0.putInt((-804));
      ByteVector byteVector2 = byteVector1.putUTF8("1'!^HT");
      byteVector2.putLong((-804));
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        byteVector1.putByteArray(byteArray0, (byte)25, 45);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test24()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        byteVector0.putByteArray(byteArray0, 1, (byte) (-107));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test
  public void test25()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putUTF8("x}Z>_V`Uso");
      ByteVector byteVector2 = byteVector1.putInt(0);
      ByteVector byteVector3 = byteVector2.putLong(0);
      assertSame(byteVector3, byteVector0);
  }

  @Test
  public void test26()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putUTF8("x}Z>_V`Uso");
      ByteVector byteVector2 = byteVector1.putInt(0);
      ByteVector byteVector3 = byteVector1.put12(0, 1);
      assertSame(byteVector3, byteVector2);
  }

  @Test
  public void test27()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putInt((-1655));
      byteVector0.putShort(1);
      ByteVector byteVector2 = byteVector1.putLong((-2669));
      ByteVector byteVector3 = byteVector2.putShort((-2102));
      byteVector2.putByte(736);
      ByteVector byteVector4 = byteVector1.putUTF8("7-Q%loVWqOo");
      ByteVector byteVector5 = byteVector3.put11(101, (-1));
      assertSame(byteVector5, byteVector4);
  }

  @Test
  public void test28()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putShort(1);
      ByteVector byteVector2 = byteVector1.putShort((-2102));
      byteVector0.putByte(736);
      ByteVector byteVector3 = byteVector2.put11(101, (-1));
      assertSame(byteVector3, byteVector0);
  }

  @Test
  public void test29()  throws Throwable  {
      ByteVector byteVector0 = new ByteVector(1);
      ByteVector byteVector1 = byteVector0.putUTF8("x}Z>_V`Uso");
      ByteVector byteVector2 = byteVector1.putInt(0);
      ByteVector byteVector3 = byteVector2.putByte(2);
      assertSame(byteVector3, byteVector1);
  }
}
