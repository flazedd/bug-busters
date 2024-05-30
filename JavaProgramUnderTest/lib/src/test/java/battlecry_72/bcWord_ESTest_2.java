/*
 * This file was automatically generated by EvoSuite
 * Tue May 28 16:38:58 GMT 2024
 */

package battlecry_72;

import org.junit.jupiter.api.Test;

import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;

public class bcWord_ESTest_2 {

    @Test
    public void test00()  throws Throwable  {
        bcWord bcWord0 = new bcWord((String) null, "");
        bcWord0.getWord();
        assertEquals("", bcWord0.getMetricCode());
        assertEquals(0, bcWord0.getSyllables());
    }

    @Test
    public void test01()  throws Throwable  {
        bcWord bcWord0 = new bcWord("", "");
        bcWord0.getWord();
        assertEquals("", bcWord0.getMetricCode());
        assertEquals(0, bcWord0.getSyllables());
    }

    @Test
    public void test02()  throws Throwable  {
        bcWord bcWord0 = new bcWord("Xv#)E.P} s1i=L", "Z");
        int int0 = bcWord0.getSyllables();
        assertEquals("", bcWord0.getMetricCode());
        assertEquals(0, int0);
    }

    @Test
    public void test03()  throws Throwable  {
        bcWord bcWord0 = new bcWord("", "");
        bcWord0.getRhymeKey(true);
        assertEquals("", bcWord0.getMetricCode());
        assertEquals(0, bcWord0.getSyllables());
    }

    @Test
    public void test04()  throws Throwable  {
        bcWord bcWord0 = new bcWord(")v=(CeW a,", "P*~Xp.(m_S");
        bcWord0.setEqualWord("P*~Xp.(m_S", (String) null);
        bcWord0.getPhonemes();
        assertEquals(0, bcWord0.getSyllables());
        assertEquals("", bcWord0.getMetricCode());
    }

    @Test
    public void test05()  throws Throwable  {
        bcWord bcWord0 = new bcWord(")v=(CeW a,", "P*~Xp.(m_S");
        bcWord0.setEqualWord(")v=(CeW a,", "");
        bcWord0.getPhonemes();
        assertEquals("", bcWord0.getMetricCode());
        assertEquals(0, bcWord0.getSyllables());
    }

    @Test
    public void test06()  throws Throwable  {
        bcWord bcWord0 = new bcWord("Xv#)E.P} s1i=L", "Z");
        String string0 = bcWord0.getMetricCode();
        assertEquals("", string0);
        assertEquals(0, bcWord0.getSyllables());
    }

    @Test
    public void test07()  throws Throwable  {
        bcWord bcWord0 = new bcWord((String) null, "");
        bcWord0.setEqualWord("", (String) null);
        // Undeclared exception!
        assertThrows(NullPointerException.class, () -> {
            bcWord0.getRhymeKey(false);
        });
    }

    @Test
    public void test08()  throws Throwable  {
        bcWord bcWord0 = new bcWord((String) null, "");
        // Undeclared exception!
        assertThrows(NullPointerException.class, () -> {
            bcWord0.equalTo("");
        });
    }

    @Test
    public void test09()  throws Throwable  {
        AtomicReference<bcWord> bcWord0 = null;
        assertThrows(NullPointerException.class, () -> {
            bcWord0.set(new bcWord((String) null, (String) null));
        });
    }

    @Test
    public void test10()  throws Throwable  {
        bcWord bcWord0 = new bcWord("]@V!1mYjKSV1pZ4/", "]@V!1mYjKSV1pZ4/");
        String string0 = bcWord0.getRhymeKey(false);
        assertEquals("]@V!1mYjKSV1pZ4/", string0);
        assertEquals(2, bcWord0.getSyllables());
    }

    @Test
    public void test11()  throws Throwable  {
        bcWord bcWord0 = new bcWord("3", "D1X>v=//A1");
        String string0 = bcWord0.getRhymeKey(true);
        assertEquals("D1X>v=//A1", string0);
        assertEquals("11", bcWord0.getMetricCode());
        assertEquals(2, bcWord0.getSyllables());
    }

    @Test
    public void test12()  throws Throwable  {
        bcWord bcWord0 = new bcWord("Z", "Xv#)E.P} s1i=L");
        String string0 = bcWord0.getRhymeKey(false);
        assertEquals("I", bcWord0.getMetricCode());
        assertEquals(1, bcWord0.getSyllables());
        assertEquals("s1i=L", string0);
    }

    @Test
    public void test13()  throws Throwable  {
        bcWord bcWord0 = new bcWord("2", "2");
        String string0 = bcWord0.getRhymeKey(true);
        assertEquals("2", string0);
        assertEquals(1, bcWord0.getSyllables());
        assertEquals("Z", bcWord0.getMetricCode());
    }

    @Test
    public void test14()  throws Throwable  {
        bcWord bcWord0 = new bcWord("{4ynPHXZ(!0xu'$JUz", "{4ynPHXZ(!0xu'$JUz");
        String string0 = bcWord0.getRhymeKey(true);
        assertEquals("O", bcWord0.getMetricCode());
        assertEquals(1, bcWord0.getSyllables());
        assertEquals("{4ynPHXZ(!0xu'$JUz", string0);
    }

    @Test
    public void test15()  throws Throwable  {
        bcWord bcWord0 = new bcWord("", "");
        bcWord0.setEqualWord("&6^qX6u;9@N", "");
        boolean boolean0 = bcWord0.equalTo("");
        assertEquals("", bcWord0.getMetricCode());
        assertEquals(0, bcWord0.getSyllables());
        assertTrue(boolean0);
    }

    @Test
    public void test16()  throws Throwable  {
        bcWord bcWord0 = new bcWord("Z", "Xv#)E.P} s1i=L");
        boolean boolean0 = bcWord0.equalTo("");
        assertFalse(boolean0);
        assertEquals("I", bcWord0.getMetricCode());
        assertEquals(1, bcWord0.getSyllables());
    }

    @Test
    public void test17()  throws Throwable  {
        bcWord bcWord0 = new bcWord(")v=(CeW a,", "P*~Xp.(m_S");
        bcWord0.setEqualWord("P*~Xp.(m_S", ")v=(CeW a,");
        boolean boolean0 = bcWord0.equalTo("P*~Xp.(m_S");
        assertTrue(boolean0);
        assertEquals("", bcWord0.getMetricCode());
        assertEquals(0, bcWord0.getSyllables());
    }

    @Test
    public void test18()  throws Throwable  {
        bcWord bcWord0 = new bcWord("Z", "Xv#)E.P} s1i=L");
        int int0 = bcWord0.getSyllables();
        assertEquals(1, int0);
        assertEquals("I", bcWord0.getMetricCode());
    }

    @Test
    public void test19()  throws Throwable  {
        bcWord bcWord0 = new bcWord("Z", "Xv#)E.P} s1i=L");
        bcWord0.getWord();
        assertEquals(1, bcWord0.getSyllables());
        assertEquals("I", bcWord0.getMetricCode());
    }

    @Test
    public void test20()  throws Throwable  {
        bcWord bcWord0 = new bcWord(")v=(CeW a,", "P*~Xp.(m_S");
        bcWord0.getPhonemes();
        assertEquals(0, bcWord0.getSyllables());
        assertEquals("", bcWord0.getMetricCode());
    }

    @Test
    public void test21()  throws Throwable  {
        bcWord bcWord0 = new bcWord("Z", "Xv#)E.P} s1i=L");
        String string0 = bcWord0.getMetricCode();
        assertEquals("I", string0);
        assertEquals(1, bcWord0.getSyllables());
    }
}
