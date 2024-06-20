package beanbin_15;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__11 {
@Test
public void testWildcardSearch() {
    WildcardSearch search = new WildcardSearch("a*b");
    assertTrue(search.doesMatch("acb"));
}
@Test
public void testWildcardSearch2() {
    WildcardSearch search = new WildcardSearch("a*c*d");
    assertTrue(search.doesMatch("axcydzd"));
}
@Test
public void testWildcardSearch3() {
    WildcardSearch search = new WildcardSearch("abc*def");
    assertTrue(search.doesMatch("abcdefdef"));
}
@Test
public void testWildcardSearch4() {
    WildcardSearch search = new WildcardSearch("*abc*");
    assertTrue(search.doesMatch("xyzabcxyz"));
}
@Test
public void testWildcardSearch5() {
    WildcardSearch search = new WildcardSearch("a*");
    assertTrue(search.doesMatch("a"));
}
@Test
public void testWildcardSearch6() {
    WildcardSearch search = new WildcardSearch("*a*b*");
    assertTrue(search.doesMatch("xcazb"));
}
@Test
public void testWildcardSearch9() {
    WildcardSearch search = new WildcardSearch("*");
    assertTrue(search.doesMatch("anything"));
}
@Test
public void testWildcardSearch10() {
    WildcardSearch search = new WildcardSearch("a*b*c*");
    assertTrue(search.doesMatch("axbxcx"));
}
}