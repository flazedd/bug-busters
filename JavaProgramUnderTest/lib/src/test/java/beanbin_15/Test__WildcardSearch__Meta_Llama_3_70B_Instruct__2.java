package beanbin_15;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__2 {
@Test
public void wildcardSearchTest() {
    WildcardSearch search = new WildcardSearch("a*b");
    assertTrue(search.doesMatch("acdb"));
}

@Test
public void wildcardSearchTest2() {
    WildcardSearch search = new WildcardSearch("a*c*d");
    assertTrue(search.doesMatch("axcydzd"));
}

@Test
public void wildcardSearchTest3() {
    WildcardSearch search = new WildcardSearch("*a*");
    assertTrue(search.doesMatch("xbaax"));
}

@Test
public void wildcardSearchTest4() {
    WildcardSearch search = new WildcardSearch("a*a*a");
    assertTrue(search.doesMatch("aaabaaabaaaa"));
}

@Test
public void wildcardSearchTest5() {
    WildcardSearch search = new WildcardSearch("abc*def");
    assertTrue(search.doesMatch("abcdefdef"));
}

@Test
public void wildcardSearchTest6() {
    WildcardSearch search = new WildcardSearch("*xyz*");
    assertTrue(search.doesMatch("abcxyzdefxyzghi"));
}

@Test
public void wildcardSearchTest7() {
    WildcardSearch search = new WildcardSearch("a*b*c*");
    assertTrue(search.doesMatch("axbxcydzcz"));
}

@Test
public void wildcardSearchTest8() {
    WildcardSearch search = new WildcardSearch("*abc");
    assertTrue(search.doesMatch("xyzabc"));
}



}