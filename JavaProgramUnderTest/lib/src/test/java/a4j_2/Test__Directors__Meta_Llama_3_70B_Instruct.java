package a4j_2;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import static org.junit.jupiter.api.Assertions.*;
import java.io.Serializable;
public class Test__Directors__Meta_Llama_3_70B_Instruct {
    @Test
    public void testGetDirectorArray() {
        Directors directors = new Directors();
        directors.setDirector(new String[]{"Director1", "Director2"});
        ArrayList directorArray = directors.getDirectorsArray();
        assertNotNull(directorArray);
    }

    @Test
    public void testGetDirectorArray8() {
        Directors directors = new Directors();
        directors.setDirector(new String[]{"Director1", "Director2"});
        ArrayList directorArray = directors.getDirectorsArray();
        assertNotNull(directorArray);
    }

}