package openjms_66;
import java.util.Arrays;
import java.util.Hashtable;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__5 {
@Test
public void testCommandLine() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertTrue(cmd.isParameter("option1"));
    assertTrue(cmd.isSwitch("option2"));
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineAdd() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option2", null);
    assertTrue(cmd.isParameter("option1"));
    assertTrue(cmd.isSwitch("option2"));
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineExists() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "value1", "-option2"});
    assertTrue(cmd.exists("option1"));
    assertTrue(cmd.exists("option2"));
    assertFalse(cmd.exists("option3"));
}
@Test
public void testCommandLineDefaultValue() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "value1"});
    assertEquals("value1", cmd.value("option1", "default"));
    assertEquals("default", cmd.value("option2", "default"));
}
@Test
public void testCommandLineAddOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option1", "value2", true);
    assertEquals("value2", cmd.value("option1"));
    cmd.add("option1", "value3", false);
    assertEquals("value2", cmd.value("option1"));
}
@Test
public void testCommandLineNoArgs() {
    CommandLine cmd = new CommandLine(new String[0]);
    assertFalse(cmd.exists("option1"));
    assertFalse(cmd.isSwitch("option1"));
    assertFalse(cmd.isParameter("option1"));
    assertNull(cmd.value("option1"));
}
@Test
public void testCommandLineMultipleValues() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "value1", "-option1", "value2"});
    assertTrue(cmd.isParameter("option1"));
    assertEquals("value2", cmd.value("option1"));
}
@Test
public void testCommandLineProcessCommandLine() {
    CommandLine cmd = new CommandLine(new String[]{"-option1", "-option2", "value2", "-option3"});
    assertTrue(cmd.isSwitch("option1"));
    assertTrue(cmd.isSwitch("option3"));
    assertTrue(cmd.isParameter("option2"));
    assertEquals("value2", cmd.value("option2"));
}
}