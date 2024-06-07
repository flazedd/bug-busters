package battlecry_72;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__2 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("example", "ehk 1 s ahm p uh l");
    assertEquals("1 s ahm p uh l", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForHello() {
    bcWord word = new bcWord("hello", "h 1 eh l oh");
    assertEquals("1 eh l oh", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForShortWord() {
    bcWord word = new bcWord("no", "n 0");
    assertEquals("0", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForMultiSyllableWord() {
    bcWord word = new bcWord("banana", "b 1 ae n 2 ah");
    assertEquals("2 ah", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForSingleSyllableWord() {
    bcWord word = new bcWord("dog", "d 0 og");
    assertEquals("0 og", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForWordWithNoSyllableMarkers() {
    bcWord word = new bcWord("hello", "h eh l oh");
    assertEquals("h eh l oh", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForWordWithMultipleSyllableMarkers() {
    bcWord word = new bcWord("communication", "k 1 ah m 2 y uh 1 n 2 eh k 2 ey sh uh n");
    assertEquals("2 ey sh uh n", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyForWordWithConsecutiveSyllableMarkers() {
    bcWord word = new bcWord("cooperation", "k 1 ow 1 eh p 2 er 2 ey sh uh n");
    assertEquals("2 ey sh uh n", word.getRhymeKey(true));
}



}