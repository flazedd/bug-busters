package battlecry_72;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
public class Test__bcWord__Meta_Llama_3_70B_Instruct__4 {
@Test
public void testGetRhymeKey() {
    bcWord word = new bcWord("battlecry", "b  AE1 t  t l k r aI 0");
    assertEquals("AE1 t  t l k r aI 0", word.getRhymeKey(false));
}
@Test
public void testRhymeKey() {
    bcWord word = new bcWord("battlecry", "b at el kr ai 1");
    assertEquals("el kr ai", word.getRhymeKey(true));
}

}