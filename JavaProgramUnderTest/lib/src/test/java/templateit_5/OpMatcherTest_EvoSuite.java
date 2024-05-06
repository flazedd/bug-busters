package templateit_5;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class OpMatcherTest_EvoSuite {

    @Test
    public void test0()  throws Throwable  {
        OpMatcher opMatcher0 = new OpMatcher();
        assertNotNull(opMatcher0);
    }

    @Test
    public void test1()  throws Throwable  {
        String[] stringArray0 = OpMatcher.matchTemplateBegin((String) null);
        assertNull(stringArray0);
    }

    @Test
    public void test2()  throws Throwable  {
        String[] stringArray0 = OpMatcher.matchTemplateBegin("@tbegin");
        assertNull(stringArray0);
    }

    @Test
    public void test3()  throws Throwable  {
        String[] stringArray0 = OpMatcher.matchTemplateBegin("@template_begin");
        assertNull(stringArray0);
    }

    @Test
    public void test4()  throws Throwable {
        String[] stringArray0 = OpMatcher.matchTemplateBegin("M=]#7L+IL");
        assertNull(stringArray0);
    }
}
