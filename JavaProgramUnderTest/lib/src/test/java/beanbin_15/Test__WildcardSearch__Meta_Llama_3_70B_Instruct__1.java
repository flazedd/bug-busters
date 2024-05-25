package beanbin_15;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__WildcardSearch__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testWildcardSearch() {
    WildcardSearch search = new WildcardSearch("a*b");
    assertTrue(search.doesMatch("axb"));
}

@Test
public void testWildcardSearchSingleChar() {
    WildcardSearch search = new WildcardSearch("a");
    assertTrue(search.doesMatch("a"));
}

}