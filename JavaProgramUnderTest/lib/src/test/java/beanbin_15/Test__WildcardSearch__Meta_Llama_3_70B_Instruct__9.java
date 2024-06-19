package beanbin_15;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__9 {
@Test
public void testWildcardSearch() {
    WildcardSearch search = new WildcardSearch("he*o");
    assertTrue(search.doesMatch("hello"));
}
@Test
public void testWildcardSearch2() {
    WildcardSearch search = new WildcardSearch("*world*");
    assertTrue(search.doesMatch("hello world again"));
}
@Test
public void testWildcardSearch3() {
    WildcardSearch search = new WildcardSearch("a*b*c");
    assertTrue(search.doesMatch("abc"));
}
@Test
public void testWildcardSearch4() {
    WildcardSearch search = new WildcardSearch("*a");
    assertTrue(search.doesMatch("xa"));
}
@Test
public void testWildcardSearch5() {
    WildcardSearch search = new WildcardSearch("ab*c");
    assertFalse(search.doesMatch("abcd"));
}
@Test
public void testWildcardSearch6() {
    WildcardSearch search = new WildcardSearch("*");
    assertTrue(search.doesMatch("any string"));
}
@Test
public void testWildcardSearch7() {
    WildcardSearch search = new WildcardSearch("a*b*c*d");
    assertTrue(search.doesMatch("axbxcxd"));
}
@Test
public void testWildcardSearch9() {
    WildcardSearch search = new WildcardSearch("abc*def");
    assertTrue(search.doesMatch("abcdef"));
}
}