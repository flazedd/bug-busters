/*
 * This file was automatically generated by EvoSuite
 * Tue May 28 16:38:55 GMT 2024
 */

package corina_35;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class NaturalSort_ESTest_2 {

    @Test
    public void test00()  throws Throwable  {
        // Undeclared exception!
        try {
            NaturalSort.compareIgnoreCase((String) null, (String) null);
            fail("Expecting exception: NullPointerException");

        } catch(NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
//            verifyException("corina.util.NaturalSort", e);
        }
    }

    @Test
    public void test01()  throws Throwable  {
        // Undeclared exception!
        try {
            NaturalSort.compare((String) null, (String) null);
            fail("Expecting exception: NullPointerException");

        } catch(NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
//            verifyException("corina.util.NaturalSort", e);
        }
    }

    @Test
    public void test02()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("eQqDI<m5|0%u", "");
        assertEquals(1, int0);
    }

    @Test
    public void test03()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("", "(afs2zVIf");
        assertEquals((-1), int0);
    }

    @Test
    public void test04()  throws Throwable  {
        int int0 = NaturalSort.compare("18:r^ Li@)Yv7J]:3`Q", "xy 'Tg");
        assertEquals((-1), int0);
    }

    @Test
    public void test05()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("oF>QMIX+ ", "oF>QMIX+ ");
        assertEquals(0, int0);
    }

    @Test
    public void test06()  throws Throwable  {
        int int0 = NaturalSort.compare("18:r^ Li@)Yv7J]:3`Q", "18:r^ Li@)Yv7J]:3`Q");
        assertEquals(0, int0);
    }

    @Test
    public void test07()  throws Throwable  {
        int int0 = NaturalSort.compare("8nBqA^JW@", "0Yu*A0q[T");
        assertEquals(1, int0);
    }

    @Test
    public void test08()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("0", "1");
        assertEquals((-1), int0);
    }

    @Test
    public void test09()  throws Throwable  {
        int int0 = NaturalSort.compare("01", "0");
        assertEquals(1, int0);
    }

    @Test
    public void test10()  throws Throwable  {
        int int0 = NaturalSort.compare("!0", "!0");
        assertEquals(0, int0);
    }

    @Test
    public void test11()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("3')qc", "8nBqA^JW@");
        assertEquals((-1), int0);
    }

    @Test
    public void test12()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("8nBqA^JW@", "82Eu");
        assertEquals((-1), int0);
    }

    @Test
    public void test13()  throws Throwable  {
        NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
        int int0 = naturalSort_NaturalComparator0.compare("/o``-)ppF(b8", "/o``-)ppF(b8");
        assertEquals(0, int0);
    }

    @Test
    public void test14()  throws Throwable  {
        NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
        int int0 = naturalSort_CINaturalComparator0.compare("eQqDI<m5|0%u", "eQqDI<m5|0%u");
        assertEquals(0, int0);
    }

    @Test
    public void test15()  throws Throwable  {
        int int0 = NaturalSort.compare("715{o9N", "3')qc");
        assertEquals(1, int0);
    }
}
