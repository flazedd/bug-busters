package battlecry_72;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__5 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("hello", "h el 0 lo");
    assertEquals("0 lo", word.getRhymeKey(true));
}
@Test
public void testEqualTo() {
    bcWord word = new bcWord("battlecry", "b at 0 tl kry");
    word.setEqualWord("cry", "kry");
    assertTrue(word.equalTo("cry"));
}
@Test
public void testGetSyllables() {
    bcWord word = new bcWord("example", "ex 1 am 0 ple");
    assertEquals(2, word.getSyllables());
}
@Test
public void testGetMetricCode() {
    bcWord word = new bcWord("hello", "h el 0 lo");
    assertEquals("O", word.getMetricCode());
}
@Test
public void testGetWord() {
    bcWord word = new bcWord("test", "t 0 est");
    assertEquals("test", word.getWord());
}
@Test
public void testGetPhonemes() {
    bcWord word = new bcWord("example", "ex 1 am 0 ple");
    assertEquals("ex 1 am 0 ple", word.getPhonemes());
}
@Test
public void testSetEqualWord() {
    bcWord word = new bcWord("battlecry", "b at 0 tl kry");
    word.setEqualWord("cry", "kry");
    assertEquals("kry", word.getPhonemes());
}
@Test
public void testGetRhymeKeySingleSyllable() {
    bcWord word = new bcWord("hello", "h el 0 lo");
    assertEquals("0 lo", word.getRhymeKey(true));
}
}