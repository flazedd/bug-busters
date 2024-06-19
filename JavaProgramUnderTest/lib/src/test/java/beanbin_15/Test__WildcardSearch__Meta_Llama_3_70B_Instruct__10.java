package beanbin_15;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testWildcardSearch() {
    WildcardSearch wcs = new WildcardSearch("he*l*o");
    assertTrue(wcs.doesMatch("hello"));
}
@Test
public void testWildcardSearch2() {
    WildcardSearch wcs = new WildcardSearch("*abc*");
    assertTrue(wcs.doesMatch("xyzabc123"));
}
@Test
public void testWildcardSearch3() {
    WildcardSearch wcs = new WildcardSearch("a*b*c");
    assertTrue(wcs.doesMatch("axbxc"));
}
@Test
public void testWildcardSearch4() {
    WildcardSearch wcs = new WildcardSearch("a*b*c*");
    assertTrue(wcs.doesMatch("axbxcx"));
}
@Test
public void testWildcardSearch6() {
    WildcardSearch wcs = new WildcardSearch("*a*b*c*");
    assertTrue(wcs.doesMatch("xaabyzc"));
}
@Test
public void testWildcardSearch7() {
    WildcardSearch wcs = new WildcardSearch("a*b*c*d");
    assertTrue(wcs.doesMatch("axbxcyd"));
}
@Test
public void testWildcardSearch8() {
    WildcardSearch wcs = new WildcardSearch("a*b*c*def");
    assertTrue(wcs.doesMatch("axbxcydef"));
}
@Test
public void testWildcardSearch9() {
    WildcardSearch wcs = new WildcardSearch("abc*def*ghi");
    assertTrue(wcs.doesMatch("abcdefghi"));
}
}