package battlecry_72;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("hello", "h 1 e l l o");
    assertEquals("1 e l l o", word.getRhymeKey(true));
}
@Test
public void testEqualTo() {
    bcWord word = new bcWord("battlecry", "b 1 a t t l e c r y");
    word.setEqualWord("cry", "c r y");
    assertTrue(word.equalTo("cry"));
}
@Test
public void testGetMetricCode() {
    bcWord word = new bcWord("example", "e 1 x a m p l e");
    assertEquals("I", word.getMetricCode());
}
@Test
public void testGetSyllables() {
    bcWord word = new bcWord("unbelievable", "u 0 n b 1 e l i 2 e v a b l e");
    assertEquals(3, word.getSyllables());
}
@Test
public void testParsePhonemes() {
    bcWord word = new bcWord("unbreakable", "u 0 n b 1 r 2 e a k a b l e");
    assertEquals("012", word.getMetricCode());
}
@Test
public void testGetWord() {
    bcWord word = new bcWord("example", "e 1 x a m p l e");
    assertEquals("example", word.getWord());
}
@Test
public void testGetPhonemes() {
    bcWord word = new bcWord("unbelievable", "u 0 n b 1 e l i 2 e v a b l e");
    assertEquals("u 0 n b 1 e l i 2 e v a b l e", word.getPhonemes());
}
@Test
public void testEqualToIgnoreCase() {
    bcWord word = new bcWord("Battlecry", "b 1 a t t l e c r y");
    assertTrue(word.equalTo("battlecry"));
}
}