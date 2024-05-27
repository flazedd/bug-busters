package beanbin_15;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testWildcardSearch() {
    WildcardSearch search = new WildcardSearch("he*o");
    assertTrue(search.doesMatch("hello"));
}

@Test
public void testWildcardSearch2() {
    WildcardSearch search = new WildcardSearch("*world");
    assertTrue(search.doesMatch("helloworld"));
}

@Test
public void testWildcardSearch4() {
    WildcardSearch search = new WildcardSearch("a*c");
    assertTrue(search.doesMatch("abc"));
}

@Test
public void testWildcardSearch5() {
    WildcardSearch search = new WildcardSearch("*a*b*c*");
    assertTrue(search.doesMatch("xaybzc"));
}

@Test
public void testWildcardSearch6() {
    WildcardSearch search = new WildcardSearch("a*b*c*");
    assertTrue(search.doesMatch("abcdefgabc"));
}

@Test
public void testWildcardSearch8() {
    WildcardSearch search = new WildcardSearch("a*b*c*d");
    assertTrue(search.doesMatch("axbxcxd"));
}

@Test
public void testWildcardSearch9() {
    WildcardSearch search = new WildcardSearch("*abc*def*ghi*");
    assertTrue(search.doesMatch("xabcxyzdefpqrghijk"));
}

@Test
public void testWildcardSearch10() {
    WildcardSearch search = new WildcardSearch("abc*def*ghi*jkl*mno*pqr*stu*vwx*y*z");
    assertTrue(search.doesMatch("abcdefghijklmnopqrstuvwxyz"));
}

}