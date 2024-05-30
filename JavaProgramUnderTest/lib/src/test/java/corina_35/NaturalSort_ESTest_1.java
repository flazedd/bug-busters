/*
 * This file was automatically generated by EvoSuite
 * Tue May 28 16:38:54 GMT 2024
 */

package corina_35;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class NaturalSort_ESTest_1 {

    @Test
    public void test00()  throws Throwable  {
        // Undeclared exception!
        assertThrows(NullPointerException.class, () -> {
            NaturalSort.compareIgnoreCase((String) null, (String) null);
        });
    }

    @Test
    public void test01()  throws Throwable  {
        // Undeclared exception!
        assertThrows(NullPointerException.class, () -> {
            NaturalSort.compare((String) null, (String) null);
        });
    }

    @Test
    public void test02()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("Z6m>9r;sml^MD0*", "&+aIYptd_To&TaXd3u");
        assertEquals(1, int0);
    }

    @Test
    public void test03()  throws Throwable  {
        int int0 = NaturalSort.compare("", "]GtQwu7aoE0q");
        assertEquals((-1), int0);
    }

    @Test
    public void test04()  throws Throwable  {
        int int0 = NaturalSort.compare(" 614`i", "L#Y#:.LR}6tGl[gV");
        assertEquals((-1), int0);
    }

    @Test
    public void test05()  throws Throwable  {
        int int0 = NaturalSort.compare(" ", " ");
        assertEquals(0, int0);
    }

    @Test
    public void test06()  throws Throwable  {
        int int0 = NaturalSort.compare(" 4", "00Y9pj%]");
        assertEquals(1, int0);
    }

    @Test
    public void test07()  throws Throwable  {
        int int0 = NaturalSort.compare("0O'$.EK", " 61)");
        assertEquals((-1), int0);
    }

    @Test
    public void test08()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("00Y9p7]", "0 ");
        assertEquals(1, int0);
    }

    @Test
    public void test09()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("0 ", "00Y9p7]");
        assertEquals((-1), int0);
    }

    @Test
    public void test10()  throws Throwable  {
        int int0 = NaturalSort.compare("2gIWt1P5_", " 614`i");
        assertEquals((-1), int0);
    }

    @Test
    public void test11()  throws Throwable  {
        int int0 = NaturalSort.compare(" 614`i", "2gIWt1P5_");
        assertEquals(1, int0);
    }

    @Test
    public void test12()  throws Throwable  {
        NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
        int int0 = naturalSort_NaturalComparator0.compare("&+aIYptd_To&TaXd3u", "&+aIYptd_To&TaXd3u");
        assertEquals(0, int0);
    }

    @Test
    public void test13()  throws Throwable  {
        NaturalSort.NaturalComparator naturalSort_NaturalComparator0 = new NaturalSort.NaturalComparator();
        NaturalSort.CINaturalComparator naturalSort_CINaturalComparator0 = new NaturalSort.CINaturalComparator();
        Object object0 = new Object();
        // Undeclared exception!
        assertThrows(ClassCastException.class, () -> {
            naturalSort_CINaturalComparator0.compare(naturalSort_NaturalComparator0, object0);
        });
    }

    @Test
    public void test14()  throws Throwable  {
        int int0 = NaturalSort.compare("Zg603)a", "Zg603)a");
        assertEquals(0, int0);
    }

    @Test
    public void test15()  throws Throwable  {
        int int0 = NaturalSort.compareIgnoreCase("-g60", "-g60");
        assertEquals(0, int0);
    }
}
