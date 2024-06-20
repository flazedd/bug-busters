package beanbin_15;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__7 {
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
    assertTrue(search.doesMatch("abracadabc"));
}

@Test
public void testWildcardSearch4() {
    WildcardSearch search = new WildcardSearch("a*c");
    assertTrue(search.doesMatch("abc"));
}

@Test
public void testWildcardSearch5() {
    WildcardSearch search = new WildcardSearch("*a*b*");
    assertTrue(search.doesMatch("xaaabyb"));
}

@Test
public void testWildcardSearch6() {
    WildcardSearch search = new WildcardSearch("a*b*c*");
    assertTrue(search.doesMatch("axxbxxcxdxx"));
}

@Test
public void testWildcardSearch7() {
    WildcardSearch search = new WildcardSearch("a*b*c*d*");
    assertTrue(search.doesMatch("axxbxxcxxdxxe"));
}

@Test
public void testWildcardSearch8() {
    WildcardSearch search = new WildcardSearch("abc*");
    assertTrue(search.doesMatch("abcdefg"));
}


}