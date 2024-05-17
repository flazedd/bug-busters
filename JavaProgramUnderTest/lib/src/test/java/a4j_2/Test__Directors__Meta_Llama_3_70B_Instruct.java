package a4j_2;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.Serializable;
import java.util.ArrayList;
public class Test__Directors__Meta_Llama_3_70B_Instruct {
@Test
public void testGetDirector() {
    Directors directors = new Directors();
    String[] newString = {"Director1", "Director2", "Director3"};
    directors.setDirector(newString);
    String[] result = directors.getDirector();
    assertArrayEquals(newString, result);
}

@Test
public void testToString() {
    Directors directors = new Directors();
    String[] newString = {"Director1", "Director2", "Director3"};
    directors.setDirector(newString);
    String expectedResult = "# of Directors = 3\nDirector - Director1\nDirector - Director2\nDirector - Director3\n";
    assertEquals(expectedResult, directors.toString());
}

}