package beanbin_15;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__4 {
@Test
public void wildcardSearchTest() {
    WildcardSearch search = new WildcardSearch("a*b");
    assertTrue(search.doesMatch("acab"));
}

@Test
public void wildcardSearchTest2() {
    WildcardSearch search = new WildcardSearch("a*c*d");
    assertTrue(search.doesMatch("axcydzd"));
}

@Test
public void wildcardSearchTest3() {
    WildcardSearch search = new WildcardSearch("a*b*c");
    assertTrue(search.doesMatch("axbxc"));
}

@Test
public void wildcardSearchTest4() {
    WildcardSearch search = new WildcardSearch("*a*b*");
    assertTrue(search.doesMatch("xcaabyz"));
}

@Test
public void wildcardSearchTest5() {
    WildcardSearch search = new WildcardSearch("a*a");
    assertTrue(search.doesMatch("aaaa"));
}

@Test
public void wildcardSearchTest6() {
    WildcardSearch search = new WildcardSearch("b*a");
    assertTrue(search.doesMatch("bxa"));
}

@Test
public void wildcardSearchTest7() {
    WildcardSearch search = new WildcardSearch("a*b*a");
    assertTrue(search.doesMatch("axbxa"));
}

@Test
public void wildcardSearchTest8() {
    WildcardSearch search = new WildcardSearch("a*a*a");
    assertTrue(search.doesMatch("aaa"));
}

}