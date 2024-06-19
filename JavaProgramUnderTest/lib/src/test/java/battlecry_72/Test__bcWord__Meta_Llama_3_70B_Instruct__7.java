package battlecry_72;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__7 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("hello", "h EH1 l oU 0");
    assertEquals("EH1 l oU 0", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKey4() {
    bcWord word = new bcWord("example", "IG ZAE1 M P 1 L");
    assertEquals("1 L", word.getRhymeKey(true));
}
@Test
public void testGetRhymeKey5() {
    bcWord word = new bcWord("university", "Y UW1 N I V ER0 S I T I 0");
    assertEquals("ER0 S I T I 0", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKey6() {
    bcWord word = new bcWord("communication", "K AH0 M Y UW1 N I K EY0 SH UH N");
    assertEquals("EY0 SH UH N", word.getRhymeKey(true));
}
@Test
public void testGetRhymeKey7() {
    bcWord word = new bcWord("authorization", "AA TH EH0 R IH0 Z EY1 SH UH N");
    assertEquals("EY1 SH UH N", word.getRhymeKey(true));
}
@Test
public void testGetRhymeKey8() {
    bcWord word = new bcWord("conversation", "K AH0 N V ER0 S EY1 SH UH N");
    assertEquals("ER0 S EY1 SH UH N", word.getRhymeKey(false));
}
@Test
public void testGetRhymeKey9() {
    bcWord word = new bcWord("declaration", "D EH0 K L EH0 R EY1 SH UH N");
    assertEquals("EY1 SH UH N", word.getRhymeKey(true));
}
@Test
public void testGetRhymeKey10() {
    bcWord word = new bcWord("investigation", "IN V EH1 S T IH0 G EY1 SH UH N");
    assertEquals("EY1 SH UH N", word.getRhymeKey(true));
}
}