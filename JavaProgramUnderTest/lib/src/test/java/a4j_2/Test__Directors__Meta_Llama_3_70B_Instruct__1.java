package a4j_2;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import java.io.Serializable;
public class Test__Directors__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testGetDirectorSize() {
    Directors directors = new Directors();
    directors.setDirector(new String[]{"John Doe"});
    assertEquals(1, directors.getDirectorsArray().size());
}

    @Test
    public void testGetDirectorSize99() {
        Directors directors = new Directors();
        directors.setDirector(new String[]{"John Doe"});
        assertEquals(1, directors.getDirectorsArray().size());
    }

}