package a4j_2;
import java.util.ArrayList;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.io.Serializable;
public class Test__Directors__Meta_Llama_3_70B_Instruct__1 {
@Test
public void testGetDirectorCount() {
    Directors directors = new Directors();
    directors.setDirector(new String[] {"Director1", "Director2", "Director3"});
    assertEquals(3, directors.getDirectorsArray().size());
}

@Test
public void testToString() {
    Directors directors = new Directors();
    directors.setDirector(new String[] {"Director1", "Director2", "Director3"});
    assertEquals("# of Directors = 3\nDirector - Director1\nDirector - Director2\nDirector - Director3\n", directors.toString());
}



}