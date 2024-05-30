package battlecry_72;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("battlecry", "b  AE1 t  t l k r aI 0");
    assertEquals("AE1 t  t l k r aI 0", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKeyHello() {
    bcWord word = new bcWord("hello", "h  LO 0");
    assertEquals("0", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyCloud() {
    bcWord word = new bcWord("cloud", "kloud 0");
    assertEquals("0", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyTable() {
    bcWord word = new bcWord("table", "tay bul 2");
    assertEquals("2", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyCastle() {
    bcWord word = new bcWord("castle", "kas tul 2");
    assertEquals("2", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyRiver() {
    bcWord word = new bcWord("river", "ri ver 2");
    assertEquals("2", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyMountain() {
    bcWord word = new bcWord("mountain", "moun tin 2");
    assertEquals("2", word.getRhymeKey(true));
}

@Test
public void testGetRhymeKeyValley() {
    bcWord word = new bcWord("valley", "val lee 2");
    assertEquals("2", word.getRhymeKey(true));
}

}