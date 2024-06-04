package beanbin_15;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__5 {
@Test
public void wildcardSearchTest() {
    WildcardSearch search = new WildcardSearch("he*o");
    assertTrue(search.doesMatch("hello"));
}
@Test
public void wildcardSearchTest2() {
    WildcardSearch search = new WildcardSearch("a*c");
    assertTrue(search.doesMatch("abc"));
}
@Test
public void wildcardSearchTest3() {
    WildcardSearch search = new WildcardSearch("*x*");
    assertTrue(search.doesMatch("axxbx"));
}
@Test
public void wildcardSearchTest4() {
    WildcardSearch search = new WildcardSearch("a*b*c");
    assertTrue(search.doesMatch("axbxc"));
}
@Test
public void wildcardSearchTest7() {
    WildcardSearch search = new WildcardSearch("a*b");
    assertFalse(search.doesMatch("axxxc"));
}
@Test
public void wildcardSearchTest8() {
    WildcardSearch search = new WildcardSearch("a*b*c*");
    assertTrue(search.doesMatch("axbxcxd"));
}
@Test
public void wildcardSearchTest9() {
    WildcardSearch search = new WildcardSearch("*");
    assertTrue(search.doesMatch("anystring"));
}
@Test
public void wildcardSearchTest10() {
    WildcardSearch search = new WildcardSearch("abc*def");
    assertTrue(search.doesMatch("abcdefgdef"));
}
}