package battlecry_72;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Arrays;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__6 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("battlecry", "b at el kr ai 1");
    assertEquals("1", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKeyForBattlecryUpdatedAgainAndAgainAndAgain() {
    bcWord word = new bcWord("battlecry", "b  ae1 t  t l k r aI 0");
    String rhymeKey = word.getRhymeKey(true);
    assertEquals("0", rhymeKey);
}
@Test
public void testGetRhymeKeyForHelloUpdatedAgain() {
    bcWord word = new bcWord("hello", "h  eh1 l  o 0");
    String rhymeKey = word.getRhymeKey(true);
    assertEquals("0", rhymeKey);
}
@Test
public void testGetRhymeKeyForGoodbyeUpdatedAgain() {
    bcWord word = new bcWord("goodbye", "g  uu1 d  b aI 0");
    String rhymeKey = word.getRhymeKey(true);
    assertEquals("0", rhymeKey);
}
@Test
public void testGetRhymeKeyForBattlecry() {
    bcWord word = new bcWord("battlecry", "b AE1 t t l k r ai");
    assertEquals("AE1 t t l k r ai", word.getRhymeKey(true));
}
@Test
public void testGetRhymeKeyForHello() {
    bcWord word = new bcWord("hello", "h EH0 L LO");
    assertEquals("EH0 L LO", word.getRhymeKey(true));
}
@Test
public void testGetRhymeKeyForCloudy() {
    bcWord word = new bcWord("cloudy", "KL AW0 D I");
    assertEquals("AW0 D I", word.getRhymeKey(true));
}
@Test
public void testGetRhymeKeyForRhythm() {
    bcWord word = new bcWord("rhythm", "R IH1 DH AH0 M");
    assertEquals("AH0 M", word.getRhymeKey(true));
}
}