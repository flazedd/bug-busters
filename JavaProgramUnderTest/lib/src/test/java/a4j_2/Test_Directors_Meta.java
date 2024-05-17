package a4j_2;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.Serializable;
import java.util.ArrayList;
public class Test_Directors_Meta {
@Test
    public void testSetAndGetDirector() {
        Directors directors = new Directors();
        String[] directorArray = {"Director 1", "Director 2", "Director 3"};
        directors.setDirector(directorArray);

        String[] retrievedArray = directors.getDirector();
        assertArrayEquals(directorArray, retrievedArray);
    }

@Test
    public void testSetAndGetDirectorsArray() {
        Directors directors = new Directors();
        String[] directorArray = {"Director 1", "Director 2", "Director 3"};
        directors.setDirector(directorArray);

        ArrayList<String> retrievedList = directors.getDirectorsArray();
        assertEquals(3, retrievedList.size());
        assertEquals("Director 1", retrievedList.get(0));
        assertEquals("Director 2", retrievedList.get(1));
        assertEquals("Director 3", retrievedList.get(2));
    }

}