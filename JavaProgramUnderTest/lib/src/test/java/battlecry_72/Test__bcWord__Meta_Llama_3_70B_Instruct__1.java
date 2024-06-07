package battlecry_72;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("example", "ehk 1 s ahm p uh l");
    assertEquals("1 s ahm p uh l", word.getRhymeKey(true));
}

@Test
public void testEqualTo() {
    bcWord word = new bcWord("battlecry", "b ae t uh l k r ahy");
    word.setEqualWord("cry", "k r ahy");
    assertTrue(word.equalTo("cry"));
}

@Test
public void testGetMetricCode() {
    bcWord word = new bcWord("example", "ehk 1 s ahm p uh l");
    assertEquals("I", word.getMetricCode());
}

@Test
public void testGetSyllables() {
    bcWord word = new bcWord("example", "ehk 1 s ahm p uh l");
    assertEquals(1, word.getSyllables());
}

@Test
public void testGetRhymeKey2() {
    bcWord word = new bcWord("hello", "h eh 1 l o");
    assertEquals("1 l o", word.getRhymeKey(true));
}

@Test
public void testGetWord() {
    bcWord word = new bcWord("hello", "h eh 1 l o");
    assertEquals("hello", word.getWord());
}

@Test
public void testGetPhonemes() {
    bcWord word = new bcWord("hello", "h eh 1 l o");
    assertEquals("h eh 1 l o", word.getPhonemes());
}

@Test
public void testEqualTo2() {
    bcWord word = new bcWord("battlecry", "b ae t uh l k r ahy");
    word.setEqualWord("cry", "k r ahy");
    assertTrue(word.equalTo("battlecry"));
}















}