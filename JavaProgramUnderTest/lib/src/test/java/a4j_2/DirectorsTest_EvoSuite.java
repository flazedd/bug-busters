package a4j_2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.io.Serializable;
import java.util.ArrayList;

public class DirectorsTest_EvoSuite {
    @Test
    public void test0()  throws Throwable  {
        Directors directors0 = new Directors();
        ArrayList<Object> arrayList0 = directors0.getDirectorsArray();
        assertNull(arrayList0);
    }

    @Test
    public void test1()  throws Throwable  {
        Directors directors0 = new Directors();
        ArrayList<Integer> arrayList0 = new ArrayList<Integer>();
        directors0.directors = arrayList0;
        String[] stringArray0 = directors0.getDirector();
        assertNotNull(stringArray0);
    }

    @Test
    public void test2()  throws Throwable  {
        Directors directors0 = new Directors();
        String[] stringArray0 = new String[5];
        directors0.setDirector(stringArray0);
        String[] stringArray1 = directors0.getDirector();
        assertFalse(stringArray1.equals(stringArray0));
    }

    @Test
    public void test3()  throws Throwable  {
        Directors directors0 = new Directors();
        String[] stringArray0 = new String[5];
        directors0.setDirector(stringArray0);
        String string0 = directors0.getDirector((-14));
        assertNull(string0);
    }

    @Test
    public void test4()  throws Throwable  {
        Directors directors0 = new Directors();
        String[] stringArray0 = new String[2];
        directors0.setDirector(stringArray0);
        // Undeclared exception!
        try {
            directors0.getDirector(1061);
            fail("Expecting exception: IndexOutOfBoundsException");
        } catch(IndexOutOfBoundsException e) {
            /*
             * Index: 1061, Size: 2
             */
        }
    }

    @Test
    public void test5()  throws Throwable  {
        Directors directors0 = new Directors();
        String string0 = directors0.toString();
        assertNotNull(string0);
        assertEquals("Director is null or size 0\n", string0);
    }

    @Test
    public void test6()  throws Throwable  {
        Directors directors0 = new Directors();
        ArrayList<Integer> arrayList0 = new ArrayList<Integer>();
        directors0.directors = arrayList0;
        String string0 = directors0.toString();
        assertEquals("Director is null or size 0\n", string0);
        assertNotNull(string0);
    }

    @Test
    public void test7()  throws Throwable  {
        Directors directors0 = new Directors();
        String[] stringArray0 = new String[2];
        stringArray0[0] = "{?:XJXP";
        stringArray0[1] = "{?:XJXP";
        directors0.setDirector(stringArray0);
        String string0 = directors0.toString();
        assertEquals("# of Directors = 2\nDirector - {?:XJXP\nDirector - {?:XJXP\n", directors0.toString());
        assertEquals("# of Directors = 2\nDirector - {?:XJXP\nDirector - {?:XJXP\n", string0);
    }
}
