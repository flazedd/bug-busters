package a4j_2;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.Serializable;
import java.util.ArrayList;
public class DirectorsTest_LLM {
@Test
void testGetDirectorArray() {
    Directors directors = new Directors();
    directors.setDirector(new String[]{"Director1", "Director2", "Director3"});
    ArrayList<String> directorArray = directors.getDirectorsArray();
    assertNotNull(directorArray);
}

}