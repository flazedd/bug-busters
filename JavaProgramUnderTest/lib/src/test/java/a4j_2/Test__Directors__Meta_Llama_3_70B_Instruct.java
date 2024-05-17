package a4j_2;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import java.io.Serializable;
import static org.junit.jupiter.api.Assertions.*;
public class Test__Directors__Meta_Llama_3_70B_Instruct {
@Test
public void testGetDirectorArray() {
    Directors directors = new Directors();
    String[] directorArray = {"Director1", "Director2", "Director3"};
    directors.setDirector(directorArray);
    ArrayList<String> expectedList = new ArrayList<String>();
    expectedList.add("Director1");
    expectedList.add("Director2");
    expectedList.add("Director3");
    assertEquals(expectedList, directors.getDirectorsArray());
}

@Test
public void testToString() {
    Directors directors = new Directors();
    String[] directorArray = {"Director1", "Director2", "Director3"};
    directors.setDirector(directorArray);
    String expectedString = "# of Directors = 3\nDirector - Director1\nDirector - Director2\nDirector - Director3\n";
    assertEquals(expectedString, directors.toString());
}

}