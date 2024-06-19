package openjms_66;
import java.util.Arrays;
import java.util.Vector;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Hashtable;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__7 {
@Test
public void testCommandLine() {
    CommandLine cl = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertTrue(cl.isParameter("option1"));
    assertTrue(cl.isSwitch("option2"));
    assertEquals("value1", cl.value("option1"));
}
@Test
public void testCommandLineAdd() {
    CommandLine cl = new CommandLine();
    cl.add("option1", "value1");
    cl.add("option2", null);
    assertTrue(cl.isParameter("option1"));
    assertTrue(cl.isSwitch("option2"));
    assertEquals("value1", cl.value("option1"));
}
@Test
public void testCommandLineDefaultValue() {
    CommandLine cl = new CommandLine();
    cl.add("option1", "value1");
    assertEquals("value1", cl.value("option1", "defaultValue"));
    assertEquals("defaultValue", cl.value("option2", "defaultValue"));
}
@Test
public void testCommandLineExists() {
    CommandLine cl = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertTrue(cl.exists("option1"));
    assertTrue(cl.exists("option2"));
    assertFalse(cl.exists("option3"));
}
@Test
public void testCommandLineOverwrite() {
    CommandLine cl = new CommandLine();
    cl.add("option1", "value1");
    cl.add("option1", "value2", true);
    assertEquals("value2", cl.value("option1"));
    cl.add("option1", "value3", false);
    assertEquals("value2", cl.value("option1"));
}
@Test
public void testCommandLineProcessCommandLine() {
    CommandLine cl = new CommandLine(new String[]{"-option1", "-option2", "value2", "-option3"});
    assertTrue(cl.isSwitch("option1"));
    assertTrue(cl.isParameter("option2"));
    assertEquals("value2", cl.value("option2"));
    assertTrue(cl.isSwitch("option3"));
}
@Test
public void testCommandLineEmpty() {
    CommandLine cl = new CommandLine();
    assertFalse(cl.exists("option1"));
    assertNull(cl.value("option1"));
}
@Test
public void testCommandLineMultipleValues() {
    CommandLine cl = new CommandLine(new String[]{"-option1", "value1", "value2", "-option2", "value3"});
    assertTrue(cl.isParameter("option1"));
    assertEquals("value1", cl.value("option1"));
    assertTrue(cl.isParameter("option2"));
    assertEquals("value3", cl.value("option2"));
}
}