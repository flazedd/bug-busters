package battlecry_72;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__3 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("battlecry", "batl kray 1");
    assertEquals("1", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKeySingleSyllable() {
    bcWord word = new bcWord("cat", "kat 1");
    assertEquals("1", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKeyNoSyllables() {
    bcWord word = new bcWord("a", "a");
    assertEquals("a", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKeyNoPhonemes() {
    bcWord word = new bcWord("test", "");
    assertEquals("", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKeyWordWithNoVowels() {
    bcWord word = new bcWord("rhythm", "r h th m 1");
    assertEquals("1", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKeyForExample() {
    bcWord word = new bcWord("example", "ex 0 am ple");
    assertEquals("0 am ple", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForHello() {
    bcWord word = new bcWord("hello", "h 0 el lo");
    assertEquals("0 el lo", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForWorld() {
    bcWord word = new bcWord("world", "w 0 rld");
    assertEquals("0 rld", word.getRhymeKey(true));
}

}