package tullibee_1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Collection;
import java.util.Vector;

public class UtilTest_EvoSuite {
    @Test
    public void test0()  throws Throwable  {
        int int0 = Util.StringCompare("u-XqB-[erRPX+y", "u-XqB-[erRPX+y");
        assertEquals(0, int0);
    }

    @Test
    public void test1()  throws Throwable  {
        Util util0 = new Util();
        assertNotNull(util0);
    }

    @Test
    public void test2()  throws Throwable  {
        int int0 = Util.StringCompareIgnCase("-1", "");
        assertEquals(2, int0);
    }

    @Test
    public void test3()  throws Throwable  {
        boolean boolean0 = Util.StringIsEmpty((String) null);
        assertEquals(true, boolean0);
    }

    @Test
    public void test4()  throws Throwable  {
        boolean boolean0 = Util.StringIsEmpty("");
        assertEquals(true, boolean0);
    }

    @Test
    public void test5()  throws Throwable  {
        boolean boolean0 = Util.StringIsEmpty("u-XqB-[erRPX+y");
        assertEquals(false, boolean0);
    }

    @Test
    public void test6()  throws Throwable  {
        String string0 = Util.NormalizeString((String) null);
        assertEquals("", string0);
    }

    @Test
    public void test7()  throws Throwable  {
        Vector<Object> vector0 = new Vector<Object>();
        Vector<Integer> vector1 = new Vector<Integer>();
        vector0.add((Object) "[]");
        boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
        assertEquals(false, boolean0);
    }

    @Test
    public void test8()  throws Throwable  {
        Vector<Integer> vector0 = new Vector<Integer>();
        boolean boolean0 = Util.VectorEqualsUnordered((Vector) null, vector0);
        assertEquals(true, boolean0);
    }

    @Test
    public void test9()  throws Throwable  {
        Vector<Integer> vector0 = new Vector<Integer>();
        boolean boolean0 = Util.VectorEqualsUnordered(vector0, (Vector) null);
        assertEquals(true, boolean0);
    }

    @Test
    public void test10()  throws Throwable  {
        Vector<Object> vector0 = new Vector<Object>();
        Vector<Integer> vector1 = new Vector<Integer>();
        vector0.add((Object) "[]");
        vector1.add((Integer) 0);
        boolean boolean0 = Util.VectorEqualsUnordered(vector0, vector1);
        assertEquals(false, boolean0);
    }

    @Test
    public void test11()  throws Throwable  {
        Vector<String> vector0 = new Vector<String>();
        vector0.add("");
        vector0.add("");
        Vector<String> vector1 = new Vector<String>((Collection<? extends String>) vector0);
        boolean boolean0 = Util.VectorEqualsUnordered(vector1, vector0);
        assertEquals(true, boolean0);
    }

    @Test
    public void test12()  throws Throwable  {
        String string0 = Util.IntMaxString((-1));
        assertEquals("-1", string0);
        assertNotNull(string0);
    }

    @Test
    public void test13()  throws Throwable  {
        String string0 = Util.IntMaxString(Integer.MAX_VALUE);
        assertEquals("", string0);
    }

    @Test
    public void test14()  throws Throwable  {
        String string0 = Util.DoubleMaxString((-1675.101690083464));
        assertEquals("-1675.101690083464", string0);
        assertNotNull(string0);
    }

    @Test
    public void test15()  throws Throwable  {
        String string0 = Util.DoubleMaxString(1.7976931348623157E308);
        assertEquals("", string0);
    }
}
