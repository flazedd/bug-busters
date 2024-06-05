package beanbin_15;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__6 {
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
    WildcardSearch search = new WildcardSearch("a*b*c");
    assertTrue(search.doesMatch("abxc"));
}
@Test
public void testWildcardSearch4() {
    WildcardSearch search = new WildcardSearch("a*c*d*");
    assertTrue(search.doesMatch("axcydzdex"));
}
@Test
public void testWildcardSearch5() {
    WildcardSearch search = new WildcardSearch("*a*b*");
    assertTrue(search.doesMatch("xcaybzx"));
}
@Test
public void testWildcardSearch6() {
    WildcardSearch search = new WildcardSearch("a*a*a");
    assertTrue(search.doesMatch("aaaxaaa"));
}
@Test
public void testWildcardSearch7() {
    WildcardSearch search = new WildcardSearch("a*b*c*");
    assertTrue(search.doesMatch("axbxcydzcz"));
}
@Test
public void testWildcardSearch8() {
    WildcardSearch search = new WildcardSearch("a*b*c*d*");
    assertTrue(search.doesMatch("axbxcydzdexfydz"));
}
}