package openjms_66;
import java.util.Arrays;
import java.util.Hashtable;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__10 {
@Test
public void testCommandLine() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertTrue(cmd.isParameter("option1"));
    assertTrue(cmd.isSwitch("option2"));
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineWithDefault() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertEquals("defaultValue", cmd.value("option3", "defaultValue"));
}
@Test
public void testCommandLineAddOption() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", null);
    assertTrue(cmd.isSwitch("option1"));
}
@Test
public void testCommandLineAddParameter() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    assertTrue(cmd.isParameter("option1"));
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineExists() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option2"});
    assertTrue(cmd.exists("option1"));
    assertTrue(cmd.exists("option2"));
    assertFalse(cmd.exists("option3"));
}
@Test
public void testCommandLineOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option1", "value2", true);
    assertEquals("value2", cmd.value("option1"));
}
@Test
public void testCommandLineNoOverwrite() {
    CommandLine cmd = new CommandLine();
    cmd.add("option1", "value1");
    cmd.add("option1", "value2", false);
    assertEquals("value1", cmd.value("option1"));
}
@Test
public void testCommandLineMultipleValues() {
    CommandLine cmd = new CommandLine(new String[] {"-option1", "value1", "-option1", "value2"});
    assertTrue(cmd.isParameter("option1"));
    assertEquals("value2", cmd.value("option1"));
}
}