package a4j_2;
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import java.io.Serializable;
public class Test__Directors__Mixtral_8x7B_Instruct_v0_1 {
@Test
    public void testGetDirector() {
        // Create a Director object with some sample data
        Directors directors = new Directors();
        ArrayList<String> directorsList = new ArrayList<>();
        directorsList.add("Christopher Nolan");
        directorsList.add("Steven Spielberg");
        directorsList.add("Martin Scorsese");
        directors.setDirector(directorsList.toArray(new String[0]));
        
        // Assert that the getDirector() method returns the correct array of strings
        String[] expectedDirectors = {"Christopher Nolan", "Steven Spielberg", "Martin Scorsese"};
        assertArrayEquals(expectedDirectors, directors.getDirector());
    }

@Test
    public void testSettingAndRetrievingDirectors() {
        // Create a Director object and initialize it with some sample data
        Directors directors = new Directors();
        String[] directorNames = {"Alfonso Cuaron", "Denis Villeneuve"};
        directors.setDirector(directorNames);

        // Assert that the number of directors is correct
        int expectedNumberOfDirectors = directorNames.length;
        assertEquals(expectedNumberOfDirectors, directors.getDirector().length);

        // Assert that each director name is present in the list
        ArrayList<String> directorsList = directors.getDirectorsArray();
        for (String name : directorNames) {
            assertTrue(directorsList.contains(name));
        }
    }

}