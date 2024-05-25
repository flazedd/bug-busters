package battlecry_72;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("battlecry", "b æ t əl k r aɪ 1");
    assertEquals("1", word.getRhymeKey(false));
}

@Test
public void testEqualTo() {
    bcWord word = new bcWord("battlecry", "b æ t əl k r aɪ 1");
    word.setEqualWord("cry", "k r aɪ 1");
    assertTrue(word.equalTo("cry"));
}

}