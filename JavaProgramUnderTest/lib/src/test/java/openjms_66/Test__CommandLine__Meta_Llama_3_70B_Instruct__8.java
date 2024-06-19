package openjms_66;
import java.util.Hashtable;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import java.util.Vector;
import static org.junit.jupiter.api.Assertions.*;
public class Test__CommandLine__Meta_Llama_3_70B_Instruct__8 {
@Test
public void testCommandLine() {
    String[] args = new String[]{"-option1", "value1", "-option2"};
    CommandLine commandLine = new CommandLine(args);
    assertTrue(commandLine.exists("option1"));
}
@Test
public void testCommandLineSwitch() {
    String[] args = new String[]{"-switch1", "-switch2", "value2"};
    CommandLine commandLine = new CommandLine(args);
    assertTrue(commandLine.isSwitch("switch1"));
}
@Test
public void testCommandLineValue() {
    String[] args = new String[]{"-option1", "value1", "-option2", "value2"};
    CommandLine commandLine = new CommandLine(args);
    assertEquals("value1", commandLine.value("option1"));
}
@Test
public void testCommandLineDefaultValue() {
    String[] args = new String[]{"-option1", "value1"};
    CommandLine commandLine = new CommandLine(args);
    assertEquals("default", commandLine.value("option2", "default"));
}
@Test
public void testCommandLineAdd() {
    CommandLine commandLine = new CommandLine();
    commandLine.add("option1", "value1");
    assertTrue(commandLine.exists("option1"));
}
@Test
public void testCommandLineIsParameter() {
    String[] args = new String[]{"-option1", "value1", "-option2"};
    CommandLine commandLine = new CommandLine(args);
    assertTrue(commandLine.isParameter("option1"));
}
@Test
public void testCommandLineOverwrite() {
    CommandLine commandLine = new CommandLine();
    commandLine.add("option1", "value1");
    commandLine.add("option1", "value2", true);
    assertEquals("value2", commandLine.value("option1"));
}
@Test
public void testCommandLineNoOverwrite() {
    CommandLine commandLine = new CommandLine();
    commandLine.add("option1", "value1");
    commandLine.add("option1", "value2", false);
    assertEquals("value1", commandLine.value("option1"));
}
}