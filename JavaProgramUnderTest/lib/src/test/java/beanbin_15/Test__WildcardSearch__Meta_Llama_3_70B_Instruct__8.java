package beanbin_15;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testWildcardSearch() {
    WildcardSearch ws = new WildcardSearch("he*o");
    assertTrue(ws.doesMatch("hello"));
}
@Test
public void testWildcardSearch3() {
    WildcardSearch ws = new WildcardSearch("a*b");
    assertTrue(ws.doesMatch("axxb"));
}
@Test
public void testWildcardSearch4() {
    WildcardSearch ws = new WildcardSearch("*a*");
    assertTrue(ws.doesMatch("banana"));
}
@Test
public void testWildcardSearch5() {
    WildcardSearch ws = new WildcardSearch("ab*c");
    assertTrue(ws.doesMatch("abcabcabc"));
}
@Test
public void testWildcardSearch6() {
    WildcardSearch ws = new WildcardSearch("a*a*a");
    assertTrue(ws.doesMatch("aaabbbbaaa"));
}
@Test
public void testWildcardSearch7() {
    WildcardSearch ws = new WildcardSearch("b*a");
    assertTrue(ws.doesMatch("bbbaaa"));
}
@Test
public void testWildcardSearch8() {
    WildcardSearch ws = new WildcardSearch("*b*");
    assertTrue(ws.doesMatch("abcbcd"));
}
@Test
public void testWildcardSearch9() {
    WildcardSearch ws = new WildcardSearch("a*b*c*d");
    assertTrue(ws.doesMatch("axxbxxcxd"));
}
}